#************************************************************
#   Copyright (C) 2023 OSS Nokalva, Inc.  All rights reserved.
#************************************************************

#   THIS FILE IS PROPRIETARY MATERIAL OF OSS NOKALVA, INC.
#   AND MAY BE USED AND DISTRIBUTED ONLY BY DIRECT LICENSEES OF OSS NOKALVA, INC.
#   THIS COPYRIGHT STATEMENT MAY NOT BE REMOVED.

#   Python 3.7 or higher is required!

#   This file was generated for 'Syed Kamal' by 'https://asn1.io/ASN1-Python-Compiler/' at '5/1/2024 2:38:09 PM'

from datetime import datetime, timezone
from decimal import Decimal
from sys import byteorder, maxsize
from typing import  Union, Tuple, List, Any
from math import isnan, log10, pow, floor, trunc
import io

class per:
    class decodingstream:
        def __init__(self, source, encoding_rule: str) -> None:
            if isinstance(source, io.BufferedReader):
                self.buffer = source
            elif isinstance(source, io.BytesIO):
                self.buffer = io.BufferedReader(source)
            else:
                self.buffer = io.BufferedReader(io.BytesIO(source))

            self.__raw_bytes = source
            self.__enc_rule = encoding_rule.upper()
            self.pos = self.buffer.tell()
            self.bit_lock = 0
            self.ui_cache = 0
            self.lock_initial = 0 if source is None else self.buffer.tell()
            self.const_num_bits_word = 64
            self.const_num_bytes_word = 8

        @property
        def aligned(self) -> bool:
            return self.__enc_rule == "PER" or self.__enc_rule == "CPER"

        @property
        def canonical(self) -> bool:
            return self.__enc_rule == "CPER" or self.__enc_rule == "CUPER"

        def ensure_not_beyond_end_of_stream(self) -> None:
            if self.bit_lock > len(self.__raw_bytes) * 8:
                raise ValueError("75003: The current position is beyond the end of the encoding!")

        def is_eof(self) -> bool:
            length = len(self.__raw_bytes) * 8
            if (self.bit_lock == length or length - self.bit_lock < 8):
                return True

            return False

        def get_bytes(self) -> bytearray:
            if isinstance(self.__raw_bytes, bytearray):
                return self.__raw_bytes

        def skip_bits(self, num_bits: int) -> None:
            self.seek(self.bit_lock + num_bits)

        def get_pos(self) -> int:
            return self.pos

        def seek(self, bit_lock) -> None:
            self.bit_lock = bit_lock
            loc = int(bit_lock / self.const_num_bits_word)

            self.buffer.seek(self.lock_initial + self.const_num_bytes_word * loc)

            if self.bit_lock % self.const_num_bits_word != 0:
                self.ui_cache = self.read_cache_from_stream()

        def seek_final(self) -> None:
            loc = int((self.bit_lock + 8 - 1) / 8)

            if loc == 0:
                loc = 1
            self.seek(self.lock_initial + loc)

        def peek_bytes(self, size, offset = 0) -> bytes:
            peeked = self.buffer.read(size + offset)
            self.buffer.seek(self.buffer.tell() - len(peeked))
            return peeked[offset:offset + size]

        def read_bits(self, num_bits: int) -> Tuple[list, bytearray]:
            num_full_bytes = int(num_bits / 8)
            num_remaining_bits = num_bits % 8
            bit_list = []

            byte_array = bytearray()
            if num_full_bytes > 0:
                byte_array = self.read_octets(num_full_bytes)
                for bt in byte_array:
                    str_val = format(bt, '#010b')[2:]
                    bit_list.extend([True if chr == '1' else False for chr in str_val])

            if num_remaining_bits > 0:
                ui = self.read_int(num_remaining_bits)
                bit_list.extend([False] * num_remaining_bits)

                for idx in range(num_remaining_bits, 0, -1):
                    if (ui & 1) != 0:
                        bit_list[num_bits - num_remaining_bits + idx - 1] = True
                    ui >>= 1

            return (bit_list, self.bit_array_to_bytes(bit_list))

        def read_octets(self, num_bytes: int) -> bytearray:
            num_full_words = int(num_bytes / self.const_num_bytes_word)
            num_remaining_bytes = num_bytes % self.const_num_bytes_word
            byte_array = bytearray(num_bytes)
            loc_dest = 0

            for i in range(num_full_words):
                ui_val = self.read_word()

                for i in range(self.const_num_bytes_word):
                    byte_array[loc_dest] = (ui_val >> 8 * (self.const_num_bytes_word - (i + 1))) & 0xFF
                    loc_dest += 1

            if num_remaining_bytes > 0:
                ui_val = self.read_int(8 * num_remaining_bytes)

                for i in range(num_remaining_bytes):
                    byte_array[loc_dest] = (ui_val >> 8 * (num_remaining_bytes - (i + 1))) & 0xFF
                    loc_dest += 1

            return byte_array

        def read_octets_with_indefinite_length(self) -> bytearray:
            length1 = None
            len_reminder = None
            num_octets = self.get_number_of_items_in_fragments(8)
            byte_array = bytearray(num_octets)
            loc_fragment = 0

            while True:
                if self.aligned:
                    self.allign()

                length1 = self.read_int(8)

                if length1 < 0xC0:
                    break

                if length1 == 0xC0:
                    length1 = 0
                    raise ValueError("75001: The length determinant is invalid!")

                if (length1 < 0xC1 or length1 > 0xC4):
                    raise ValueError("75001: The length determinant is invalid!")

                len_fragment = 16384 * (length1 - 0xC0)
                byte_array2 = self.read_octets(len_fragment)
                byte_array[loc_fragment:] = byte_array2

                loc_fragment += len_fragment

            if length1 >= 0x80:
                length2 = self.read_int(8)
                len_reminder = (length1 - 0x80) << 8 | length2
            else:
                len_reminder = length1

            if len_reminder > 0:
                byte_array2 = self.read_octets(len_reminder)
                byte_array[loc_fragment:] = byte_array2

            return byte_array

        def read_bits_with_indefinite_length(self) -> Tuple[int, bytearray]:
            num_bits = self.get_number_of_items_in_fragments(1)
            num_bytes = int((num_bits + 8 - 1) / 8)

            loc_fragment = 0
            byte_array = bytearray(num_bytes)
            len_reminder = None
            length1 = None

            while True:
                if self.aligned:
                    self.allign()

                length1 = self.read_int(8)

                if length1 < 0xC0:
                    break

                if length1 == 0xC0:
                    length1 = 0
                    raise ValueError("75001: The length determinant is invalid!")

                if (length1 < 0xC1 or length1 > 0xC4):
                    raise ValueError("75001: The length determinant is invalid!")

                len_fragment = 16384 * (length1 - 0xC0)
                byte_array2 = self.read_octets(int(len_fragment / 8))
                begin = int(loc_fragment / 8)
                end = begin + len(byte_array2)
                byte_array[begin: end] = byte_array2
                loc_fragment += len_fragment

            if length1 >= 0x80:
                length2 = self.read_int(8)
                len_reminder = (length1 - 0x80) << 8 | length2
            else:
                len_reminder = length1

            num_full_bytes = int(len_reminder / 8)
            num_remaining_bits = len_reminder % 8

            byte_array2 = self.read_octets(num_full_bytes)
            begin = int(loc_fragment / 8)
            end = begin + len(byte_array2)
            byte_array[begin: end] = byte_array2

            if num_remaining_bits > 0:
                _, byte_array2 = self.read_bits(num_remaining_bits)
                byte_array[-1] = byte_array2[0]

            return (num_bits, byte_array)

        def read_septets_with_indefinite_length(self) -> bytearray:
            num_septets = self.get_number_of_items_in_fragments(7)
            byte_array = bytearray(num_septets)
            loc_fragment = 0
            len_reminder = None
            length1 = None

            while True:
                length1 = self.read_int(8)

                if length1 < 0xC0:
                    break

                if length1 == 0xC0:
                    length1 = 0
                    raise ValueError("75001: The length determinant is invalid!")

                if (length1 < 0xC1 or length1 > 0xC4):
                    raise ValueError("75001: The length determinant is invalid!")

                len_fragment = 16384 * (length1 - 0xC0)

                for loc in range(0, len_fragment):
                    byte_array[loc] = self.read_int(7)

                loc_fragment += len_fragment

            if length1 >= 0x80:
                length2 = self.read_int(8)
                len_reminder = (length1 - 0x80) << 8 | length2
            else:
                len_reminder = length1

            if len_reminder > 0:
                for loc in range(loc_fragment, loc_fragment + len_reminder):
                    byte_array[loc] = self.read_int(7)

            return byte_array

        def bit_array_to_bytes(self, bit_list: list) -> bytearray:
            return shared.bit_array_to_bytes(list(bit_list))

        def trim(self, bit_array: list) -> None:
            shared.trim(bit_array)

        def get_number_of_items_in_fragments(self, width_item: int) -> int:
            length1 = None
            len_reminder = None
            len_total = 0
            bit_lock_start = self.bit_lock

            while True:
                if self.aligned:
                    self.allign()

                length1 = self.read_int(8)

                if length1 < 0xC0:
                    break

                if length1 == 0xC0:
                    length1 = 0
                    raise ValueError("75001: The length determinant is invalid!")

                if (length1 < 0xC1 or length1 > 0xC4):
                    raise ValueError("75001: The length determinant is invalid!")

                len_fragment = 16384 * (length1 - 0xC0)
                len_total += len_fragment

                self.skip_bits(len_fragment * width_item)

            if length1 >= 0x80:
                length2 = self.read_int(8)
                len_reminder = (length1 - 0x80) << 8 | length2
            else:
                len_reminder = length1

            len_total += len_reminder
            self.seek(bit_lock_start)

            return len_total

        def allign(self) -> None:
            bit_lock_in_word = self.bit_lock % self.const_num_bits_word
            bit_idx = bit_lock_in_word % 8

            if bit_idx > 0:
                padding = 8 - bit_idx
                self.bit_lock += padding

        def read_int(self, width: int) -> int:
            ui_val = 0
            bit_lock_in_word = self.bit_lock % self.const_num_bits_word

            if bit_lock_in_word == 0:
                self.ui_cache = self.read_cache_from_stream()

            if bit_lock_in_word + width <= self.const_num_bits_word:
                ui_val = self.ui_cache >> (self.const_num_bits_word - bit_lock_in_word - width)
            else:
                num_bits_high = self.const_num_bits_word - bit_lock_in_word
                num_bits_low = width - num_bits_high
                ui_val = self.ui_cache << num_bits_low
                self.ui_cache = self.read_cache_from_stream()
                ui_val |= self.ui_cache >> (self.const_num_bits_word - num_bits_low)

            ui_val &= 0xFFFFFFFFFFFFFFFF >> (self.const_num_bits_word - width)
            self.bit_lock += width

            return ui_val

        def read_word(self) -> int:
            ui_val = None

            bit_lock_in_word = (self.bit_lock % self.const_num_bits_word)

            if bit_lock_in_word == 0:
                ui_val = self.read_cache_from_stream()
            else:
                ui_val = self.ui_cache << bit_lock_in_word
                ui_val &= 0xFFFFFFFFFFFFFFFF
                self.ui_cache = self.read_cache_from_stream()
                ui_val |= self.ui_cache >> (self.const_num_bits_word - bit_lock_in_word)

            self.bit_lock += self.const_num_bits_word
            return ui_val 

        def read_bit(self) -> bool:
            bit_lock_in_word = self.bit_lock % self.const_num_bits_word

            if bit_lock_in_word == 0:
                self.ui_cache = self.read_cache_from_stream()

            ui_val = self.ui_cache >> (self.const_num_bits_word - bit_lock_in_word - 1)
            self.bit_lock += 1

            return (ui_val & 1) != 0

        def read_cache_from_stream(self) -> int:
            ui_val = cnt = 0

            b_arr = bytearray(self.buffer.read(self.const_num_bytes_word))

            for i in b_arr:
                cnt = cnt + 1
                ui_val = ui_val << 8 | i

            if cnt == 0:
                raise ValueError("75002: The end of the encoding was unexpectedly encountered!")

            cnt = cnt + 1
            if cnt <= self.const_num_bytes_word:
                ui_val = ui_val << 8 * (self.const_num_bytes_word - cnt + 1)

            return ui_val

        def decode_fragment(self, code_point_array: list, byte_array: bytes, loc_fragment: int, len_fragment: int, width_item: int, use_code_points: bool, use_alphabet: bool, alphabet: list) -> None:
            if use_code_points:
                if use_alphabet:
                    for loc in range(loc_fragment, loc_fragment + len_fragment):
                        idx = self.read_int(width_item) if width_item > 0 else 0
                        idx_base = 0
                        code_point = 0
                        found = False

                        for code_range in alphabet:
                            if (idx >= idx_base and idx <= idx_base + code_range[1] - code_range[0]):
                                code_point = code_range[0] + idx - idx_base
                                found = True
                                break
                            idx_base += code_range[1] - code_range[0] + 1

                        if not found:
                            raise ValueError("77303: The encoding of the string value contains one or more invalid character indexes!")

                        code_point_array[loc] = code_point
                else:
                    for idx in range(loc_fragment, loc_fragment + len_fragment):
                        code_point = self.read_int(width_item)

                        if (code_point > 0x10FFFF or code_point >= 0xD800 and code_point <= 0xDFFF):
                            code_point = 32
                            raise ValueError("77302: The string value contains one or more invalid characters!")

                        code_point_array[idx] = code_point
            else:
                for idx in range(loc_fragment, loc_fragment + len_fragment):
                    byte_array[idx] = self.read_int(width_item)

        def decode_preamble(self, length: int) -> list:
            byte_array = None
            if length < 65536:
                _, byte_array = self.read_bits(length)
            else:
                _, byte_array = self.read_bits_with_indefinite_length()

            return self.to_bit_list(length, byte_array)

        def to_bit_list(self, length: int, byte_array: bytearray) -> list:
            return shared.to_bit_list(length, byte_array)

    class encodingstream:
        def __init__(self, encoding_rule: str) -> None:
            self.__buffer = bytearray()
            self.pos = 0

            self.__enc_rule = encoding_rule.upper()
            self._num_bits = -1
            self.bit_lock = 0
            self.ui_cache = 0

            self.const_num_bits_word = 64
            self.const_num_bytes_word = int(self.const_num_bits_word / 8)

        @property
        def aligned(self) -> bool:
            return self.__enc_rule == "PER" or self.__enc_rule == "CPER"

        @property
        def canonical(self) -> bool:
            return self.__enc_rule == "CPER" or self.__enc_rule == "CUPER"

        @property
        def buffer(self) -> bytearray:
            return self.__buffer

        def append(self, value: Any) -> None:
            self.pos += len(value)
            self.__buffer.extend(value)

        def get_pos(self) -> int:
            return self.pos

        def get_buffer(self) -> bytearray:
            self.flush()
            return self.buffer

        def get_bit_length(self) -> Tuple[int, None]:
            if self.bit_lock > 0:
                return self.bit_lock

            return None

        def write_word(self, ui: int) -> None:
            bit_lock_in_word = self.bit_lock  % self.const_num_bits_word

            if bit_lock_in_word == 0:
                self.write_word_to_stream(ui)
            else:
                self.ui_cache |= ui >> bit_lock_in_word
                self.write_cache_to_stream()
                self.ui_cache = ui << (self.const_num_bits_word - bit_lock_in_word)

            self.bit_lock += self.const_num_bits_word

        def write_bit(self, extend: bool) -> None:
            bit_lock_in_word = self.bit_lock % self.const_num_bits_word

            if bit_lock_in_word == 0:
                self.ui_cache = 0

            if extend:
                self.ui_cache |= 1 << (self.const_num_bits_word - bit_lock_in_word - 1)

            if bit_lock_in_word + 1 == self.const_num_bits_word:
                self.write_cache_to_stream()

            self.bit_lock += 1

        def write_octets(self, byte_array: bytearray, loc_start: int = 0, length: int = -1) -> None:
            num_bytes = length if (length >= 0) else len(byte_array)

            num_full_words = int(num_bytes / self.const_num_bytes_word)
            num_remaining_bytes = num_bytes % self.const_num_bytes_word
            loc_src = loc_start

            for _ in range (1, num_full_words + 1):
                ui_val = 0

                for _ in range(1, self.const_num_bytes_word + 1):
                    ui_val = ui_val << 8 | byte_array[loc_src]
                    loc_src += 1

                self.write_word(ui_val)

            if num_remaining_bytes > 0:
                ui_val = 0

                for _ in range (1, num_remaining_bytes + 1):
                    ui_val = ui_val << 8 | byte_array[loc_src]
                    loc_src += 1

                self.write_int(ui_val, 8 * num_remaining_bytes)

        def write_bits(self, bits: list) -> None:
            num_bits = len(bits)
            num_full_bytes = int(num_bits / 8)
            num_remaining_bits = num_bits % 8

            if num_full_bytes > 0:
                byte_array = bytearray()
                for byte_idx in range(num_full_bytes):
                    num = int(''.join('1' if idx else '0' for idx in bits[0 + (byte_idx * 8): (byte_idx + 1) * 8]), 2)
                    bts = num.to_bytes(1, byteorder)
                    _ = [byte_array.append(bt) for bt in bts]
                self.write_octets(byte_array)
            if num_remaining_bits > 0:
                ui = 0
                for idx in range(num_full_bytes * 8, num_bits):
                    ui <<= 1
                    if bits[idx]:
                        ui += 1
                self.write_int(ui, num_remaining_bits)

        def write_bits_with_indefinite_length(self, length: int, byte_array: bytearray) -> None:
            num_bits = length
            num_full_bytes = int(num_bits / 8)
            num_remaining_bits = num_bits % 8

            len_remainder = num_bits
            loc_fragment = 0

            while len_remainder >= 16384:
                for idx in range(4, -1, -1):
                    if len_remainder >= 16384 * idx:
                        break
                len_fragment = 16384 * idx

                if self.aligned:
                    self.allign()
                self.write_int(0xC0 + idx, 8)
                self.write_octets(byte_array, int(loc_fragment / 8), int(len_fragment / 8))

                len_remainder -= len_fragment
                loc_fragment += len_fragment

            if self.aligned:
                self.allign()

            if len_remainder >= 128:
                self.write_int(0x8000 + len_remainder, 16)
            else:
                self.write_int(len_remainder, 8)

            if len_remainder > 0:
                self.write_octets(byte_array, int(loc_fragment / 8), int(len_remainder / 8))

            if num_remaining_bits > 0:
                ui = 0
                bit_array = shared.bit_array_from_bytes(length, byte_array)
                for idx in range(num_full_bytes * 8 + 1, num_bits + 1):
                    ui <<= 1

                    if bit_array[idx - 1]:
                        ui += 1

                self.write_int(ui, num_remaining_bits)

        def write_octets_with_indefinite_length(self, byte_array: bytearray) -> None:
            len_reminder = len(byte_array)
            loc_fragment = 0

            while len_reminder >= 16384:
                idx = 4
                while True:
                    if len_reminder >= 16384 * idx:
                        break
                    idx = idx - 1

                len_fragment = 16384 * idx

                if self.aligned:
                    self.allign()

                self.write_int(0xC0 + idx, 8)
                self.write_octets(byte_array, loc_fragment, len_fragment)

                len_reminder -= len_fragment
                loc_fragment += len_fragment

            if self.aligned:
                self.allign()

            if len_reminder >= 128:
                self.write_int(0x8000 + len_reminder, 16)
            else:
                self.write_int(len_reminder, 8)

            self.write_octets(byte_array, loc_fragment, len_reminder)

        def write_septets_with_indefinite_length(self, byte_array: bytearray) -> None:
            len_reminder = len(byte_array)
            loc_fragment = 0

            while len_reminder >= 16384:
                idx = 4
                while True:
                    if len_reminder >= 16384 * idx:
                        break
                    idx = idx - 1

                len_fragment = 16384 * idx
                self.write_int(0xC0 + idx, 8)
                for loc in range(loc_fragment, loc_fragment + len_fragment):
                    self.write_int(byte_array[loc] & 0x7F, 7)

                len_reminder -= len_fragment
                loc_fragment += len_fragment

            if len_reminder >= 128:
                self.write_int(0x8000 + len_reminder, 16)
            else:
                self.write_int(len_reminder, 8)

            for loc in range(loc_fragment, loc_fragment + len_reminder):
                self.write_int(byte_array[loc] & 0x7F, 7)


        def allign(self) -> None:
            bit_lock_in_word = self.bit_lock % self.const_num_bits_word
            bit_idx = bit_lock_in_word % 8

            if bit_idx > 0:
                width = 8 - bit_idx

                if bit_lock_in_word + width == self.const_num_bits_word:
                    self.write_cache_to_stream()
                self.bit_lock += width

        def write_int(self, ui_val: int, width: int) -> None:
            bit_lock_in_word = self.bit_lock % self.const_num_bits_word

            if bit_lock_in_word == 0:
                self.ui_cache = 0

            if bit_lock_in_word + width <= self.const_num_bits_word:
                self.ui_cache |= ui_val << (self.const_num_bits_word - bit_lock_in_word - width)

                if bit_lock_in_word + width == self.const_num_bits_word:
                    self.write_cache_to_stream()
            else:
                num_bits_high = self.const_num_bits_word - bit_lock_in_word
                num_bits_low = width - num_bits_high
                self.ui_cache |= ui_val >> num_bits_low
                self.write_cache_to_stream()
                self.ui_cache = ui_val << (self.const_num_bits_word - num_bits_low)

            self.bit_lock += width

        def flush(self) -> None:
            if self._num_bits == -1:
                bit_lock_in_word = self.bit_lock % self.const_num_bits_word
                num_bytes = int((bit_lock_in_word + 8 - 1) / 8)

                for idx in range(1, num_bytes + 1):
                    self.__buffer.append(self.ui_cache >> 8 * (self.const_num_bytes_word - idx) & 0xFF)

                self._num_bits = self.bit_lock
            if len(self.__buffer) == 0:
                self.__buffer.append(0)

        def write_word_to_stream(self, ui: int) -> None:
            for idx in range (1, self.const_num_bytes_word + 1):
                self.__buffer.append(ui >> 8 * (self.const_num_bytes_word - idx) & 0xFF)

        def write_cache_to_stream(self) -> None:
            self.write_word_to_stream(self.ui_cache)

        def encode_fragment(self, code_point_array: list, byte_array: bytes, loc_fragment: int, len_fragment: int, width_item: int, use_code_point: bool, use_alphabet: bool, alphabet: list) -> None:
            if use_code_point:
                if use_alphabet:
                    for loc in range(loc_fragment, loc_fragment + len_fragment):
                        code_point = code_point_array[loc]
                        idx_base = 0
                        idx = 0
                        found = False

                        for code_range in alphabet:
                            if (code_point >= code_range[0] and code_point <= code_range[1]):
                                idx = idx_base + (code_point - code_range[0])
                                found = True
                                break
                            idx_base += code_range[1] - code_range[0] + 1

                        if not found:
                            raise ValueError("63904: The string value contains one or more characters that cannot be encoded!")
                        if width_item > 0:
                            self.write_int(idx, width_item)
                else:
                    for loc in range(loc_fragment, loc_fragment + len_fragment):
                        self.write_int(code_point_array[loc], width_item)
            else:
                for loc in range(loc_fragment, loc_fragment + len_fragment):
                    self.write_int(byte_array[loc], width_item)

        def encode_preamble(self, bits: list) -> None:
            if (bits is not None and len(bits) < 65536):
                self.write_bits(bits)
            else:
                num_full_bytes = int(bits / 8)
                num_remaining_bits = bits % 8

                bits2 = list(bits)
                length = num_full_bytes
                if num_remaining_bits > 0:
                    length += 1
                    for _ in range(num_remaining_bits):
                        bits2.append(False)

                byte_array = bytearray()
                for byte_idx in range(length):
                    num = int(''.join('1' if idx else '0' for idx in bits[0: (byte_idx + 1) * 8]), 2)
                    bts = num.to_bytes(1, byteorder)
                    _ = [byte_array.append(bt) for bt in bts]

                self.write_bits_with_indefinite_length(len(bits), byte_array)

        def encode_extension_bitmap(self, bits: list) -> None:
            self.write_bit(len(bits) > 64)

            if len(bits) <= 64:
                self.write_int(len(bits) - 1, 6)
                self.write_bits(bits)
            else:
                self.write_bits_with_indefinite_length(len(bits), bits)

        def width_of_range(self, min_int: int, max_int: int) -> int:
            num = max_int - min_int
            cnt = 0

            while num >= 65536:
                cnt += 16
                num >>= 16

            while num >= 256:
                cnt += 8
                num >>= 8

            while num >= 16:
                cnt += 4
                num >>= 4

            while num >= 4:
                cnt += 2
                num >>= 2

            while num >= 1:
                cnt += 1
                num >>= 1

            return cnt

        def get_code_points(self, value: str) -> list:
            code_ponts = []
            for ch in value:
                if len(ch) != 2:
                    code_ponts.append(ord(ch))
                else:
                    code_ponts.append(0x10000 + (ord(ch[0]) - 0xD800) * 0x400 + (ord(ch[1]) - 0xDC00))
            return code_ponts

    @staticmethod
    def decode_integer(stream: decodingstream, **kwargs) -> int:
        width_value = width_length = None
        align_value = align_length = False

        if stream.aligned:
            width_value = kwargs.get("width_value_aligned")
            width_length = kwargs.get("width_length")
            align_value = kwargs.get("align_value")
            align_length = kwargs.get("align_length")
        else:
            width_value = kwargs.get("width_value_unaligned")
            width_length = None
            align_value = False
            align_length = False

        minimum = kwargs.get("minimum")
        extend_value = stream.read_bit() if kwargs.get("has_extensible_value") else False
        value = 0

        unsigned = True if (minimum is not None and extend_value is False) else False

        if (width_value is None or extend_value):
            byte_array = None
            length = None

            if (width_length is None or extend_value):
                byte_array = stream.read_octets_with_indefinite_length()
                length = len(byte_array)
            else:
                if align_length:
                    stream.allign()

                length = stream.read_int(width_length) + 1 if (width_length is not None and width_length > 0) else 1
                stream.allign()
                byte_array = stream.read_octets(length)

            if length == 0:
                raise ValueError("76401: The encoding of the integer value is not well-formed!")
            if length != 0:
                for idx in range(length):
                    value = value << 8 | byte_array[idx]

                if (not unsigned and byte_array[0] >= 0x80):
                    value -= 1 << 8 * length
        else:
            num_whole64_bit_chunks = int(width_value / 64)
            width_first_chunk = width_value % 64

            if align_value:
                stream.allign()

            if width_first_chunk != 0:
                ui_chunk = stream.read_int(width_first_chunk)
                value |= ui_chunk << num_whole64_bit_chunks * 64

            for idx in range(1, num_whole64_bit_chunks + 1):
                ui_chunk = stream.read_word()
                value |= ui_chunk << (num_whole64_bit_chunks - idx) * 64

        if unsigned:
            value += minimum

        return value

    @staticmethod
    def decode_string(stream: decodingstream, **kwargs) -> Union[str, None]:
        width_length = kwargs.get("width_length_aligned") if stream.aligned else kwargs.get("width_length_unaligned")
        width_code_point = kwargs.get("width_alphabet_aligned") if stream.aligned else kwargs.get("width_alphabet_unaligned")
        align_length = kwargs.get("align_length") if stream.aligned else False
        width_idx = kwargs.get("width_index_aligned") if stream.aligned else kwargs.get("width_index_unaligned")

        use_code_points = True if width_code_point is not None else False
        use_alphabet = True if width_idx is not None else False

        code_point_array = None
        byte_array = None
        len_reminder = None
        loc_fragment = 0
        length1 = None
        string_value = None
        width_item = None

        if use_code_points:
            width_item = width_idx if use_alphabet is not False else width_code_point
        else:
            width_item = 8

        extend_size = stream.read_bit() if kwargs.get("has_extensible_size") else False

        if (width_length is None or extend_size):
            num_items = stream.get_number_of_items_in_fragments(width_item)

            if use_code_points:
                code_point_array = [None] * num_items
            else:
                byte_array = bytearray(num_items)

            while True:
                if stream.aligned:
                    stream.allign()

                length1 = stream.read_int(8)

                if length1 < 0xC0:
                    break

                if length1 == 0xC0:
                    length1 = 0
                    raise ValueError("77301: The length determinant of the string encoding is invalid!")

                if (length1 < 0xC1 or length1 > 0xc4):
                    raise ValueError("77301: The length determinant of the string encoding is invalid!")

                len_fragment = 16384 * (length1 - 0xC0)
                stream.decode_fragment(code_point_array, byte_array, loc_fragment, len_fragment, width_item, use_code_points, use_alphabet, kwargs.get("alphabet"))

                loc_fragment += len_fragment

            if length1 >= 0x80:
                length2 = stream.read_int(8)
                len_reminder = (length1 - 0x80) << 8 | length2
            else:
                len_reminder = length1
            stream.decode_fragment(code_point_array, byte_array, loc_fragment, len_reminder, width_item, use_code_points, use_alphabet, kwargs.get("alphabet"))
        else:
            if align_length:
                stream.allign()

            min_root_size = kwargs.get("minimum_root_size")
            max_root_size = kwargs.get("maximum_root_size")
            length1 = stream.read_int(width_length) if width_length is not None and width_length > 0 else 0
            length = min_root_size + length1

            if (stream.aligned and length > 0):
                if (width_length is not None and width_length > 0 and (max_root_size is not None and max_root_size * width_item > 15) or (min_root_size * width_item > 16)):
                    stream.allign()

            if use_code_points:
                code_point_array = [None] * length
            else:
                byte_array = bytearray(length)

            stream.decode_fragment(code_point_array, byte_array, 0, length, width_item, use_code_points, use_alphabet, kwargs.get("alphabet"))

        if code_point_array is not None:
            letters = [chr(letter) for letter in code_point_array]
            string_value = ''.join(letters)
        elif kwargs.get("is_utf8"):
            string_value = byte_array.decode("utf-8")
        else:
            string_value = byte_array.decode("ascii")
            if "\xFF" in string_value:
                string_value = None

        return string_value

    @staticmethod
    def decode_real(stream: decodingstream, **_) -> Union[Any, dict]:
        byte_array = stream.read_octets_with_indefinite_length()
        return shared.decode_real(byte_array)

    @staticmethod
    def decode_enum(stream: decodingstream, **kwargs) -> int:
        width_idx = kwargs.get("width_index_aligned") if stream.aligned else kwargs.get("width_index_unaligned")
        width_length = kwargs.get("width_length_aligned") if stream.aligned else None
        align_idx = kwargs.get("align_index") if stream.aligned else False
        is_extensible = kwargs.get("is_extension") if "is_extension" in kwargs else False
        is_small = is_extensible and not stream.read_bit()
        idx = 0

        if is_small:
            idx = stream.read_int(6)
        elif (width_idx is None or is_extensible):
            byte_array = None
            length = None

            if (width_length is None or is_extensible):
                byte_array = stream.read_octets_with_indefinite_length()
                length = len(byte_array)
            else:
                length = stream.read_int(width_length) + 1 if width_length is not None and width_length > 0 else 1
                stream.allign()
                byte_array = stream.read_octets(length)

            for loc in range(length):
                idx = idx << 8 | byte_array[loc]
        else:
            if align_idx:
                stream.allign()

            idx = stream.read_int(width_idx) if (width_idx is not None and width_idx > 0) else 0

        return idx

    @staticmethod
    def decode_boolean(stream: decodingstream) -> bool:
        return stream.read_bit()

    @staticmethod
    def decode_null(_: decodingstream) -> None:
        return None

    @staticmethod
    def decode_bit_string(stream: decodingstream, **kwargs) -> Union[dict, str]:
        width_length = kwargs.get("width_length_aligned") if stream.aligned else kwargs.get("width_length_unaligned")
        align_length = kwargs.get("align_length") if stream.aligned else False

        extend_size = stream.read_bit() if kwargs.get("has_extensible_size") else False
        min_root_size = kwargs.get("minimum_root_size")
        max_root_size = kwargs.get("maximum_root_size")

        length = 0
        bit_list = []
        byte_array = bytearray()

        if (width_length is None or extend_size):
            length, byte_array = stream.read_bits_with_indefinite_length()
        else:
            if align_length:
                stream.allign()

            length = stream.read_int(width_length) if width_length is not None and width_length > 0 else 0

            if (stream.aligned and min_root_size + length > 0):
                if (width_length is not None and width_length > 0 or min_root_size > 16):
                    stream.allign()

            bit_list, byte_array, = stream.read_bits(min_root_size + length)
            length = len(bit_list)

        if kwargs.get("has_named_bits"):
            if len(bit_list) == 0:
                bit_list = shared.bit_array_from_bytes(length, byte_array)

            shared.trim(bit_list)
            length = len(bit_list)
            if length < min_root_size:
                length = min_root_size

        if min_root_size != max_root_size or length % 8 != 0:
            return {"length": length, "value": byte_array.hex().upper()}

        return byte_array.hex().upper()

    @staticmethod
    def decode_octet_string(stream: decodingstream, **kwargs) -> bytearray:
        width_length = kwargs.get("width_length_aligned") if stream.aligned else kwargs.get("width_length_unaligned")
        align_length = kwargs.get("align_length") if stream.aligned else False

        extend_size = stream.read_bit() if kwargs.get("has_extensible_size") else False
        min_root_size = kwargs.get("minimum_root_size")
        byte_array = None

        if (width_length is None or extend_size):
            byte_array = stream.read_octets_with_indefinite_length()
        else:
            if align_length:
                stream.allign()

            length1 = stream.read_int(width_length) if width_length is not None and width_length > 0 else 0

            if (stream.aligned and min_root_size + length1 > 0):
                if (width_length > 0 or min_root_size > 2):
                    stream.allign()

            byte_array = stream.read_octets(min_root_size + length1)

        return byte_array.hex().upper()

    @staticmethod
    def decode_absolute_oid(stream: decodingstream) -> Union[str, list]:
        byte_array = stream.read_octets_with_indefinite_length()

        oid_list = shared.decode_absolute_oid(byte_array)
        return ".".join([str(oid) for oid in oid_list])

    @staticmethod
    def decode_relative_oid(stream: decodingstream) -> str:
        byte_array = stream.read_octets_with_indefinite_length()

        oid_list = shared.decode_relative_oid(byte_array)
        return ".".join([str(oid) for oid in oid_list])

    @staticmethod
    def decode_oid_iri(stream: decodingstream) -> str:
        byte_array = stream.read_octets_with_indefinite_length()
        return shared.decode_oid_iri(byte_array)

    @staticmethod
    def decode_generalized_time(stream: decodingstream) -> str:
        byte_array = None

        if stream.aligned:
            byte_array = stream.read_octets_with_indefinite_length()
        else:
            byte_array = stream.read_septets_with_indefinite_length()

        return shared.decode_time(byte_array, False)

    @staticmethod
    def decode_utc_time(stream: decodingstream) -> str:
        byte_array = None
        if stream.aligned:
            byte_array = stream.read_octets_with_indefinite_length()
        else:
            byte_array = stream.read_septets_with_indefinite_length()

        return shared.decode_time(byte_array, True)

    @staticmethod
    def decode_sequence_of(stream: decodingstream, encoding_rule: str, components: list, value_tracker: dict, decode_components: callable, **kwargs) -> int:
        width_length = kwargs.get("width_length_aligned") if stream.aligned else kwargs.get("width_length_unaligned")
        align_length = kwargs.get("align_length") if stream.aligned else False

        extend_size = stream.read_bit() if kwargs.get("has_extensible_size") else False
        min_root_size = kwargs.get("minimum_root_size")
        length = None
        len_remainder = None

        if (width_length is None or extend_size):
            while True:
                if stream.aligned:
                    stream.allign()

                length = stream.read_int(8)

                if length < 0xC0:
                    break

                if length == 0xC0:
                    length = 0
                    raise ValueError("77101: The length determinant of the sequence-of or set-of encoding is invalid!")

                if (length < 0xC1 or length > 0xC4):
                    raise ValueError("77101: The length determinant of the sequence-of or set-of encoding is invalid!")

                len_fragment = 16384 * (length - 0xC0)
                decode_components(encoding_rule, stream, value_tracker, components, len_fragment)

            if (length is not None and length >= 0x80):
                length2 = stream.read_int(8)
                len_remainder = (length - 0x80) << 8 | length2
            else:
                len_remainder = length
        else:
            if align_length:
                stream.allign()

            length = stream.read_int(width_length) if width_length is not None and width_length > 0 else 0
            len_remainder = min_root_size + length

        return len_remainder

    @staticmethod
    def decode_choice_preamble(stream: decodingstream, **kwargs) -> Tuple[int, bool]:
        width_idx = kwargs.get("width_index_aligned") if stream.aligned else kwargs.get("width_index_unaligned")
        width_length = kwargs.get("width_length_aligned") if stream.aligned else None
        align_idx = kwargs.get("align_index") if stream.aligned else False

        is_extension = stream.read_bit() if kwargs.get("is_extensible") else False
        is_small = not stream.read_bit() if is_extension else False
        idx = 0

        if is_small:
            idx = stream.read_int(6)
        elif (width_idx is None or is_extension):
            hex_val = bytearray()
            length = 0
            if (width_length is None or is_extension):
                hex_val = stream.read_octets_with_indefinite_length()
                length = len(hex_val)
            else:
                length = stream.read_int(width_length) + 1 if width_length is not None and width_length > 0 else 1
                stream.allign()
                hex_val = stream.read_octets(length)

            for loc in range(0, length):
                idx = idx << 8 | hex_val[loc]
        else:
            if align_idx:
                stream.allign()
            idx = stream.read_int(width_idx) if width_idx is not None and width_idx > 0 else 0

        return (idx, is_extension)

    @staticmethod
    def encode_integer(stream: encodingstream, value: int, **kwargs) -> None:
        if not isinstance(value, int):
            try:
                value = int(value)
            except Exception as exc:
                raise TypeError("65201: The value class containing the value to be encoded does not match the type specified in the schema!") from exc

        width_value = width_length = None
        align_value = align_length = False

        if stream.aligned:
            width_value = kwargs.get("width_value_aligned")
            width_length = kwargs.get("width_length")
            align_value = kwargs.get("align_value")
            align_length = kwargs.get("align_length")
        else:
            width_value = kwargs.get("width_value_unaligned")
            width_length = None
            align_value = False
            align_length = False

        minimum = kwargs.get("minimum")
        maximum = kwargs.get("maximum")

        extend_value = True if (minimum is not None and value < minimum or maximum is not None and value > maximum) else False

        if (kwargs.get("has_extensible_value") is True):
            stream.write_bit(extend_value)

        if (extend_value and kwargs.get("has_extensible_value") is False):
            raise ValueError("63001: The integer value is outside the encodable range!")

        unsigned = (minimum is not None and not extend_value)

        if unsigned:
            value -= minimum

        if (width_value is None or extend_value):
            length = None

            if value == 0:
                length = 1
            elif value < 0:
                length = int((stream.width_of_range(value, 0) + 8 - 1) / 8)

                if (value & (1 << (8 * length - 1))) == 0:
                    length = length + 1

            else:
                length = int((stream.width_of_range(0, value) + 8 - 1) / 8)

                if (not unsigned and (value & (1 << (8 * length - 1))) != 0):
                    length = length + 1

            byte_array = bytearray(length)

            for idx in range(length - 1, -1, -1):
                byte_array[idx] = value & 0xFF
                value >>= 8

            if width_length is None or extend_value:
                stream.write_octets_with_indefinite_length(byte_array)
            else:
                if align_length:
                    stream.allign()

                if (width_length is not None and width_length > 0):
                    stream.write_int(length - 1, width_length)

                stream.allign()
                stream.write_octets(byte_array, 0, -1)
        else:
            num_whole_64bit_chunks = int(width_value / 64)
            width_first_chunk = width_value % 64

            if align_value:
                stream.allign()

            if width_first_chunk != 0:
                ui_chunk = value >> num_whole_64bit_chunks * 64
                stream.write_int(ui_chunk, width_first_chunk)

            for idx in range (1, num_whole_64bit_chunks + 1):
                ui_chunk = value >> (num_whole_64bit_chunks - 1) * 64 & 0xFFFFFFFFFFFFFFFF
                stream.write_word(ui_chunk)

    @staticmethod
    def encode_string(stream: encodingstream, value: str, **kwargs) -> None:
        if not isinstance(value, str):
            try:
                value = str(value)
            except Exception as exc:
                raise TypeError("65201: The value class containing the value to be encoded does not match the type specified in the schema!") from exc

        width_idx = kwargs.get("width_index_aligned") if stream.aligned else kwargs.get("width_index_unaligned")
        width_length = kwargs.get("width_length_aligned") if stream.aligned else kwargs.get("width_length_unaligned")
        width_code_point = kwargs.get("width_alphabet_aligned") if stream.aligned else kwargs.get("width_alphabet_unaligned")
        align_length = kwargs.get("align_length") if stream.aligned else False

        use_code_points = True if width_code_point is not None else False
        use_alphabet = True if width_idx is not None else False

        code_point_array = None
        byte_array = None

        if use_code_points:
            if value is None:
                raise ValueError("63901: The 'plain string' is missing from the string value!")
            code_point_array = stream.get_code_points(value)

            if width_code_point < 32:
                for c_point in code_point_array:
                    if c_point >= 1 << width_code_point:
                        raise ValueError("77302: The string value contains one or more invalid characters!")
        else:
            if kwargs.get("is_utf8") is True:
                if value is None:
                    raise ValueError("63901: The 'plain string' is missing from the string value!")
                byte_array = value.encode('utf-8')
            else:
                if value is None:
                    raise ValueError("63901: The 'plain string' is missing from the string value!")
                byte_array = value.encode('ascii')

                if byte_array is None:
                    raise ValueError("63903: Both the 'plain string' and the 'plain octets' are missing from the string value!")

        min_root_size = kwargs.get("minimum_root_size")
        max_root_size = kwargs.get("maximum_root_size")

        length = len(code_point_array) if use_code_points else len(byte_array)
        extend_size = True if length < min_root_size or max_root_size is not None and length > max_root_size else False

        if kwargs.get("has_extensible_size"):
            stream.write_bit(extend_size)
        if (extend_size and not kwargs.get("has_extensible_size")):
            raise ValueError("63902: The length (number of characters) of the string value is outside the encodable range!")

        len_remainder = length
        loc_fragment = 0
        width_item = 0

        if use_code_points:
            width_item = width_idx if use_alphabet else width_code_point
        else:
            width_item = 8

        if (width_length is None or extend_size):
            while len_remainder >= 16384:
                idx = 0
                for idx in range(4, -maxsize, -1):
                    if len_remainder >= 16384 * idx:
                        break
                len_fragment = 16384 * idx

                if stream.aligned:
                    stream.allign()

                stream.write_int(0xC0 + idx, 8)
                stream.encode_fragment(code_point_array, byte_array, loc_fragment, len_fragment, width_item, use_code_points, use_alphabet, kwargs.get("alphabet"))

                len_remainder -= len_fragment
                loc_fragment += len_fragment

            if stream.aligned:
                stream.allign()

            if len_remainder >= 128:
                stream.write_int(0x8000 + len_remainder, 16)
            else:
                stream.write_int(len_remainder, 8)

            stream.encode_fragment(code_point_array, byte_array, loc_fragment, len_remainder, width_item, use_code_points, use_alphabet, kwargs.get("alphabet"))
        else:
            if align_length:
                stream.allign()

            if (width_length is not None and width_length > 0):
                stream.write_int(length - min_root_size, width_length)

            if (stream.aligned and len_remainder > 0):
                if (width_length > 0 and max_root_size is not None and max_root_size * width_item > 15 or min_root_size * width_item > 16):
                    stream.allign()

            stream.encode_fragment(code_point_array, byte_array, 0, len_remainder, width_item, use_code_points, use_alphabet, kwargs.get("alphabet"))

    @staticmethod
    def encode_real(stream: encodingstream, value: Union[Any, dict], **_) -> None:
        if (not isinstance(value, int) and not isinstance(value, float) and not isinstance(value, Decimal) and not isinstance(value, str) and not isinstance(value, dict)):
            raise TypeError("65201: The value class containing the value to be encoded does not match the type specified in the schema!")

        byte_array = shared.encode_real(value)
        stream.write_octets_with_indefinite_length(byte_array)

    @staticmethod
    def encode_enum(stream: encodingstream, value: int, **kwargs) -> None:
        width_idx = kwargs.get("width_index_aligned") if stream.aligned else kwargs.get("width_index_unaligned")
        width_length = kwargs.get("width_length_aligned") if stream.aligned else None
        align_idx = kwargs.get("align_index") if stream.aligned else False
        is_extension = kwargs.get("is_extension")

        if (is_extension and value <= 63):
            stream.write_int(value, 6)
        elif (width_idx is None or is_extension):
            length = int((stream.width_of_range(0, value) + 8 - 1) / 8)
            byte_array = bytearray(length)

            for loc in range(length - 1, -1, -1):
                byte_array[loc] = (value & 0xFF)
                value >>= 8
            if width_length is None or is_extension:
                stream.write_octets_with_indefinite_length(byte_array)
            else:
                if width_length is not None and width_length > 0:
                    stream.write_int(length - 1, width_length)
                stream.allign()
                stream.write_octets(byte_array, 0, -1)
        else:
            if align_idx:
                stream.allign()
            if (width_idx is not None and width_idx > 0):
                stream.write_int(value, width_idx)

    @staticmethod
    def encode_boolean(stream: encodingstream, value: bool, **_) -> None:
        if not isinstance(value, bool):
            try:
                value = bool(value)
            except Exception as exc:
                raise TypeError("65201: The value class containing the value to be encoded does not match the type specified in the schema!") from exc

        stream.write_bit(value)

    @staticmethod
    def encode_null(stream: encodingstream, value: None, **_) -> None:
        if value is not None:
            raise TypeError("65201: The value class containing the value to be encoded does not match the type specified in the schema!")

    @staticmethod
    def encode_absolute_oid(stream: encodingstream, value: list, **_) -> None:
        if isinstance(value, str):
            value = value.replace('.', ' ').split()

        if isinstance(value, list):
            for idx, val in enumerate(value):
                if not isinstance(val, int):
                    try:
                        oid_val = int(val)
                        value[idx] = oid_val
                    except Exception as exc:
                        raise TypeError("65201: The value class containing the value to be encoded does not match the type specified in the schema!") from exc
        else:
            raise TypeError("65201: The value class containing the value to be encoded does not match the type specified in the schema!")

        byte_array = shared.encode_absolute_oid(value)
        stream.write_octets_with_indefinite_length(byte_array)

    @staticmethod
    def encode_relative_oid(stream: encodingstream, value: Union[str, list], **_) -> None:
        if isinstance(value, str):
            value = value.replace('.', ' ').split()

        if isinstance(value, list):
            for idx, val in enumerate(value):
                if not isinstance(val, int):
                    try:
                        oid_val = int(val)
                        value[idx] = oid_val
                    except Exception as exc:
                        raise TypeError("65201: The value class containing the value to be encoded does not match the type specified in the schema!") from exc
        else:
            raise TypeError("65201: The value class containing the value to be encoded does not match the type specified in the schema!")

        byte_array = shared.encode_relative_oid(value)
        stream.write_octets_with_indefinite_length(byte_array)

    @staticmethod
    def encode_oid_iri(stream: encodingstream, value: str, **_) -> None:
        if not isinstance(value, str):
            try:
                value = str(value)
            except Exception as exc:
                raise TypeError("65201: The value class containing the value to be encoded does not match the type specified in the schema!") from exc

        byte_array = shared.encode_oid_iri(value)
        stream.write_octets_with_indefinite_length(byte_array)

    @staticmethod
    def encode_generalized_time(stream: encodingstream, value: Any, **_) -> None:
        byte_array = shared.encode_time(value, False)

        if stream.aligned:
            stream.write_octets_with_indefinite_length(byte_array)
        else:
            stream.write_septets_with_indefinite_length(byte_array)

    @staticmethod
    def encode_utc_time(stream: encodingstream, value: Any, **_) -> None:
        byte_array = shared.encode_time(value, True)

        if stream.aligned:
            stream.write_octets_with_indefinite_length(byte_array)
        else:
            stream.write_septets_with_indefinite_length(byte_array)

    @staticmethod
    def encode_bit_string(stream: encodingstream, length: int, byte_array: bytearray, **kwargs) -> None:
        width_length = kwargs.get("width_length_aligned") if stream.aligned else kwargs.get("width_length_unaligned")
        align_length = kwargs.get("align_length") if stream.aligned else False

        min_root_size = kwargs.get("minimum_root_size")
        max_root_size = kwargs.get("maximum_root_size")

        if length is None:
            if max_root_size is not None and min_root_size == max_root_size:
                length = min_root_size
            else:
                length = len(byte_array) * 8

        if kwargs.get("has_named_bits"):
            if length < min_root_size:
                length = min_root_size

        extend_size = True if length < min_root_size or max_root_size is not None and length > max_root_size else False

        if kwargs.get("has_extensible_size"):
            stream.write_bit(extend_size)

        if (extend_size and kwargs.get("has_extensible_size") is False):
            raise ValueError("62107: The length (number of bits) of the bit string value is outside the encodable range!")

        if len(byte_array) == 0: 
            bit_list = shared.bit_array_from_bytes(length, byte_array)
            byte_array = shared.bit_array_to_bytes(bit_list)

        if (width_length is None or extend_size):
            stream.write_bits_with_indefinite_length(length, byte_array)
        else:
            if align_length:
                stream.allign()

            if (width_length is not None and width_length > 0):
                stream.write_int(length - min_root_size, width_length)

            if (stream.aligned and length > 0):
                if (width_length is not None and width_length > 0 or min_root_size > 16):
                    stream.allign()

            bit_list = shared.bit_array_from_bytes(length, byte_array)
            stream.write_bits(bit_list)

    @staticmethod
    def encode_octet_string(stream: encodingstream, byte_array: bytearray, **kwargs) -> None:
        width_length = kwargs.get("width_length_aligned") if stream.aligned else kwargs.get("width_length_unaligned")
        align_length = kwargs.get("align_length") if stream.aligned else False

        length = len(byte_array)
        min_root_size = kwargs.get("minimum_root_size")
        max_root_size = kwargs.get("maximum_root_size")
        extend_size = True if  length < min_root_size or max_root_size is not None and length > max_root_size else False

        if kwargs.get("has_extensible_size"):
            stream.write_bit(extend_size)

        if (extend_size and kwargs.get("has_extensible_size") is False):
            raise ValueError("63307: The length (number of octets) of the octet string value is outside the encodable range!")

        if (width_length is None or extend_size):
            stream.write_octets_with_indefinite_length(byte_array)
        elif (width_length is not None and width_length == 0):
            if (stream.aligned and min_root_size > 2):
                stream.allign()
            stream.write_octets(byte_array)
        else:
            if align_length:
                stream.allign()
            stream.write_int(length - min_root_size, width_length)

            if (stream.aligned and len(byte_array) > 0):
                stream.allign()
            stream.write_octets(byte_array)

    @staticmethod
    def encode_sequence_of(stream: encodingstream, encoding_rule: str, value: list, value_tracker: dict, encode_components: callable, **kwargs) -> Tuple[int, int]:
        width_length = kwargs.get("width_length_aligned") if stream.aligned else kwargs.get("width_length_unaligned")
        align_length = kwargs.get("align_length") if stream.aligned else False

        min_root_size = kwargs.get("minimum_root_size")
        max_root_size = kwargs.get("maximum_root_size")

        length = len(value)
        extend_size = True if length < min_root_size or max_root_size is not None and length > max_root_size else False

        if kwargs.get("has_extensible_size"):
            stream.write_bit(extend_size)

        if (extend_size and kwargs.get("has_extensible_size") is False):
            raise ValueError("63702: The length (number of items) of the sequence-of or set-of value is outside the encodable range!")

        len_remainder = length
        loc_fragment = 0

        if (width_length is None or extend_size):
            while len_remainder >= 16384:
                for idx in range(4, -1, -1):
                    if len_remainder >= 16384 * idx:
                        break

                len_fragment = 16384 * idx

                if stream.aligned:
                    stream.allign()

                stream.write_int(0xC0 + idx, 8)

                encode_components(encoding_rule, stream, value, value_tracker, loc_fragment, loc_fragment + len_fragment, kwargs.get('encoded_items'))
                len_remainder -= len_fragment
                loc_fragment += len_fragment

            if stream.aligned:
                stream.allign()

            if len_remainder >= 128:
                stream.write_int(0x8000 + len_remainder, 16)
            else:
                stream.write_int(len_remainder, 8)
        else:
            if align_length:
                stream.allign()
            if (width_length is not None and width_length > 0):
                stream.write_int(length - min_root_size, width_length)

        return (loc_fragment, loc_fragment + len_remainder)

    @staticmethod
    def encode_choice_preamble(stream: encodingstream, is_extension: bool, idx: int, **kwargs) -> None:
        width_idx = kwargs.get("width_index_aligned") if stream.aligned else kwargs.get("width_index_unaligned")
        width_length = kwargs.get("width_length_aligned") if stream.aligned else None
        align_idx = kwargs.get("align_index") if stream.aligned else False

        if (is_extension and idx <= 63):
            stream.write_int(idx, 6)
        elif (width_idx is None or is_extension):
            length = int((stream.width_of_range(0, idx) + 8 - 1) / 8)
            hex_value = bytearray(length)

            for loc in range(length - 1, -1, -1):
                hex_value[loc] = (idx & 0xFF)
                idx >>= 8

            if (width_length is None or is_extension):
                stream.write_octets_with_indefinite_length(hex_value)
            else:
                if (width_length is not None and width_length > 0):
                    stream.write_int(length - 1, width_length)

                stream.allign()
                stream.write_octets(hex_value)
        else:
            if align_idx:
                stream.allign()

            if (width_idx is not None and width_idx > 0):
                stream.write_int(idx, width_idx)

from decimal import Decimal


class shared:
    @staticmethod
    def decode_absolute_oid(byte_array: bytearray) -> list:
        oids = []
        length = len(byte_array)
        num = 0

        if length < 1:
            raise ValueError("61903: The encoding of the object identifier value is empty!")

        for idx in range(0, length):
            curr_byte = byte_array[idx]
            num <<= 7
            num |= curr_byte & 0x7F

            if (curr_byte & 0x80) == 0:
                if len(oids) == 0:
                    idx0 = 2 if num >= 80 else int(num / 40)
                    oids.append(idx0)
                    oids.append(num - idx0 * 40)
                else:
                    oids.append(num)
                num = 0

        if num != 0:
            raise ValueError("61904: The encoding of the object identifier value is not well-formed!")

        return oids

    @staticmethod
    def decode_relative_oid(byte_array: bytearray) -> list:
        num_list = []
        length = len(byte_array)

        if length < 1:
            raise ValueError("63603: The encoding of the relative OID value is empty!")

        num = 0

        for idx in range(length):
            by0 = byte_array[idx]
            num <<= 7
            num |= by0 & 0x7F

            if by0 & 0x80 == 0:
                num_list.append(num)
                num = 0

        if num != 0:
            raise ValueError("63604: The encoding of the relative OID value is not well-formed!")

        return num_list

    @staticmethod
    def decode_oid_iri(byte_array: bytearray) -> str:
        return byte_array.decode('utf-8')

    @staticmethod
    def decode_real(byte_array: bytearray) -> Union[str, Decimal, int, dict]:
        length = len(byte_array)

        if length == 0:
            return '0'

        if length == 1:
            if byte_array[0] == 0x40:
                return 'INF'
            elif byte_array[0] == 0x41:
                return '-INF'
            elif byte_array[0] == 0x42:
                return 'NaN'
            elif byte_array[0] == 0x43:
                return '-0'
            else:
                Decimal(0)

        first_octet = byte_array[0]

        if first_octet & 0x80 != 0:
            is_negative = (first_octet & 0x40) != 0
            scaling = (first_octet & 0x0C) >> 2
            base = (first_octet & 0x30) >> 4
            exponent = first_octet & 0x03
            len_exponent = 0
            loc_exponent = 1

            if exponent <= 2:
                len_exponent = exponent + 1
            else:
                len_exponent =  byte_array[1]
                loc_exponent = loc_exponent + 1

            if len_exponent == 0:
                raise ValueError("63508: The exponent of the real value in the encoded data is empty!")
            if loc_exponent + len_exponent > length:
                raise ValueError("63509: The exponent of the real value in the encoded data is incomplete!")

            exponent_array = bytearray(len_exponent)
            loc_src = loc_exponent

            for idx in range(len_exponent - 1, -1, -1):
                exponent_array[idx] = byte_array[loc_src]
                loc_src += 1

            exponent = int.from_bytes(exponent_array, byteorder=byteorder, signed=True)

            if base == 1:
                exponent = exponent << 3
            elif base == 2:
                exponent = exponent << 4
            elif base == 3:
                raise ValueError("63507: The encoding of the real value in the encoded data is not well-formed!")

            loc_mantissa = loc_src
            len_mantissa = length - loc_mantissa
            mantissa = 0

            if len_mantissa != 0:
                needs_leading_zeros = byte_array[loc_mantissa] >= 0x80
                if needs_leading_zeros:
                    loc_mantissa -= 1
                    len_mantissa += 1

                mantissa_array = bytearray(len_mantissa)
                loc_src = loc_mantissa

                for idx in range(len_mantissa - 1, -1, -1):
                    mantissa_array[idx] = byte_array[loc_src]
                    loc_src += 1

                if needs_leading_zeros:
                    mantissa_array[len_mantissa - 1] = 0

                mantissa = int.from_bytes(mantissa_array, byteorder=byteorder, signed=True) << scaling
                if is_negative:
                    mantissa = -mantissa

            if mantissa == 0:
                return Decimal(0)

            return {
                'mantissa': mantissa,
                'base': 2, 
                'exponent': exponent
            }
        else:
            is_negative = True if byte_array[1] == ord('-') else False
            loc_start = 2 if is_negative else 1

            ascii_real = byte_array[loc_start:].decode('ascii')
            value = Decimal(ascii_real)

            if is_negative:
                value = -value

            if ('.' not in str(value) and 'e' not in str(value)):
                return int(value)

            return value

    @staticmethod
    def get_base2_real(dec_val: Decimal, base10_value: int) -> Union[str, dict]:
        is_negative = True if base10_value < 0 else False

        if str(dec_val) == '-0.0':
            return '-0'
        elif str(dec_val) == '0.0':
            return 0
        elif isnan(dec_val):
            return 'NaN'
        elif dec_val == Decimal('inf'):
            return 'INF'
        elif dec_val == Decimal('-inf'):
            return '-INF'
        else:
            ui_exponent = (base10_value >> 52) & 0x7FF
            ui_mantissa = base10_value & 0xF_FFFF_FFFF_FFFF
            idx_exponent = None

            if ui_exponent == 0:
                idx_exponent = ui_exponent - 1023 - 52 + 1
            else:
                idx_exponent = ui_exponent - 1023 - 52
                ui_mantissa += 0x10_0000_0000_0000

            if ui_mantissa != 0:
                while (ui_mantissa & 0xFFFF) == 0:
                    ui_mantissa >>= 16
                    idx_exponent += 16

                while (ui_mantissa & 0xF) == 0:
                    ui_mantissa >>= 4
                    idx_exponent += 4

                while (ui_mantissa & 1) == 0:
                    ui_mantissa >>= 1
                    idx_exponent += 1

            return {
                'mantissa': -ui_mantissa if is_negative else ui_mantissa,
                'base': 2, 
                'exponent': idx_exponent
            }

    @staticmethod
    def get_real_value(value: Union[str, int, dict]) -> Union[int, Decimal]:
        if isinstance(value, int):
            return Decimal(value)

        if isinstance(value, str):
            if value == '-INF':
                return Decimal('-inf')
            elif value == 'INF':
                return Decimal('inf')
            elif value == 'NaN':
                return Decimal('nan')
            elif value == '-0':
                return Decimal(-0.0)
            elif value == '0':
                return Decimal(0.0)
            else:
                if 'E' in value:
                    mantissa, exponent = value.split('E')
                    value = shared.base2_real_from_base10_real(int(mantissa), int(exponent))

        if (isinstance(value, dict) and 'base' in value and value['base'] == 2):
            mantissa = value['mantissa']
            exponent = value['exponent']

            exponent_max = 1023 - 52
            exponent_min = -1023 - 52 + 1
            cnt_bits = 0
            is_negative = True if mantissa < 0 else False

            num = abs(mantissa)

            if num > 0:
                while num >= 0x80000000:
                    num >>= 32
                    cnt_bits += 32
                while num >= 0x80:
                    num >>= 8
                    cnt_bits += 8
                while num >= 1:
                    num >>= 1
                    cnt_bits += 1
            elif num < 0:
                while num < -0xFFFFFFFF:
                    num >>= 32
                    cnt_bits += 32
                while num < -0xFF:
                    num >>= 8
                    cnt_bits += 8
                while num < 1:
                    num >>= 1
                    cnt_bits += 1

            if cnt_bits < 53:
                mantissa = abs(mantissa) << (53 - cnt_bits)
                exponent = exponent - (53 - cnt_bits)
            elif cnt_bits > 53:
                mantissa = abs(mantissa) >> (cnt_bits - 53)
                exponent = exponent + (cnt_bits - 53)
            else:
                mantissa = abs(mantissa)

            if (mantissa < 0x10_0000_0000_0000 or mantissa > 0x1F_FFFF_FFFF_FFFF):
                raise ValueError("Invalid Usage exception!")

            ui_mantissa = mantissa + 2**32 if mantissa < 0 else mantissa

            if exponent > exponent_max:
                raise ValueError("Invalid Usage exception!")

            if exponent < exponent_min:
                raise ValueError("Invalid Usage exception!")

            ui_exponent = exponent - exponent_min + 1
            ui_exponent = ui_exponent + 2**32 if ui_exponent < 0 else ui_exponent
            uid = ui_exponent << 52 | ui_mantissa & 0xF_FFFF_FFFF_FFFF

            if is_negative:
                uid |= 0x8000_0000_0000_0000

            return uid

    @staticmethod
    def base2_real_from_base10_real(base10_mantissa: int, base10_exponent: int) -> dict:
        log_base2 = base10_exponent / log10(2)
        floor_log = floor(log_base2)
        factor = pow(2, log_base2 - floor_log)
        base2_mantissa = base10_mantissa * factor
        base2_exponent = floor_log

        is_negative = True if base2_mantissa < 0 else False

        if is_negative:
            base2_mantissa = -base2_mantissa

        epsilon = 1E-12
        while base2_mantissa >= 2:
            base2_mantissa /= 2
            base2_exponent += 1

        while 2 * base2_mantissa <= 999_999_999_999_999:
            int_part = trunc(base2_mantissa)
            fract_part = base2_mantissa - int_part

            if fract_part < epsilon:
                base2_mantissa = int_part
                break

            if fract_part > 1 - epsilon:
                base2_mantissa = int_part + 1
                break

            base2_mantissa *= 2
            base2_exponent -= 1
            epsilon *= 2

        if is_negative:
            base2_mantissa = -base2_mantissa

        return {
            'mantissa': base2_mantissa, 
            'base': 2,
            'exponent' : base2_exponent
        }

    @staticmethod
    def decode_time(byte_array: bytearray, utc_time: bool) -> str:
        return shared.fix_tail(shared.bytes_to_utf8string(byte_array), utc_time)

    @staticmethod
    def fix_tail(time_val: str, utc_time: bool) -> str:
        if '+' in time_val:
            idx = time_val.index('+')
            tail_len = len(time_val) - (idx + 1)
            while tail_len < 4:
                time_val += '0'
                tail_len += 1
        elif '-' in time_val:
            idx = time_val.index('-')
            tail_len = len(time_val) - (idx + 1)
            while tail_len < 4:
                time_val += '0'
                tail_len += 1
        return time_val

    @staticmethod
    def to_bit_list(length: int, byte_array: bytearray) -> list:
        bit_str = ''.join([format(num, "08b") for num in byte_array])
        bits = [True if bit == "1" else False for bit in bit_str[0:length]]
        return bits

    @staticmethod
    def encode_absolute_oid(oids: list) -> bytearray:
        num_components = len(oids)
        if num_components < 2:
            raise ValueError("61902: The object identifier value has too few components!")

        num0 = oids[0]
        num1 = oids[1]

        if (num0 < 0 or num0 > 2 or num1 < 0 or num0 < 2 and num1 >= 40):
            raise ValueError("61901: The object identifier value contains an invalid component!")

        length = 0
        for idx in range(2, num_components + 1):
            num = num0 * 40 + num1 if idx == 2 else oids[idx - 1]

            if num < 0:
                raise ValueError("61901: The object identifier value contains an invalid component!")

            length += 1
            num >>= 7

            while num != 0:
                length +=1
                num >>= 7

        byte_array = bytearray(length)
        loc_comp = 0

        for idx in range(2, num_components + 1):
            num = num0 * 40 + num1 if idx == 2 else oids[idx - 1]
            num2 = num
            len_comp = 0

            len_comp += 1
            num2 >>= 7

            while num2 != 0:
                len_comp += 1
                num2 >>= 7

            loc = loc_comp + len_comp - 1
            byte_plus = 0x00
            loc_comp = loc + 1

            byte_array[loc] = num & 0x7F | byte_plus
            num >>= 7
            loc -= 1
            byte_plus = 0x80

            while num != 0:
                byte_array[loc] = num & 0x7F | byte_plus
                num >>= 7
                loc -= 1
                byte_plus = 0x80

        return byte_array

    @staticmethod
    def encode_relative_oid(oids: list) -> bytearray:
        num_oids = len(oids)

        if num_oids < 1:
            raise ValueError("63602: The relative OID value does not have any components!")

        length = 0
        for oid in oids:
            num = oid

            if num < 0:
                raise ValueError("63601: The relative OID value contains an invalid component!")

            length += 1
            num >>= 7

            while num != 0:
                length += 1
                num >>= 7

        byte_array = bytearray(length)
        loc_comp = 0

        for oid in oids:
            num = oid
            num2 = num
            len_comp = 0

            len_comp += 1
            num2 >>= 7

            while num2 != 0:
                len_comp += 1
                num2 >>= 7

            loc = loc_comp + len_comp - 1
            by_more = 0x00
            loc_comp = loc + 1

            byte_array[loc] = num & 0x7F | by_more
            num >>= 7
            loc -= 1
            by_more = 0x80

            while num != 0:
                byte_array[loc] = num & 0x7F | by_more
                num >>= 7
                loc -= 1
                by_more = 0x80

        return byte_array

    @staticmethod
    def encode_oid_iri(value: str) -> bytearray:
        return bytearray(value.encode('utf-8'))

    @staticmethod
    def encode_real(value: Union[str, Decimal, float, int, dict]) -> bytearray:
        if (isinstance(value, dict) and 'base10Value' in value):
            try:
                value = Decimal(value['base10Value'])
            except: # noqa: E722
               raise TypeError("65201: The value class containing the value to be encoded does not match the type specified in the schema!")

        if isinstance(value, float):
            value = Decimal(value)

        if isinstance(value, str):
            if value == 'INF':
                return bytearray([0x40])
            elif value == '-INF':
                return bytearray([0x41])
            elif value == 'NaN':
                return bytearray([0x42])
            elif (value == '-0' or value == '-0.0'):
                return bytearray([0x43])
            elif (value == '0' or value == '0.0'):
                return bytearray()
            else:
                try:
                    decimal_value = Decimal(value)
                    decimal_tuple = decimal_value.as_tuple()
                    exponent = decimal_tuple.exponent
                    mantissa_digits = decimal_tuple.digits
                    mantissa = int(''.join(map(str, mantissa_digits)))
                    value = shared.base2_real_from_base10_real(mantissa, exponent)
                except:  # noqa: E722
                    raise TypeError("65201: The value class containing the value to be encoded does not match the type specified in the schema!")

        if isinstance(value, Decimal):
            if value == Decimal('inf'):
                return bytearray([0x40])
            elif value == Decimal('-inf'):
                return bytearray([0x41])
            elif isnan(value):
                return bytearray([0x42])
            elif (value == -0.0 and value < 0):
                return bytearray([0x43])
            elif value == Decimal(0.0):
                return bytearray()
            else:
                decimal_tuple = value.as_tuple()
                exponent = decimal_tuple.exponent
                mantissa_digits = decimal_tuple.digits
                mantissa = int(''.join(map(str, mantissa_digits)))

                if (value < 0 and mantissa > 0):
                    mantissa = -mantissa

                value = {
                    'base': 10,
                    'mantissa': mantissa,
                    'exponent': exponent
                }

        if isinstance(value, int):
            value = {
                'base': 10,
                'mantissa': value,
                'exponent': 0
            }

        if isinstance(value, dict):
            if 'mantissa' not in value:
                raise ValueError("63502: The mantissa is missing from the real value!")
            if 'base' not in value:
                raise ValueError("63503: The base is missing from the real value!")
            if 'exponent' not in value:
                raise ValueError("63504: The exponent is missing from the real value!")

            base = int(value['base'])
            mantissa = int(value['mantissa'])
            exponent = int(value['exponent'])

            if base == 2:
                if mantissa != 0:
                    while (mantissa & 1) == 0:
                        mantissa >>= 1
                        exponent += 1

                by0 = 0x80
                if mantissa < 0:
                    by0 |= 0x40
                    mantissa = -mantissa

                num_bytes = (8 + (exponent + (exponent < 0)).bit_length()) // 8
                exponent_arr = bytearray(exponent.to_bytes(num_bytes, byteorder=byteorder, signed=True))
                exponent_arr.reverse()
                len_exponent = len(exponent_arr)
                len_total = 1

                if len_exponent >= 4:
                    by0 |= 0x03
                    len_total += 1
                else:
                    by0 |= len_exponent - 1

                len_total += len_exponent

                num_bytes = (8 + (mantissa + (mantissa < 0)).bit_length()) // 8
                mantissa_arr = bytearray(mantissa.to_bytes(num_bytes, byteorder=byteorder, signed=True))
                mantissa_arr.reverse()
                len_mantissa = len(mantissa_arr)
                has_leading_zeros = True if len_mantissa > 1 and mantissa_arr[0] == 0 else False

                if has_leading_zeros:
                    len_total += len_mantissa -1
                else:
                    len_total += len_mantissa

                byte_array = bytearray(len_total)
                byte_array[0] = by0

                loc_exponent = 1
                if len_exponent >= 4:
                    if len_exponent > 255:
                        raise ValueError("63505: The exponent inside the real value is not supported (over 2040 bits)!")
                    byte_array[1] = len_exponent
                    loc_exponent += 1

                loc_mantissa = loc_exponent + len_exponent

                if has_leading_zeros:
                    loc_mantissa -= 1

                byte_array[loc_mantissa:loc_mantissa + len(mantissa_arr)] = mantissa_arr
                byte_array[loc_exponent:loc_exponent + len(exponent_arr)] = exponent_arr
                return byte_array
            elif base == 10:
                if mantissa != 0:
                    while (mantissa % 10) == 0:
                        mantissa //= 10
                        exponent = exponent + 1
                by0 = 0x03

                mantissa_arr = bytearray(str(mantissa).encode('ascii'))
                exponent_arr = "+0".encode('ascii')
                if exponent != 0:
                    exponent_arr = str(exponent).encode('ascii')

                len_mantissa = len(mantissa_arr)
                len_exponent = len(exponent_arr)
                len_total = 1 + len_mantissa + 1 + 1 + len_exponent

                byte_array = bytearray(len_total)
                byte_array[0] = by0

                byte_array[1: 1 + len(mantissa_arr)] = mantissa_arr
                byte_array[1 + len_mantissa] = ord('.')
                byte_array[1 + len_mantissa + 1] = ord('E')
                byte_array[1 + len_mantissa + 2: 1 + len_mantissa + 2 + len(exponent_arr)] = bytearray(exponent_arr)
                return byte_array
            else:
                raise ValueError("63506: The base inside the real value is invalid!")

    @staticmethod
    def encode_time(timevalue: Any, is_utc_time: bool = False) -> bytearray:
        timeobj = None
        strtime = ''

        if isinstance(timevalue, str):
            strtime = timevalue
            if not is_utc_time:
                strtime = shared.remove_trailing_zeroes(timevalue)
        elif isinstance(timevalue, datetime):
            timeobj = timevalue
            timeformat = shared.get_format_from_time_object(timeobj, is_utc_time)
            strtime = timeobj.strftime(timeformat)
            strtime = shared.remove_trailing_zeros(strtime)

            if timeobj.tzinfo == timezone.utc:
                if timeobj.utcoffset().total_seconds() == 0:
                    strtime = strtime + 'Z'
        else:
            raise TypeError("65201: The value class containing the value to be encoded does not match the type specified in the schema!")

        return shared.bytes_from_utf8string(strtime)

    @staticmethod
    def remove_trailing_zeroes(time_val: str) -> str:
        position = None
        if '-' in time_val:
            position = time_val.find('-')
        elif '+' in time_val:
            position = time_val.find('+')
        if position is not None:
            position = position + 2
            chars = list(time_val)
            rng = len(chars) - 1 - position
            for i in range(len(chars) - 1, position, -1):
                if rng % 2 != 0:
                    chars.pop()
                    rng = rng - 1
                    continue
                if chars[i] == '0':
                    if (i > 0 and chars[i - 1] == '0'):
                        chars.pop()
                        rng = rng - 1
                else:
                    break
            return ''.join(chars)
        return time_val

    @staticmethod
    def bytes_to_utf8string(byte_array: bytearray) -> str:
        return byte_array.decode("utf-8")

    @staticmethod
    def bytes_from_utf8string(value: str) -> bytearray:
        buffer = bytearray()

        if not isinstance(value, str):
            value = str(value)

        buffer.extend(value.encode('utf-8'))
        return buffer

    @staticmethod
    def remove_trailing_zeros(timevalue: str) -> str:
        if '.' not in timevalue:
            return timevalue

        start = 0
        stop = len(timevalue) - 1

        if '+' in timevalue:
            stop = timevalue.index('+') - 1
        elif '-' in timevalue:
            stop = timevalue.index('-') - 1

        start = stop

        while timevalue[start] == '0':
            start = start -1

        if timevalue[start] == '.':
            start = start - 1

        if '+'in timevalue or '-' in timevalue:
            return timevalue[0: start + 1] + timevalue[stop::]

        return timevalue[0: start + 1]

    @staticmethod
    def get_format_from_time_object(timeobj: datetime, utctime: bool = False) -> str:
        timeformat = ''

        if timeobj.year is not None:
            if not utctime:
                timeformat += "%Y"
            else:
                timeformat += "%y"
        if timeobj.month is not None:
            timeformat += "%m"
        if timeobj.day is not None:
            timeformat += "%d"
        if timeobj.hour is not None:
            timeformat += "%H"
        if timeobj.minute is not None:
            timeformat += "%M"
        if timeobj.second is not None:
            timeformat += "%S"
        if timeobj.microsecond != 0:
            timeformat += ".%f"
        if timeobj.utcoffset() is not None and timeobj.utcoffset().total_seconds() != 0:
            timeformat += "%z"

        return timeformat

    @staticmethod
    def bit_array_from_bytes(length: int, byte_array: bytearray) -> list:
        if length == 0:
            return []

        bin_list = []
        bin_list = [format(idx, '08b') for idx in byte_array]

        length2 = len(byte_array) * 8
        while length > length2:
            bin_list.append('0')
            length2 +=1

        remainder = length % 8
        bin_list[-1] = bin_list[-1][0: length % 8] if remainder > 0 else bin_list[-1]
        bit_string = ''.join(bin_list)
        bit_array = []
        bit_array = [True if bs == '1' else False for bs in bit_string]
        return bit_array

    @staticmethod
    def bit_array_to_bytes(bit_list: list) -> bytearray:
        byte_array = bytearray()

        while len(bit_list) % 8 != 0:
            bit_list.append(False)

        num_bytes = len(bit_list) // 8

        for idx in range(num_bytes):
            byte_array.append(int(''.join(['1' if i else '0' for i in bit_list[idx * 8:idx * 8 + 8]]), 2))

        return byte_array

    @staticmethod
    def trim(bit_array: list) -> None:
        for idx in range(len(bit_array) - 1, -1, -1):
            if bit_array[idx] is False:
                bit_array.pop()
            else:
                break

class ValueTracker(dict):
    def __init__(self):
        self.__deferred_types = {}
        self.__deferred_context = False
        self.__stack = []
        self.__curent_depth = 0
    @property
    def deferred_context(self) -> bool:
        return self.__deferred_context
    @property 
    def depth(self) -> int:
        return self.__curent_depth
    @depth.setter
    def depth(self, level: int) -> None:
        while self.__curent_depth > level:
            self.__stack.pop()
            self.__decrement_level()
    def reset_context(self) -> None:
        self.__deferred_context = False
    def add_ancestor(self, value: Any, def_values: Any = None) -> None:
        self.__stack.append(value)

        if def_values is not None:
            for key, _ in def_values.items():
                if key not in value:
                    value[key] = def_values[key]

        self.__increment_level()
    def remove_ancestor(self) -> None:
        self.__stack.pop()
        self.__decrement_level()
    def get_ancestor(self, depth: int) -> Any:
        if depth is None:
            return None
        if self.__deferred_context:
            return self.__stack[self.__curent_depth - 1]
        if self.__curent_depth < depth:
            return None
        level = self.__curent_depth - depth
        return self.__stack[level]
    def get_discriminator(self, indetifier_paths: list) -> Any:
        discriminator = self.__stack[self.__curent_depth - 1]
        for identifier in indetifier_paths:
            if identifier in discriminator:
                discriminator = discriminator[identifier]
            else:
                discriminator = None
                break
        return discriminator
    def add_deferred(self, depth: int, deferred_data: dict) -> None:
        if depth is not None:
            level = self.__curent_depth - depth
            if level >= 0:
                if level not in self.__deferred_types:
                    self.__deferred_types[level] = []
                self.__deferred_types[level].append(deferred_data)
    def are_equivalent(self, value1: list, value2: list) -> bool:
        if value1 == value2:
            return True
        return False
    def are_def_eq(self, value1: Any, value2: Any, component: type) -> bool:
        component = component()
        if (isinstance(value1, dict) and isinstance(value2, dict) and hasattr(component, "_def_vals")):
            if len(value2) > len(value1):
                return False
            for key in value1:
                if key not in value2:
                    if (key not in component._def_vals or not self.are_def_eq(value1[key], component._def_vals[key], component._comp_types[key])):
                        return False
                elif not self.are_def_eq(value1[key], value2[key], component._comp_types[key]):
                    return False
            return True
        else:
            if isinstance(value1, Decimal):
                return str(value1) == str(value2)
            return value1 == value2

    def get_selected_entities(self, entities: Tuple[int, List[str]]) -> list:
        discriminators = []
        for segments in entities:
            (depth, paths) = segments
            discriminator = self.get_ancestor(depth)
            if discriminator is not None:
                for identifier in paths:
                    if identifier in discriminator:
                        discriminator = discriminator[identifier]
                if (discriminator is not None):
                    discriminators.append(discriminator)
        return discriminators

    def value_exists(self, dictionary, keys):
        nested_dict = dictionary
        for key in keys:
            try:
                nested_dict = nested_dict[key]
            except KeyError:
                return False
        return True

    def is_empty_buffer(self, buffer: bytearray) -> bool:
        if (buffer is None or len(buffer) == 0):
            return True
        elif (len(buffer) == 1 and 0x00 in buffer):
            return True
        return False

    def __increment_level(self):
        self.__curent_depth = self.__curent_depth + 1
    def __decrement_level(self):
        self.__curent_depth = self.__curent_depth - 1
    def __has_deferred(self):
        if self.__curent_depth - 1 in self.__deferred_types:
            return True
        return False
    def execute_deferred(self, value: dict) -> Any:
        if self.__has_deferred():
            stored_proc = self.__deferred_types[self.__curent_depth - 1]
            decoded_values = self.__execute_stored_procedures(stored_proc)
            self.__deferred_types.pop(self.__curent_depth - 1)
            if len(decoded_values) > 0:
                value = self.__fill(decoded_values, value)
        self.__deferred_context = False
        self.remove_ancestor()
        return value
    def __execute_stored_procedures(self, stored_proc: list) -> None:
        self.__deferred_context = True
        decoded_values = []
        for data in stored_proc:
            func = getattr(data['type'], 'decode')
            encoding_rule = data['encoding_rule']
            encoding = data['encoding']
            try:
                self.__deferred_context = True
                deferred_val = func(encoding_rule, encoding, self)
                decoded_values.append(deferred_val)
            except Exception as _exc: #pylint: disable=broad-except
                return decoded_values
        return decoded_values

    def __fill(self, decoded_values: list, value: Any) -> Any:
        if isinstance(value, dict):
            for key in value:
                if (len(decoded_values) > 0 and isinstance(value[key], dict) and '_unknown_encoding' in value[key]):
                    value[key] = decoded_values[0]
                    decoded_values.pop(0)
                value[key] = self.__fill(decoded_values, value[key])
        if isinstance(value, list):
            for idx, item in enumerate(value):
                if (len(decoded_values) > 0 and isinstance(item, dict) and '_unknown_encoding' in item):
                    value[idx] = decoded_values[0]
                    decoded_values.pop(0)
                self.__fill(decoded_values, value[idx])
        return value

