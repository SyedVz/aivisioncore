#************************************************************
#   Copyright (C) 2023 OSS Nokalva, Inc.  All rights reserved.
#************************************************************

#   THIS FILE IS PROPRIETARY MATERIAL OF OSS NOKALVA, INC.
#   AND MAY BE USED AND DISTRIBUTED ONLY BY DIRECT LICENSEES OF OSS NOKALVA, INC.
#   THIS COPYRIGHT STATEMENT MAY NOT BE REMOVED.

#   Python 3.7 or higher is required!

#   This file was generated for 'Syed Kamal' by 'https://asn1.io/ASN1-Python-Compiler/' at '5/1/2024 2:38:08 PM'

from io import BufferedReader, BytesIO
from typing import Union, Any

class DSRC:
    class MessageFrame:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.MessageFrame`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import MessageFrame
                    from private.osspy_der import ValueTracker
                    return MessageFrame.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'MessageFrame' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import MessageFrame
                    from private.osspy_per import ValueTracker
                    return MessageFrame.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'MessageFrame' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import MessageFrame
                    from private.osspy_oer import ValueTracker
                    return MessageFrame.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'MessageFrame' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.MessageFrame``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import MessageFrame
                    from private.osspy_der import ValueTracker
                    decval = MessageFrame.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'MessageFrame' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import MessageFrame
                    from private.osspy_per import ValueTracker
                    decval = MessageFrame.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'MessageFrame' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import MessageFrame
                    from private.osspy_oer import ValueTracker
                    decval = MessageFrame.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'MessageFrame' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.MessageFrame``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import MessageFrame
                    MessageFrame.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'MessageFrame' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import MessageFrame
                    MessageFrame.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'MessageFrame' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import MessageFrame
                    MessageFrame.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'MessageFrame' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class BasicSafetyMessage:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.BasicSafetyMessage`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import BasicSafetyMessage
                    from private.osspy_der import ValueTracker
                    return BasicSafetyMessage.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'BasicSafetyMessage' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import BasicSafetyMessage
                    from private.osspy_per import ValueTracker
                    return BasicSafetyMessage.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'BasicSafetyMessage' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import BasicSafetyMessage
                    from private.osspy_oer import ValueTracker
                    return BasicSafetyMessage.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'BasicSafetyMessage' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.BasicSafetyMessage``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import BasicSafetyMessage
                    from private.osspy_der import ValueTracker
                    decval = BasicSafetyMessage.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'BasicSafetyMessage' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import BasicSafetyMessage
                    from private.osspy_per import ValueTracker
                    decval = BasicSafetyMessage.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'BasicSafetyMessage' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import BasicSafetyMessage
                    from private.osspy_oer import ValueTracker
                    decval = BasicSafetyMessage.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'BasicSafetyMessage' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.BasicSafetyMessage``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import BasicSafetyMessage
                    BasicSafetyMessage.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'BasicSafetyMessage' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import BasicSafetyMessage
                    BasicSafetyMessage.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'BasicSafetyMessage' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import BasicSafetyMessage
                    BasicSafetyMessage.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'BasicSafetyMessage' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class PartII_Id:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.PartII_Id`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import PartII_Id
                    from private.osspy_der import ValueTracker
                    return PartII_Id.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'PartII_Id' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import PartII_Id
                    from private.osspy_per import ValueTracker
                    return PartII_Id.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'PartII_Id' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import PartII_Id
                    from private.osspy_oer import ValueTracker
                    return PartII_Id.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'PartII_Id' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.PartII_Id``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import PartII_Id
                    from private.osspy_der import ValueTracker
                    decval = PartII_Id.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'PartII_Id' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import PartII_Id
                    from private.osspy_per import ValueTracker
                    decval = PartII_Id.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'PartII_Id' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import PartII_Id
                    from private.osspy_oer import ValueTracker
                    decval = PartII_Id.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'PartII_Id' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.PartII_Id``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import PartII_Id
                    PartII_Id.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'PartII_Id' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import PartII_Id
                    PartII_Id.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'PartII_Id' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import PartII_Id
                    PartII_Id.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'PartII_Id' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class CommonSafetyRequest:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.CommonSafetyRequest`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import CommonSafetyRequest
                    from private.osspy_der import ValueTracker
                    return CommonSafetyRequest.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'CommonSafetyRequest' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import CommonSafetyRequest
                    from private.osspy_per import ValueTracker
                    return CommonSafetyRequest.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'CommonSafetyRequest' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import CommonSafetyRequest
                    from private.osspy_oer import ValueTracker
                    return CommonSafetyRequest.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'CommonSafetyRequest' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.CommonSafetyRequest``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import CommonSafetyRequest
                    from private.osspy_der import ValueTracker
                    decval = CommonSafetyRequest.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'CommonSafetyRequest' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import CommonSafetyRequest
                    from private.osspy_per import ValueTracker
                    decval = CommonSafetyRequest.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'CommonSafetyRequest' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import CommonSafetyRequest
                    from private.osspy_oer import ValueTracker
                    decval = CommonSafetyRequest.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'CommonSafetyRequest' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.CommonSafetyRequest``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import CommonSafetyRequest
                    CommonSafetyRequest.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'CommonSafetyRequest' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import CommonSafetyRequest
                    CommonSafetyRequest.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'CommonSafetyRequest' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import CommonSafetyRequest
                    CommonSafetyRequest.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'CommonSafetyRequest' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class EmergencyVehicleAlert:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.EmergencyVehicleAlert`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import EmergencyVehicleAlert
                    from private.osspy_der import ValueTracker
                    return EmergencyVehicleAlert.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'EmergencyVehicleAlert' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import EmergencyVehicleAlert
                    from private.osspy_per import ValueTracker
                    return EmergencyVehicleAlert.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'EmergencyVehicleAlert' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import EmergencyVehicleAlert
                    from private.osspy_oer import ValueTracker
                    return EmergencyVehicleAlert.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'EmergencyVehicleAlert' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.EmergencyVehicleAlert``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import EmergencyVehicleAlert
                    from private.osspy_der import ValueTracker
                    decval = EmergencyVehicleAlert.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'EmergencyVehicleAlert' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import EmergencyVehicleAlert
                    from private.osspy_per import ValueTracker
                    decval = EmergencyVehicleAlert.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'EmergencyVehicleAlert' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import EmergencyVehicleAlert
                    from private.osspy_oer import ValueTracker
                    decval = EmergencyVehicleAlert.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'EmergencyVehicleAlert' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.EmergencyVehicleAlert``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import EmergencyVehicleAlert
                    EmergencyVehicleAlert.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'EmergencyVehicleAlert' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import EmergencyVehicleAlert
                    EmergencyVehicleAlert.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'EmergencyVehicleAlert' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import EmergencyVehicleAlert
                    EmergencyVehicleAlert.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'EmergencyVehicleAlert' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class IntersectionCollision:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.IntersectionCollision`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import IntersectionCollision
                    from private.osspy_der import ValueTracker
                    return IntersectionCollision.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'IntersectionCollision' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import IntersectionCollision
                    from private.osspy_per import ValueTracker
                    return IntersectionCollision.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'IntersectionCollision' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import IntersectionCollision
                    from private.osspy_oer import ValueTracker
                    return IntersectionCollision.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'IntersectionCollision' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.IntersectionCollision``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import IntersectionCollision
                    from private.osspy_der import ValueTracker
                    decval = IntersectionCollision.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'IntersectionCollision' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import IntersectionCollision
                    from private.osspy_per import ValueTracker
                    decval = IntersectionCollision.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'IntersectionCollision' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import IntersectionCollision
                    from private.osspy_oer import ValueTracker
                    decval = IntersectionCollision.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'IntersectionCollision' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.IntersectionCollision``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import IntersectionCollision
                    IntersectionCollision.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'IntersectionCollision' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import IntersectionCollision
                    IntersectionCollision.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'IntersectionCollision' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import IntersectionCollision
                    IntersectionCollision.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'IntersectionCollision' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class MapData:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.MapData`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import MapData
                    from private.osspy_der import ValueTracker
                    return MapData.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'MapData' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import MapData
                    from private.osspy_per import ValueTracker
                    return MapData.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'MapData' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import MapData
                    from private.osspy_oer import ValueTracker
                    return MapData.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'MapData' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.MapData``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import MapData
                    from private.osspy_der import ValueTracker
                    decval = MapData.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'MapData' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import MapData
                    from private.osspy_per import ValueTracker
                    decval = MapData.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'MapData' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import MapData
                    from private.osspy_oer import ValueTracker
                    decval = MapData.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'MapData' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.MapData``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import MapData
                    MapData.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'MapData' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import MapData
                    MapData.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'MapData' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import MapData
                    MapData.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'MapData' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class NMEAcorrections:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.NMEAcorrections`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import NMEAcorrections
                    from private.osspy_der import ValueTracker
                    return NMEAcorrections.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'NMEAcorrections' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import NMEAcorrections
                    from private.osspy_per import ValueTracker
                    return NMEAcorrections.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'NMEAcorrections' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import NMEAcorrections
                    from private.osspy_oer import ValueTracker
                    return NMEAcorrections.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'NMEAcorrections' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.NMEAcorrections``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import NMEAcorrections
                    from private.osspy_der import ValueTracker
                    decval = NMEAcorrections.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'NMEAcorrections' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import NMEAcorrections
                    from private.osspy_per import ValueTracker
                    decval = NMEAcorrections.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'NMEAcorrections' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import NMEAcorrections
                    from private.osspy_oer import ValueTracker
                    decval = NMEAcorrections.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'NMEAcorrections' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.NMEAcorrections``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import NMEAcorrections
                    NMEAcorrections.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'NMEAcorrections' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import NMEAcorrections
                    NMEAcorrections.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'NMEAcorrections' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import NMEAcorrections
                    NMEAcorrections.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'NMEAcorrections' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class PersonalSafetyMessage:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.PersonalSafetyMessage`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import PersonalSafetyMessage
                    from private.osspy_der import ValueTracker
                    return PersonalSafetyMessage.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'PersonalSafetyMessage' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import PersonalSafetyMessage
                    from private.osspy_per import ValueTracker
                    return PersonalSafetyMessage.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'PersonalSafetyMessage' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import PersonalSafetyMessage
                    from private.osspy_oer import ValueTracker
                    return PersonalSafetyMessage.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'PersonalSafetyMessage' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.PersonalSafetyMessage``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import PersonalSafetyMessage
                    from private.osspy_der import ValueTracker
                    decval = PersonalSafetyMessage.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'PersonalSafetyMessage' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import PersonalSafetyMessage
                    from private.osspy_per import ValueTracker
                    decval = PersonalSafetyMessage.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'PersonalSafetyMessage' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import PersonalSafetyMessage
                    from private.osspy_oer import ValueTracker
                    decval = PersonalSafetyMessage.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'PersonalSafetyMessage' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.PersonalSafetyMessage``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import PersonalSafetyMessage
                    PersonalSafetyMessage.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'PersonalSafetyMessage' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import PersonalSafetyMessage
                    PersonalSafetyMessage.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'PersonalSafetyMessage' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import PersonalSafetyMessage
                    PersonalSafetyMessage.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'PersonalSafetyMessage' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class ProbeDataManagement:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.ProbeDataManagement`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import ProbeDataManagement
                    from private.osspy_der import ValueTracker
                    return ProbeDataManagement.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'ProbeDataManagement' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import ProbeDataManagement
                    from private.osspy_per import ValueTracker
                    return ProbeDataManagement.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'ProbeDataManagement' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import ProbeDataManagement
                    from private.osspy_oer import ValueTracker
                    return ProbeDataManagement.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'ProbeDataManagement' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.ProbeDataManagement``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import ProbeDataManagement
                    from private.osspy_der import ValueTracker
                    decval = ProbeDataManagement.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'ProbeDataManagement' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import ProbeDataManagement
                    from private.osspy_per import ValueTracker
                    decval = ProbeDataManagement.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'ProbeDataManagement' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import ProbeDataManagement
                    from private.osspy_oer import ValueTracker
                    decval = ProbeDataManagement.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'ProbeDataManagement' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.ProbeDataManagement``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import ProbeDataManagement
                    ProbeDataManagement.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'ProbeDataManagement' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import ProbeDataManagement
                    ProbeDataManagement.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'ProbeDataManagement' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import ProbeDataManagement
                    ProbeDataManagement.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'ProbeDataManagement' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class ProbeVehicleData:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.ProbeVehicleData`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import ProbeVehicleData
                    from private.osspy_der import ValueTracker
                    return ProbeVehicleData.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'ProbeVehicleData' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import ProbeVehicleData
                    from private.osspy_per import ValueTracker
                    return ProbeVehicleData.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'ProbeVehicleData' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import ProbeVehicleData
                    from private.osspy_oer import ValueTracker
                    return ProbeVehicleData.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'ProbeVehicleData' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.ProbeVehicleData``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import ProbeVehicleData
                    from private.osspy_der import ValueTracker
                    decval = ProbeVehicleData.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'ProbeVehicleData' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import ProbeVehicleData
                    from private.osspy_per import ValueTracker
                    decval = ProbeVehicleData.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'ProbeVehicleData' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import ProbeVehicleData
                    from private.osspy_oer import ValueTracker
                    decval = ProbeVehicleData.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'ProbeVehicleData' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.ProbeVehicleData``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import ProbeVehicleData
                    ProbeVehicleData.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'ProbeVehicleData' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import ProbeVehicleData
                    ProbeVehicleData.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'ProbeVehicleData' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import ProbeVehicleData
                    ProbeVehicleData.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'ProbeVehicleData' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class RTCMcorrections:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.RTCMcorrections`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import RTCMcorrections
                    from private.osspy_der import ValueTracker
                    return RTCMcorrections.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'RTCMcorrections' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import RTCMcorrections
                    from private.osspy_per import ValueTracker
                    return RTCMcorrections.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'RTCMcorrections' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import RTCMcorrections
                    from private.osspy_oer import ValueTracker
                    return RTCMcorrections.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'RTCMcorrections' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.RTCMcorrections``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import RTCMcorrections
                    from private.osspy_der import ValueTracker
                    decval = RTCMcorrections.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'RTCMcorrections' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import RTCMcorrections
                    from private.osspy_per import ValueTracker
                    decval = RTCMcorrections.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'RTCMcorrections' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import RTCMcorrections
                    from private.osspy_oer import ValueTracker
                    decval = RTCMcorrections.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'RTCMcorrections' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.RTCMcorrections``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import RTCMcorrections
                    RTCMcorrections.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'RTCMcorrections' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import RTCMcorrections
                    RTCMcorrections.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'RTCMcorrections' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import RTCMcorrections
                    RTCMcorrections.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'RTCMcorrections' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class SPAT:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.SPAT`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import SPAT
                    from private.osspy_der import ValueTracker
                    return SPAT.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'SPAT' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import SPAT
                    from private.osspy_per import ValueTracker
                    return SPAT.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'SPAT' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import SPAT
                    from private.osspy_oer import ValueTracker
                    return SPAT.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'SPAT' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.SPAT``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import SPAT
                    from private.osspy_der import ValueTracker
                    decval = SPAT.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'SPAT' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import SPAT
                    from private.osspy_per import ValueTracker
                    decval = SPAT.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'SPAT' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import SPAT
                    from private.osspy_oer import ValueTracker
                    decval = SPAT.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'SPAT' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.SPAT``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import SPAT
                    SPAT.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'SPAT' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import SPAT
                    SPAT.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'SPAT' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import SPAT
                    SPAT.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'SPAT' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class SignalRequestMessage:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.SignalRequestMessage`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import SignalRequestMessage
                    from private.osspy_der import ValueTracker
                    return SignalRequestMessage.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalRequestMessage' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import SignalRequestMessage
                    from private.osspy_per import ValueTracker
                    return SignalRequestMessage.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalRequestMessage' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import SignalRequestMessage
                    from private.osspy_oer import ValueTracker
                    return SignalRequestMessage.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalRequestMessage' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.SignalRequestMessage``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import SignalRequestMessage
                    from private.osspy_der import ValueTracker
                    decval = SignalRequestMessage.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalRequestMessage' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import SignalRequestMessage
                    from private.osspy_per import ValueTracker
                    decval = SignalRequestMessage.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalRequestMessage' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import SignalRequestMessage
                    from private.osspy_oer import ValueTracker
                    decval = SignalRequestMessage.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalRequestMessage' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.SignalRequestMessage``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import SignalRequestMessage
                    SignalRequestMessage.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalRequestMessage' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import SignalRequestMessage
                    SignalRequestMessage.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalRequestMessage' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import SignalRequestMessage
                    SignalRequestMessage.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalRequestMessage' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class SignalStatusMessage:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.SignalStatusMessage`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import SignalStatusMessage
                    from private.osspy_der import ValueTracker
                    return SignalStatusMessage.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalStatusMessage' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import SignalStatusMessage
                    from private.osspy_per import ValueTracker
                    return SignalStatusMessage.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalStatusMessage' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import SignalStatusMessage
                    from private.osspy_oer import ValueTracker
                    return SignalStatusMessage.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalStatusMessage' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.SignalStatusMessage``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import SignalStatusMessage
                    from private.osspy_der import ValueTracker
                    decval = SignalStatusMessage.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalStatusMessage' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import SignalStatusMessage
                    from private.osspy_per import ValueTracker
                    decval = SignalStatusMessage.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalStatusMessage' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import SignalStatusMessage
                    from private.osspy_oer import ValueTracker
                    decval = SignalStatusMessage.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalStatusMessage' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.SignalStatusMessage``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import SignalStatusMessage
                    SignalStatusMessage.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalStatusMessage' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import SignalStatusMessage
                    SignalStatusMessage.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalStatusMessage' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import SignalStatusMessage
                    SignalStatusMessage.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalStatusMessage' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class TravelerInformation:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.TravelerInformation`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import TravelerInformation
                    from private.osspy_der import ValueTracker
                    return TravelerInformation.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'TravelerInformation' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import TravelerInformation
                    from private.osspy_per import ValueTracker
                    return TravelerInformation.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'TravelerInformation' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import TravelerInformation
                    from private.osspy_oer import ValueTracker
                    return TravelerInformation.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'TravelerInformation' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.TravelerInformation``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import TravelerInformation
                    from private.osspy_der import ValueTracker
                    decval = TravelerInformation.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'TravelerInformation' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import TravelerInformation
                    from private.osspy_per import ValueTracker
                    decval = TravelerInformation.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'TravelerInformation' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import TravelerInformation
                    from private.osspy_oer import ValueTracker
                    decval = TravelerInformation.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'TravelerInformation' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.TravelerInformation``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import TravelerInformation
                    TravelerInformation.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'TravelerInformation' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import TravelerInformation
                    TravelerInformation.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'TravelerInformation' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import TravelerInformation
                    TravelerInformation.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'TravelerInformation' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class TestMessage00:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.TestMessage00`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import TestMessage00
                    from private.osspy_der import ValueTracker
                    return TestMessage00.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'TestMessage00' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import TestMessage00
                    from private.osspy_per import ValueTracker
                    return TestMessage00.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'TestMessage00' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import TestMessage00
                    from private.osspy_oer import ValueTracker
                    return TestMessage00.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'TestMessage00' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.TestMessage00``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import TestMessage00
                    from private.osspy_der import ValueTracker
                    decval = TestMessage00.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'TestMessage00' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import TestMessage00
                    from private.osspy_per import ValueTracker
                    decval = TestMessage00.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'TestMessage00' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import TestMessage00
                    from private.osspy_oer import ValueTracker
                    decval = TestMessage00.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'TestMessage00' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.TestMessage00``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import TestMessage00
                    TestMessage00.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'TestMessage00' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import TestMessage00
                    TestMessage00.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'TestMessage00' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import TestMessage00
                    TestMessage00.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'TestMessage00' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class TestMessage01(TestMessage00):
        pass

    class TestMessage02(TestMessage00):
        pass

    class TestMessage03(TestMessage00):
        pass

    class TestMessage04(TestMessage00):
        pass

    class TestMessage05(TestMessage00):
        pass

    class TestMessage06(TestMessage00):
        pass

    class TestMessage07(TestMessage00):
        pass

    class TestMessage08(TestMessage00):
        pass

    class TestMessage09(TestMessage00):
        pass

    class TestMessage10(TestMessage00):
        pass

    class TestMessage11(TestMessage00):
        pass

    class TestMessage12(TestMessage00):
        pass

    class TestMessage13(TestMessage00):
        pass

    class TestMessage14(TestMessage00):
        pass

    class TestMessage15(TestMessage00):
        pass

    class URL_Link:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.URL_Link`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import URL_Link
                    from private.osspy_der import ValueTracker
                    return URL_Link.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'URL_Link' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import URL_Link
                    from private.osspy_per import ValueTracker
                    return URL_Link.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'URL_Link' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import URL_Link
                    from private.osspy_oer import ValueTracker
                    return URL_Link.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'URL_Link' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.URL_Link``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import URL_Link
                    from private.osspy_der import ValueTracker
                    decval = URL_Link.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'URL_Link' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import URL_Link
                    from private.osspy_per import ValueTracker
                    decval = URL_Link.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'URL_Link' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import URL_Link
                    from private.osspy_oer import ValueTracker
                    decval = URL_Link.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'URL_Link' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.URL_Link``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import URL_Link
                    URL_Link.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'URL_Link' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import URL_Link
                    URL_Link.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'URL_Link' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import URL_Link
                    URL_Link.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'URL_Link' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class DDate:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.DDate`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import DDate
                    from private.osspy_der import ValueTracker
                    return DDate.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'DDate' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import DDate
                    from private.osspy_per import ValueTracker
                    return DDate.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'DDate' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import DDate
                    from private.osspy_oer import ValueTracker
                    return DDate.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'DDate' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.DDate``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import DDate
                    from private.osspy_der import ValueTracker
                    decval = DDate.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'DDate' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import DDate
                    from private.osspy_per import ValueTracker
                    decval = DDate.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'DDate' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import DDate
                    from private.osspy_oer import ValueTracker
                    decval = DDate.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'DDate' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.DDate``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import DDate
                    DDate.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'DDate' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import DDate
                    DDate.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'DDate' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import DDate
                    DDate.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'DDate' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class DFullTime:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.DFullTime`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import DFullTime
                    from private.osspy_der import ValueTracker
                    return DFullTime.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'DFullTime' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import DFullTime
                    from private.osspy_per import ValueTracker
                    return DFullTime.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'DFullTime' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import DFullTime
                    from private.osspy_oer import ValueTracker
                    return DFullTime.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'DFullTime' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.DFullTime``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import DFullTime
                    from private.osspy_der import ValueTracker
                    decval = DFullTime.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'DFullTime' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import DFullTime
                    from private.osspy_per import ValueTracker
                    decval = DFullTime.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'DFullTime' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import DFullTime
                    from private.osspy_oer import ValueTracker
                    decval = DFullTime.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'DFullTime' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.DFullTime``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import DFullTime
                    DFullTime.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'DFullTime' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import DFullTime
                    DFullTime.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'DFullTime' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import DFullTime
                    DFullTime.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'DFullTime' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class DMonthDay:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.DMonthDay`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import DMonthDay
                    from private.osspy_der import ValueTracker
                    return DMonthDay.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'DMonthDay' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import DMonthDay
                    from private.osspy_per import ValueTracker
                    return DMonthDay.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'DMonthDay' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import DMonthDay
                    from private.osspy_oer import ValueTracker
                    return DMonthDay.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'DMonthDay' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.DMonthDay``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import DMonthDay
                    from private.osspy_der import ValueTracker
                    decval = DMonthDay.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'DMonthDay' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import DMonthDay
                    from private.osspy_per import ValueTracker
                    decval = DMonthDay.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'DMonthDay' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import DMonthDay
                    from private.osspy_oer import ValueTracker
                    decval = DMonthDay.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'DMonthDay' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.DMonthDay``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import DMonthDay
                    DMonthDay.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'DMonthDay' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import DMonthDay
                    DMonthDay.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'DMonthDay' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import DMonthDay
                    DMonthDay.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'DMonthDay' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class DTime:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.DTime`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import DTime
                    from private.osspy_der import ValueTracker
                    return DTime.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'DTime' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import DTime
                    from private.osspy_per import ValueTracker
                    return DTime.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'DTime' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import DTime
                    from private.osspy_oer import ValueTracker
                    return DTime.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'DTime' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.DTime``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import DTime
                    from private.osspy_der import ValueTracker
                    decval = DTime.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'DTime' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import DTime
                    from private.osspy_per import ValueTracker
                    decval = DTime.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'DTime' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import DTime
                    from private.osspy_oer import ValueTracker
                    decval = DTime.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'DTime' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.DTime``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import DTime
                    DTime.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'DTime' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import DTime
                    DTime.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'DTime' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import DTime
                    DTime.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'DTime' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class DYearMonth:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.DYearMonth`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import DYearMonth
                    from private.osspy_der import ValueTracker
                    return DYearMonth.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'DYearMonth' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import DYearMonth
                    from private.osspy_per import ValueTracker
                    return DYearMonth.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'DYearMonth' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import DYearMonth
                    from private.osspy_oer import ValueTracker
                    return DYearMonth.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'DYearMonth' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.DYearMonth``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import DYearMonth
                    from private.osspy_der import ValueTracker
                    decval = DYearMonth.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'DYearMonth' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import DYearMonth
                    from private.osspy_per import ValueTracker
                    decval = DYearMonth.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'DYearMonth' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import DYearMonth
                    from private.osspy_oer import ValueTracker
                    decval = DYearMonth.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'DYearMonth' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.DYearMonth``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import DYearMonth
                    DYearMonth.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'DYearMonth' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import DYearMonth
                    DYearMonth.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'DYearMonth' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import DYearMonth
                    DYearMonth.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'DYearMonth' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class SpecialVehicleExtensions:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.SpecialVehicleExtensions`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import SpecialVehicleExtensions
                    from private.osspy_der import ValueTracker
                    return SpecialVehicleExtensions.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'SpecialVehicleExtensions' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import SpecialVehicleExtensions
                    from private.osspy_per import ValueTracker
                    return SpecialVehicleExtensions.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'SpecialVehicleExtensions' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import SpecialVehicleExtensions
                    from private.osspy_oer import ValueTracker
                    return SpecialVehicleExtensions.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'SpecialVehicleExtensions' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.SpecialVehicleExtensions``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import SpecialVehicleExtensions
                    from private.osspy_der import ValueTracker
                    decval = SpecialVehicleExtensions.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'SpecialVehicleExtensions' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import SpecialVehicleExtensions
                    from private.osspy_per import ValueTracker
                    decval = SpecialVehicleExtensions.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'SpecialVehicleExtensions' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import SpecialVehicleExtensions
                    from private.osspy_oer import ValueTracker
                    decval = SpecialVehicleExtensions.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'SpecialVehicleExtensions' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.SpecialVehicleExtensions``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import SpecialVehicleExtensions
                    SpecialVehicleExtensions.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'SpecialVehicleExtensions' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import SpecialVehicleExtensions
                    SpecialVehicleExtensions.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'SpecialVehicleExtensions' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import SpecialVehicleExtensions
                    SpecialVehicleExtensions.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'SpecialVehicleExtensions' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class SupplementalVehicleExtensions:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.SupplementalVehicleExtensions`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import SupplementalVehicleExtensions
                    from private.osspy_der import ValueTracker
                    return SupplementalVehicleExtensions.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'SupplementalVehicleExtensions' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import SupplementalVehicleExtensions
                    from private.osspy_per import ValueTracker
                    return SupplementalVehicleExtensions.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'SupplementalVehicleExtensions' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import SupplementalVehicleExtensions
                    from private.osspy_oer import ValueTracker
                    return SupplementalVehicleExtensions.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'SupplementalVehicleExtensions' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.SupplementalVehicleExtensions``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import SupplementalVehicleExtensions
                    from private.osspy_der import ValueTracker
                    decval = SupplementalVehicleExtensions.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'SupplementalVehicleExtensions' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import SupplementalVehicleExtensions
                    from private.osspy_per import ValueTracker
                    decval = SupplementalVehicleExtensions.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'SupplementalVehicleExtensions' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import SupplementalVehicleExtensions
                    from private.osspy_oer import ValueTracker
                    decval = SupplementalVehicleExtensions.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'SupplementalVehicleExtensions' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.SupplementalVehicleExtensions``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import SupplementalVehicleExtensions
                    SupplementalVehicleExtensions.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'SupplementalVehicleExtensions' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import SupplementalVehicleExtensions
                    SupplementalVehicleExtensions.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'SupplementalVehicleExtensions' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import SupplementalVehicleExtensions
                    SupplementalVehicleExtensions.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'SupplementalVehicleExtensions' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class VerticalOffset:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.VerticalOffset`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import VerticalOffset
                    from private.osspy_der import ValueTracker
                    return VerticalOffset.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'VerticalOffset' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import VerticalOffset
                    from private.osspy_per import ValueTracker
                    return VerticalOffset.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'VerticalOffset' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import VerticalOffset
                    from private.osspy_oer import ValueTracker
                    return VerticalOffset.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'VerticalOffset' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.VerticalOffset``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import VerticalOffset
                    from private.osspy_der import ValueTracker
                    decval = VerticalOffset.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'VerticalOffset' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import VerticalOffset
                    from private.osspy_per import ValueTracker
                    decval = VerticalOffset.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'VerticalOffset' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import VerticalOffset
                    from private.osspy_oer import ValueTracker
                    decval = VerticalOffset.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'VerticalOffset' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.VerticalOffset``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import VerticalOffset
                    VerticalOffset.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'VerticalOffset' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import VerticalOffset
                    VerticalOffset.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'VerticalOffset' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import VerticalOffset
                    VerticalOffset.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'VerticalOffset' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class CodeWord:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.CodeWord`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import CodeWord
                    from private.osspy_der import ValueTracker
                    return CodeWord.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'CodeWord' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import CodeWord
                    from private.osspy_per import ValueTracker
                    return CodeWord.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'CodeWord' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import CodeWord
                    from private.osspy_oer import ValueTracker
                    return CodeWord.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'CodeWord' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.CodeWord``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import CodeWord
                    from private.osspy_der import ValueTracker
                    decval = CodeWord.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'CodeWord' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import CodeWord
                    from private.osspy_per import ValueTracker
                    decval = CodeWord.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'CodeWord' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import CodeWord
                    from private.osspy_oer import ValueTracker
                    decval = CodeWord.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'CodeWord' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.CodeWord``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import CodeWord
                    CodeWord.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'CodeWord' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import CodeWord
                    CodeWord.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'CodeWord' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import CodeWord
                    CodeWord.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'CodeWord' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class Count:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.Count`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import Count
                    from private.osspy_der import ValueTracker
                    return Count.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'Count' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import Count
                    from private.osspy_per import ValueTracker
                    return Count.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'Count' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import Count
                    from private.osspy_oer import ValueTracker
                    return Count.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'Count' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.Count``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import Count
                    from private.osspy_der import ValueTracker
                    decval = Count.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'Count' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import Count
                    from private.osspy_per import ValueTracker
                    decval = Count.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'Count' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import Count
                    from private.osspy_oer import ValueTracker
                    decval = Count.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'Count' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.Count``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import Count
                    Count.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'Count' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import Count
                    Count.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'Count' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import Count
                    Count.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'Count' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class DSRCmsgID:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.DSRCmsgID`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import DSRCmsgID
                    from private.osspy_der import ValueTracker
                    return DSRCmsgID.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'DSRCmsgID' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import DSRCmsgID
                    from private.osspy_per import ValueTracker
                    return DSRCmsgID.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'DSRCmsgID' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import DSRCmsgID
                    from private.osspy_oer import ValueTracker
                    return DSRCmsgID.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'DSRCmsgID' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.DSRCmsgID``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import DSRCmsgID
                    from private.osspy_der import ValueTracker
                    decval = DSRCmsgID.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'DSRCmsgID' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import DSRCmsgID
                    from private.osspy_per import ValueTracker
                    decval = DSRCmsgID.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'DSRCmsgID' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import DSRCmsgID
                    from private.osspy_oer import ValueTracker
                    decval = DSRCmsgID.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'DSRCmsgID' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.DSRCmsgID``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import DSRCmsgID
                    DSRCmsgID.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'DSRCmsgID' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import DSRCmsgID
                    DSRCmsgID.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'DSRCmsgID' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import DSRCmsgID
                    DSRCmsgID.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'DSRCmsgID' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class Duration:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.Duration`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import Duration
                    from private.osspy_der import ValueTracker
                    return Duration.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'Duration' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import Duration
                    from private.osspy_per import ValueTracker
                    return Duration.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'Duration' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import Duration
                    from private.osspy_oer import ValueTracker
                    return Duration.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'Duration' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.Duration``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import Duration
                    from private.osspy_der import ValueTracker
                    decval = Duration.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'Duration' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import Duration
                    from private.osspy_per import ValueTracker
                    decval = Duration.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'Duration' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import Duration
                    from private.osspy_oer import ValueTracker
                    decval = Duration.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'Duration' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.Duration``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import Duration
                    Duration.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'Duration' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import Duration
                    Duration.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'Duration' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import Duration
                    Duration.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'Duration' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class Location_quality:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.Location_quality`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import Location_quality
                    from private.osspy_der import ValueTracker
                    return Location_quality.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'Location_quality' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import Location_quality
                    from private.osspy_per import ValueTracker
                    return Location_quality.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'Location_quality' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import Location_quality
                    from private.osspy_oer import ValueTracker
                    return Location_quality.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'Location_quality' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.Location_quality``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import Location_quality
                    from private.osspy_der import ValueTracker
                    decval = Location_quality.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'Location_quality' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import Location_quality
                    from private.osspy_per import ValueTracker
                    decval = Location_quality.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'Location_quality' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import Location_quality
                    from private.osspy_oer import ValueTracker
                    decval = Location_quality.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'Location_quality' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.Location_quality``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import Location_quality
                    Location_quality.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'Location_quality' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import Location_quality
                    Location_quality.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'Location_quality' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import Location_quality
                    Location_quality.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'Location_quality' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class Location_tech:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.Location_tech`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import Location_tech
                    from private.osspy_der import ValueTracker
                    return Location_tech.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'Location_tech' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import Location_tech
                    from private.osspy_per import ValueTracker
                    return Location_tech.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'Location_tech' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import Location_tech
                    from private.osspy_oer import ValueTracker
                    return Location_tech.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'Location_tech' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.Location_tech``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import Location_tech
                    from private.osspy_der import ValueTracker
                    decval = Location_tech.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'Location_tech' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import Location_tech
                    from private.osspy_per import ValueTracker
                    decval = Location_tech.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'Location_tech' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import Location_tech
                    from private.osspy_oer import ValueTracker
                    decval = Location_tech.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'Location_tech' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.Location_tech``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import Location_tech
                    Location_tech.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'Location_tech' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import Location_tech
                    Location_tech.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'Location_tech' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import Location_tech
                    Location_tech.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'Location_tech' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class MessageBLOB:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.MessageBLOB`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import MessageBLOB
                    from private.osspy_der import ValueTracker
                    return MessageBLOB.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'MessageBLOB' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import MessageBLOB
                    from private.osspy_per import ValueTracker
                    return MessageBLOB.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'MessageBLOB' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import MessageBLOB
                    from private.osspy_oer import ValueTracker
                    return MessageBLOB.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'MessageBLOB' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.MessageBLOB``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import MessageBLOB
                    from private.osspy_der import ValueTracker
                    decval = MessageBLOB.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'MessageBLOB' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import MessageBLOB
                    from private.osspy_per import ValueTracker
                    decval = MessageBLOB.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'MessageBLOB' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import MessageBLOB
                    from private.osspy_oer import ValueTracker
                    decval = MessageBLOB.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'MessageBLOB' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.MessageBLOB``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import MessageBLOB
                    MessageBLOB.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'MessageBLOB' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import MessageBLOB
                    MessageBLOB.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'MessageBLOB' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import MessageBLOB
                    MessageBLOB.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'MessageBLOB' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class PayloadData:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.PayloadData`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import PayloadData
                    from private.osspy_der import ValueTracker
                    return PayloadData.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'PayloadData' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import PayloadData
                    from private.osspy_per import ValueTracker
                    return PayloadData.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'PayloadData' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import PayloadData
                    from private.osspy_oer import ValueTracker
                    return PayloadData.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'PayloadData' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.PayloadData``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import PayloadData
                    from private.osspy_der import ValueTracker
                    decval = PayloadData.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'PayloadData' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import PayloadData
                    from private.osspy_per import ValueTracker
                    decval = PayloadData.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'PayloadData' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import PayloadData
                    from private.osspy_oer import ValueTracker
                    decval = PayloadData.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'PayloadData' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.PayloadData``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import PayloadData
                    PayloadData.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'PayloadData' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import PayloadData
                    PayloadData.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'PayloadData' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import PayloadData
                    PayloadData.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'PayloadData' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class SignalReqScheme:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.SignalReqScheme`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import SignalReqScheme
                    from private.osspy_der import ValueTracker
                    return SignalReqScheme.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalReqScheme' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import SignalReqScheme
                    from private.osspy_per import ValueTracker
                    return SignalReqScheme.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalReqScheme' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import SignalReqScheme
                    from private.osspy_oer import ValueTracker
                    return SignalReqScheme.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalReqScheme' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.SignalReqScheme``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import SignalReqScheme
                    from private.osspy_der import ValueTracker
                    decval = SignalReqScheme.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalReqScheme' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import SignalReqScheme
                    from private.osspy_per import ValueTracker
                    decval = SignalReqScheme.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalReqScheme' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import SignalReqScheme
                    from private.osspy_oer import ValueTracker
                    decval = SignalReqScheme.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalReqScheme' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.SignalReqScheme``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import SignalReqScheme
                    SignalReqScheme.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalReqScheme' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import SignalReqScheme
                    SignalReqScheme.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalReqScheme' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import SignalReqScheme
                    SignalReqScheme.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalReqScheme' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class TransitStatus:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.TransitStatus`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import TransitStatus
                    from private.osspy_der import ValueTracker
                    return TransitStatus.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'TransitStatus' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import TransitStatus
                    from private.osspy_per import ValueTracker
                    return TransitStatus.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'TransitStatus' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import TransitStatus
                    from private.osspy_oer import ValueTracker
                    return TransitStatus.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'TransitStatus' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.TransitStatus``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import TransitStatus
                    from private.osspy_der import ValueTracker
                    decval = TransitStatus.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'TransitStatus' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import TransitStatus
                    from private.osspy_per import ValueTracker
                    decval = TransitStatus.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'TransitStatus' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import TransitStatus
                    from private.osspy_oer import ValueTracker
                    decval = TransitStatus.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'TransitStatus' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.TransitStatus``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import TransitStatus
                    TransitStatus.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'TransitStatus' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import TransitStatus
                    TransitStatus.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'TransitStatus' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import TransitStatus
                    TransitStatus.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'TransitStatus' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class BSMPSMParams:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.BSMPSMParams`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import BSMPSMParams
                    from private.osspy_der import ValueTracker
                    return BSMPSMParams.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'BSMPSMParams' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import BSMPSMParams
                    from private.osspy_per import ValueTracker
                    return BSMPSMParams.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'BSMPSMParams' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import BSMPSMParams
                    from private.osspy_oer import ValueTracker
                    return BSMPSMParams.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'BSMPSMParams' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.BSMPSMParams``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import BSMPSMParams
                    from private.osspy_der import ValueTracker
                    decval = BSMPSMParams.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'BSMPSMParams' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import BSMPSMParams
                    from private.osspy_per import ValueTracker
                    decval = BSMPSMParams.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'BSMPSMParams' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import BSMPSMParams
                    from private.osspy_oer import ValueTracker
                    decval = BSMPSMParams.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'BSMPSMParams' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.BSMPSMParams``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import BSMPSMParams
                    BSMPSMParams.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'BSMPSMParams' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import BSMPSMParams
                    BSMPSMParams.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'BSMPSMParams' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import BSMPSMParams
                    BSMPSMParams.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'BSMPSMParams' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class MAPSPaTParams:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.MAPSPaTParams`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import MAPSPaTParams
                    from private.osspy_der import ValueTracker
                    return MAPSPaTParams.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'MAPSPaTParams' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import MAPSPaTParams
                    from private.osspy_per import ValueTracker
                    return MAPSPaTParams.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'MAPSPaTParams' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import MAPSPaTParams
                    from private.osspy_oer import ValueTracker
                    return MAPSPaTParams.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'MAPSPaTParams' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.MAPSPaTParams``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import MAPSPaTParams
                    from private.osspy_der import ValueTracker
                    decval = MAPSPaTParams.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'MAPSPaTParams' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import MAPSPaTParams
                    from private.osspy_per import ValueTracker
                    decval = MAPSPaTParams.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'MAPSPaTParams' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import MAPSPaTParams
                    from private.osspy_oer import ValueTracker
                    decval = MAPSPaTParams.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'MAPSPaTParams' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.MAPSPaTParams``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import MAPSPaTParams
                    MAPSPaTParams.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'MAPSPaTParams' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import MAPSPaTParams
                    MAPSPaTParams.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'MAPSPaTParams' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import MAPSPaTParams
                    MAPSPaTParams.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'MAPSPaTParams' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class SignalAheadParams:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.SignalAheadParams`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import SignalAheadParams
                    from private.osspy_der import ValueTracker
                    return SignalAheadParams.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalAheadParams' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import SignalAheadParams
                    from private.osspy_per import ValueTracker
                    return SignalAheadParams.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalAheadParams' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import SignalAheadParams
                    from private.osspy_oer import ValueTracker
                    return SignalAheadParams.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalAheadParams' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.SignalAheadParams``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import SignalAheadParams
                    from private.osspy_der import ValueTracker
                    decval = SignalAheadParams.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalAheadParams' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import SignalAheadParams
                    from private.osspy_per import ValueTracker
                    decval = SignalAheadParams.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalAheadParams' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import SignalAheadParams
                    from private.osspy_oer import ValueTracker
                    decval = SignalAheadParams.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalAheadParams' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.SignalAheadParams``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import SignalAheadParams
                    SignalAheadParams.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalAheadParams' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import SignalAheadParams
                    SignalAheadParams.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalAheadParams' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import SignalAheadParams
                    SignalAheadParams.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalAheadParams' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class DataRequestMessage:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.DataRequestMessage`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import DataRequestMessage
                    from private.osspy_der import ValueTracker
                    return DataRequestMessage.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'DataRequestMessage' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import DataRequestMessage
                    from private.osspy_per import ValueTracker
                    return DataRequestMessage.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'DataRequestMessage' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import DataRequestMessage
                    from private.osspy_oer import ValueTracker
                    return DataRequestMessage.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'DataRequestMessage' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.DataRequestMessage``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import DataRequestMessage
                    from private.osspy_der import ValueTracker
                    decval = DataRequestMessage.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'DataRequestMessage' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import DataRequestMessage
                    from private.osspy_per import ValueTracker
                    decval = DataRequestMessage.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'DataRequestMessage' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import DataRequestMessage
                    from private.osspy_oer import ValueTracker
                    decval = DataRequestMessage.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'DataRequestMessage' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.DataRequestMessage``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import DataRequestMessage
                    DataRequestMessage.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'DataRequestMessage' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import DataRequestMessage
                    DataRequestMessage.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'DataRequestMessage' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import DataRequestMessage
                    DataRequestMessage.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'DataRequestMessage' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class DataRequestResponse:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.DataRequestResponse`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import DataRequestResponse
                    from private.osspy_der import ValueTracker
                    return DataRequestResponse.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'DataRequestResponse' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import DataRequestResponse
                    from private.osspy_per import ValueTracker
                    return DataRequestResponse.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'DataRequestResponse' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import DataRequestResponse
                    from private.osspy_oer import ValueTracker
                    return DataRequestResponse.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'DataRequestResponse' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.DataRequestResponse``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import DataRequestResponse
                    from private.osspy_der import ValueTracker
                    decval = DataRequestResponse.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'DataRequestResponse' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import DataRequestResponse
                    from private.osspy_per import ValueTracker
                    decval = DataRequestResponse.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'DataRequestResponse' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import DataRequestResponse
                    from private.osspy_oer import ValueTracker
                    decval = DataRequestResponse.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'DataRequestResponse' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.DataRequestResponse``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import DataRequestResponse
                    DataRequestResponse.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'DataRequestResponse' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import DataRequestResponse
                    DataRequestResponse.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'DataRequestResponse' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import DataRequestResponse
                    DataRequestResponse.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'DataRequestResponse' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class StatusMessage:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.StatusMessage`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import StatusMessage
                    from private.osspy_der import ValueTracker
                    return StatusMessage.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'StatusMessage' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import StatusMessage
                    from private.osspy_per import ValueTracker
                    return StatusMessage.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'StatusMessage' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import StatusMessage
                    from private.osspy_oer import ValueTracker
                    return StatusMessage.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'StatusMessage' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.StatusMessage``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import StatusMessage
                    from private.osspy_der import ValueTracker
                    decval = StatusMessage.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'StatusMessage' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import StatusMessage
                    from private.osspy_per import ValueTracker
                    decval = StatusMessage.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'StatusMessage' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import StatusMessage
                    from private.osspy_oer import ValueTracker
                    decval = StatusMessage.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'StatusMessage' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.StatusMessage``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import StatusMessage
                    StatusMessage.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'StatusMessage' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import StatusMessage
                    StatusMessage.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'StatusMessage' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import StatusMessage
                    StatusMessage.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'StatusMessage' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class DisconnectMessage:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.DisconnectMessage`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import DisconnectMessage
                    from private.osspy_der import ValueTracker
                    return DisconnectMessage.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'DisconnectMessage' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import DisconnectMessage
                    from private.osspy_per import ValueTracker
                    return DisconnectMessage.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'DisconnectMessage' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import DisconnectMessage
                    from private.osspy_oer import ValueTracker
                    return DisconnectMessage.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'DisconnectMessage' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.DisconnectMessage``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import DisconnectMessage
                    from private.osspy_der import ValueTracker
                    decval = DisconnectMessage.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'DisconnectMessage' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import DisconnectMessage
                    from private.osspy_per import ValueTracker
                    decval = DisconnectMessage.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'DisconnectMessage' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import DisconnectMessage
                    from private.osspy_oer import ValueTracker
                    decval = DisconnectMessage.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'DisconnectMessage' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.DisconnectMessage``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import DisconnectMessage
                    DisconnectMessage.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'DisconnectMessage' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import DisconnectMessage
                    DisconnectMessage.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'DisconnectMessage' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import DisconnectMessage
                    DisconnectMessage.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'DisconnectMessage' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class SignalAheadMessage:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``DSRC.SignalAheadMessage`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import SignalAheadMessage
                    from private.osspy_der import ValueTracker
                    return SignalAheadMessage.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalAheadMessage' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import SignalAheadMessage
                    from private.osspy_per import ValueTracker
                    return SignalAheadMessage.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalAheadMessage' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import SignalAheadMessage
                    from private.osspy_oer import ValueTracker
                    return SignalAheadMessage.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalAheadMessage' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``DSRC.SignalAheadMessage``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import SignalAheadMessage
                    from private.osspy_der import ValueTracker
                    decval = SignalAheadMessage.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalAheadMessage' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import SignalAheadMessage
                    from private.osspy_per import ValueTracker
                    decval = SignalAheadMessage.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalAheadMessage' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import SignalAheadMessage
                    from private.osspy_oer import ValueTracker
                    decval = SignalAheadMessage.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalAheadMessage' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``DSRC.SignalAheadMessage``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import SignalAheadMessage
                    SignalAheadMessage.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalAheadMessage' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import SignalAheadMessage
                    SignalAheadMessage.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalAheadMessage' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import SignalAheadMessage
                    SignalAheadMessage.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'SignalAheadMessage' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    RegionId: "AddGrpB.MsgCount"

class AddGrpB:
    class MsgCount:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``AddGrpB.MsgCount`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import MsgCount__A
                    from private.osspy_der import ValueTracker
                    return MsgCount__A.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'MsgCount__A' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import MsgCount__A
                    from private.osspy_per import ValueTracker
                    return MsgCount__A.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'MsgCount__A' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import MsgCount__A
                    from private.osspy_oer import ValueTracker
                    return MsgCount__A.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'MsgCount__A' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``AddGrpB.MsgCount``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import MsgCount__A
                    from private.osspy_der import ValueTracker
                    decval = MsgCount__A.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'MsgCount__A' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import MsgCount__A
                    from private.osspy_per import ValueTracker
                    decval = MsgCount__A.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'MsgCount__A' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import MsgCount__A
                    from private.osspy_oer import ValueTracker
                    decval = MsgCount__A.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'MsgCount__A' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``AddGrpB.MsgCount``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import MsgCount__A
                    MsgCount__A.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'MsgCount__A' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import MsgCount__A
                    MsgCount__A.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'MsgCount__A' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import MsgCount__A
                    MsgCount__A.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'MsgCount__A' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class Angle:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``AddGrpB.Angle`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import Angle__A
                    from private.osspy_der import ValueTracker
                    return Angle__A.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'Angle__A' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import Angle__A
                    from private.osspy_per import ValueTracker
                    return Angle__A.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'Angle__A' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import Angle__A
                    from private.osspy_oer import ValueTracker
                    return Angle__A.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'Angle__A' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``AddGrpB.Angle``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import Angle__A
                    from private.osspy_der import ValueTracker
                    decval = Angle__A.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'Angle__A' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import Angle__A
                    from private.osspy_per import ValueTracker
                    decval = Angle__A.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'Angle__A' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import Angle__A
                    from private.osspy_oer import ValueTracker
                    decval = Angle__A.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'Angle__A' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``AddGrpB.Angle``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import Angle__A
                    Angle__A.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'Angle__A' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import Angle__A
                    Angle__A.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'Angle__A' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import Angle__A
                    Angle__A.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'Angle__A' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class LaneDataAttribute_addGrpB:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``AddGrpB.LaneDataAttribute_addGrpB`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import LaneDataAttribute_addGrpB
                    from private.osspy_der import ValueTracker
                    return LaneDataAttribute_addGrpB.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'LaneDataAttribute_addGrpB' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import LaneDataAttribute_addGrpB
                    from private.osspy_per import ValueTracker
                    return LaneDataAttribute_addGrpB.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'LaneDataAttribute_addGrpB' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import LaneDataAttribute_addGrpB
                    from private.osspy_oer import ValueTracker
                    return LaneDataAttribute_addGrpB.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'LaneDataAttribute_addGrpB' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``AddGrpB.LaneDataAttribute_addGrpB``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import LaneDataAttribute_addGrpB
                    from private.osspy_der import ValueTracker
                    decval = LaneDataAttribute_addGrpB.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'LaneDataAttribute_addGrpB' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import LaneDataAttribute_addGrpB
                    from private.osspy_per import ValueTracker
                    decval = LaneDataAttribute_addGrpB.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'LaneDataAttribute_addGrpB' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import LaneDataAttribute_addGrpB
                    from private.osspy_oer import ValueTracker
                    decval = LaneDataAttribute_addGrpB.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'LaneDataAttribute_addGrpB' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``AddGrpB.LaneDataAttribute_addGrpB``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import LaneDataAttribute_addGrpB
                    LaneDataAttribute_addGrpB.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'LaneDataAttribute_addGrpB' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import LaneDataAttribute_addGrpB
                    LaneDataAttribute_addGrpB.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'LaneDataAttribute_addGrpB' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import LaneDataAttribute_addGrpB
                    LaneDataAttribute_addGrpB.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'LaneDataAttribute_addGrpB' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class MovementEvent_addGrpB:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``AddGrpB.MovementEvent_addGrpB`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import MovementEvent_addGrpB
                    from private.osspy_der import ValueTracker
                    return MovementEvent_addGrpB.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'MovementEvent_addGrpB' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import MovementEvent_addGrpB
                    from private.osspy_per import ValueTracker
                    return MovementEvent_addGrpB.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'MovementEvent_addGrpB' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import MovementEvent_addGrpB
                    from private.osspy_oer import ValueTracker
                    return MovementEvent_addGrpB.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'MovementEvent_addGrpB' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``AddGrpB.MovementEvent_addGrpB``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import MovementEvent_addGrpB
                    from private.osspy_der import ValueTracker
                    decval = MovementEvent_addGrpB.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'MovementEvent_addGrpB' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import MovementEvent_addGrpB
                    from private.osspy_per import ValueTracker
                    decval = MovementEvent_addGrpB.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'MovementEvent_addGrpB' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import MovementEvent_addGrpB
                    from private.osspy_oer import ValueTracker
                    decval = MovementEvent_addGrpB.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'MovementEvent_addGrpB' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``AddGrpB.MovementEvent_addGrpB``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import MovementEvent_addGrpB
                    MovementEvent_addGrpB.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'MovementEvent_addGrpB' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import MovementEvent_addGrpB
                    MovementEvent_addGrpB.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'MovementEvent_addGrpB' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import MovementEvent_addGrpB
                    MovementEvent_addGrpB.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'MovementEvent_addGrpB' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class NodeOffsetPointXY_addGrpB:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``AddGrpB.NodeOffsetPointXY_addGrpB`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import NodeOffsetPointXY_addGrpB
                    from private.osspy_der import ValueTracker
                    return NodeOffsetPointXY_addGrpB.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'NodeOffsetPointXY_addGrpB' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import NodeOffsetPointXY_addGrpB
                    from private.osspy_per import ValueTracker
                    return NodeOffsetPointXY_addGrpB.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'NodeOffsetPointXY_addGrpB' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import NodeOffsetPointXY_addGrpB
                    from private.osspy_oer import ValueTracker
                    return NodeOffsetPointXY_addGrpB.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'NodeOffsetPointXY_addGrpB' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``AddGrpB.NodeOffsetPointXY_addGrpB``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import NodeOffsetPointXY_addGrpB
                    from private.osspy_der import ValueTracker
                    decval = NodeOffsetPointXY_addGrpB.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'NodeOffsetPointXY_addGrpB' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import NodeOffsetPointXY_addGrpB
                    from private.osspy_per import ValueTracker
                    decval = NodeOffsetPointXY_addGrpB.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'NodeOffsetPointXY_addGrpB' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import NodeOffsetPointXY_addGrpB
                    from private.osspy_oer import ValueTracker
                    decval = NodeOffsetPointXY_addGrpB.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'NodeOffsetPointXY_addGrpB' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``AddGrpB.NodeOffsetPointXY_addGrpB``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import NodeOffsetPointXY_addGrpB
                    NodeOffsetPointXY_addGrpB.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'NodeOffsetPointXY_addGrpB' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import NodeOffsetPointXY_addGrpB
                    NodeOffsetPointXY_addGrpB.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'NodeOffsetPointXY_addGrpB' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import NodeOffsetPointXY_addGrpB
                    NodeOffsetPointXY_addGrpB.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'NodeOffsetPointXY_addGrpB' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class Position3D_addGrpB:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``AddGrpB.Position3D_addGrpB`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import Position3D_addGrpB
                    from private.osspy_der import ValueTracker
                    return Position3D_addGrpB.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'Position3D_addGrpB' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import Position3D_addGrpB
                    from private.osspy_per import ValueTracker
                    return Position3D_addGrpB.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'Position3D_addGrpB' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import Position3D_addGrpB
                    from private.osspy_oer import ValueTracker
                    return Position3D_addGrpB.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'Position3D_addGrpB' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``AddGrpB.Position3D_addGrpB``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import Position3D_addGrpB
                    from private.osspy_der import ValueTracker
                    decval = Position3D_addGrpB.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'Position3D_addGrpB' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import Position3D_addGrpB
                    from private.osspy_per import ValueTracker
                    decval = Position3D_addGrpB.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'Position3D_addGrpB' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import Position3D_addGrpB
                    from private.osspy_oer import ValueTracker
                    decval = Position3D_addGrpB.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'Position3D_addGrpB' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``AddGrpB.Position3D_addGrpB``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import Position3D_addGrpB
                    Position3D_addGrpB.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'Position3D_addGrpB' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import Position3D_addGrpB
                    Position3D_addGrpB.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'Position3D_addGrpB' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import Position3D_addGrpB
                    Position3D_addGrpB.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'Position3D_addGrpB' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class TimeMark:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``AddGrpB.TimeMark`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import TimeMark__A
                    from private.osspy_der import ValueTracker
                    return TimeMark__A.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'TimeMark__A' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import TimeMark__A
                    from private.osspy_per import ValueTracker
                    return TimeMark__A.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'TimeMark__A' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import TimeMark__A
                    from private.osspy_oer import ValueTracker
                    return TimeMark__A.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'TimeMark__A' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``AddGrpB.TimeMark``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import TimeMark__A
                    from private.osspy_der import ValueTracker
                    decval = TimeMark__A.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'TimeMark__A' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import TimeMark__A
                    from private.osspy_per import ValueTracker
                    decval = TimeMark__A.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'TimeMark__A' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import TimeMark__A
                    from private.osspy_oer import ValueTracker
                    decval = TimeMark__A.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'TimeMark__A' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``AddGrpB.TimeMark``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import TimeMark__A
                    TimeMark__A.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'TimeMark__A' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import TimeMark__A
                    TimeMark__A.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'TimeMark__A' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import TimeMark__A
                    TimeMark__A.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'TimeMark__A' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

class AddGrpC:
    class ConnectionManeuverAssist_addGrpC:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``AddGrpC.ConnectionManeuverAssist_addGrpC`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import ConnectionManeuverAssist_addGrpC
                    from private.osspy_der import ValueTracker
                    return ConnectionManeuverAssist_addGrpC.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'ConnectionManeuverAssist_addGrpC' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import ConnectionManeuverAssist_addGrpC
                    from private.osspy_per import ValueTracker
                    return ConnectionManeuverAssist_addGrpC.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'ConnectionManeuverAssist_addGrpC' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import ConnectionManeuverAssist_addGrpC
                    from private.osspy_oer import ValueTracker
                    return ConnectionManeuverAssist_addGrpC.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'ConnectionManeuverAssist_addGrpC' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``AddGrpC.ConnectionManeuverAssist_addGrpC``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import ConnectionManeuverAssist_addGrpC
                    from private.osspy_der import ValueTracker
                    decval = ConnectionManeuverAssist_addGrpC.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'ConnectionManeuverAssist_addGrpC' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import ConnectionManeuverAssist_addGrpC
                    from private.osspy_per import ValueTracker
                    decval = ConnectionManeuverAssist_addGrpC.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'ConnectionManeuverAssist_addGrpC' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import ConnectionManeuverAssist_addGrpC
                    from private.osspy_oer import ValueTracker
                    decval = ConnectionManeuverAssist_addGrpC.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'ConnectionManeuverAssist_addGrpC' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``AddGrpC.ConnectionManeuverAssist_addGrpC``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import ConnectionManeuverAssist_addGrpC
                    ConnectionManeuverAssist_addGrpC.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'ConnectionManeuverAssist_addGrpC' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import ConnectionManeuverAssist_addGrpC
                    ConnectionManeuverAssist_addGrpC.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'ConnectionManeuverAssist_addGrpC' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import ConnectionManeuverAssist_addGrpC
                    ConnectionManeuverAssist_addGrpC.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'ConnectionManeuverAssist_addGrpC' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class IntersectionState_addGrpC:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``AddGrpC.IntersectionState_addGrpC`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import IntersectionState_addGrpC
                    from private.osspy_der import ValueTracker
                    return IntersectionState_addGrpC.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'IntersectionState_addGrpC' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import IntersectionState_addGrpC
                    from private.osspy_per import ValueTracker
                    return IntersectionState_addGrpC.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'IntersectionState_addGrpC' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import IntersectionState_addGrpC
                    from private.osspy_oer import ValueTracker
                    return IntersectionState_addGrpC.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'IntersectionState_addGrpC' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``AddGrpC.IntersectionState_addGrpC``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import IntersectionState_addGrpC
                    from private.osspy_der import ValueTracker
                    decval = IntersectionState_addGrpC.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'IntersectionState_addGrpC' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import IntersectionState_addGrpC
                    from private.osspy_per import ValueTracker
                    decval = IntersectionState_addGrpC.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'IntersectionState_addGrpC' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import IntersectionState_addGrpC
                    from private.osspy_oer import ValueTracker
                    decval = IntersectionState_addGrpC.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'IntersectionState_addGrpC' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``AddGrpC.IntersectionState_addGrpC``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import IntersectionState_addGrpC
                    IntersectionState_addGrpC.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'IntersectionState_addGrpC' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import IntersectionState_addGrpC
                    IntersectionState_addGrpC.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'IntersectionState_addGrpC' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import IntersectionState_addGrpC
                    IntersectionState_addGrpC.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'IntersectionState_addGrpC' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class MapData_addGrpC:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``AddGrpC.MapData_addGrpC`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import MapData_addGrpC
                    from private.osspy_der import ValueTracker
                    return MapData_addGrpC.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'MapData_addGrpC' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import MapData_addGrpC
                    from private.osspy_per import ValueTracker
                    return MapData_addGrpC.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'MapData_addGrpC' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import MapData_addGrpC
                    from private.osspy_oer import ValueTracker
                    return MapData_addGrpC.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'MapData_addGrpC' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``AddGrpC.MapData_addGrpC``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import MapData_addGrpC
                    from private.osspy_der import ValueTracker
                    decval = MapData_addGrpC.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'MapData_addGrpC' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import MapData_addGrpC
                    from private.osspy_per import ValueTracker
                    decval = MapData_addGrpC.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'MapData_addGrpC' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import MapData_addGrpC
                    from private.osspy_oer import ValueTracker
                    decval = MapData_addGrpC.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'MapData_addGrpC' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``AddGrpC.MapData_addGrpC``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import MapData_addGrpC
                    MapData_addGrpC.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'MapData_addGrpC' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import MapData_addGrpC
                    MapData_addGrpC.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'MapData_addGrpC' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import MapData_addGrpC
                    MapData_addGrpC.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'MapData_addGrpC' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class Position3D_addGrpC:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``AddGrpC.Position3D_addGrpC`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import Position3D_addGrpC
                    from private.osspy_der import ValueTracker
                    return Position3D_addGrpC.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'Position3D_addGrpC' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import Position3D_addGrpC
                    from private.osspy_per import ValueTracker
                    return Position3D_addGrpC.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'Position3D_addGrpC' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import Position3D_addGrpC
                    from private.osspy_oer import ValueTracker
                    return Position3D_addGrpC.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'Position3D_addGrpC' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``AddGrpC.Position3D_addGrpC``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import Position3D_addGrpC
                    from private.osspy_der import ValueTracker
                    decval = Position3D_addGrpC.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'Position3D_addGrpC' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import Position3D_addGrpC
                    from private.osspy_per import ValueTracker
                    decval = Position3D_addGrpC.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'Position3D_addGrpC' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import Position3D_addGrpC
                    from private.osspy_oer import ValueTracker
                    decval = Position3D_addGrpC.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'Position3D_addGrpC' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``AddGrpC.Position3D_addGrpC``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import Position3D_addGrpC
                    Position3D_addGrpC.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'Position3D_addGrpC' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import Position3D_addGrpC
                    Position3D_addGrpC.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'Position3D_addGrpC' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import Position3D_addGrpC
                    Position3D_addGrpC.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'Position3D_addGrpC' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

    class RestrictionUserType_addGrpC:
        @staticmethod
        def encode(encoding_rule: str, value: Union[dict, Any]) -> bytearray:
            ''' Encodes a value of type ``AddGrpC.RestrictionUserType_addGrpC`.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns the encoded values as ``bytearray``.
            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import RestrictionUserType_addGrpC
                    from private.osspy_der import ValueTracker
                    return RestrictionUserType_addGrpC.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'RestrictionUserType_addGrpC' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import RestrictionUserType_addGrpC
                    from private.osspy_per import ValueTracker
                    return RestrictionUserType_addGrpC.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'RestrictionUserType_addGrpC' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import RestrictionUserType_addGrpC
                    from private.osspy_oer import ValueTracker
                    return RestrictionUserType_addGrpC.encode(encoding_rule, value, ValueTracker()).get_buffer()
                except ImportError as exc:
                    raise ImportError("Could not load 'RestrictionUserType_addGrpC' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

        @staticmethod
        def decode(encoding_rule: str, stream: Union[bytearray, BufferedReader, BytesIO]):
            ''' Decodes a value of type ``AddGrpC.RestrictionUserType_addGrpC``.

                Supported encoding rules: ``"BER"|"DER"|"PER"|"UPER"|"CPER"|"CUPER"|"OER"|"COER"``.

                Accepts the input as ``bytearray``, ``io.BufferReader`` or ``io.BytesIO``.

                Returns decoded values as ``dict`` or ``primitive type``.

            '''
            encoding_rule = encoding_rule if encoding_rule is not None else 'UPER'

            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import RestrictionUserType_addGrpC
                    from private.osspy_der import ValueTracker
                    decval = RestrictionUserType_addGrpC.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'RestrictionUserType_addGrpC' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import RestrictionUserType_addGrpC
                    from private.osspy_per import ValueTracker
                    decval = RestrictionUserType_addGrpC.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'RestrictionUserType_addGrpC' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import RestrictionUserType_addGrpC
                    from private.osspy_oer import ValueTracker
                    decval = RestrictionUserType_addGrpC.decode(encoding_rule, stream, ValueTracker())
                except ImportError as exc:
                    raise ImportError("Could not load 'RestrictionUserType_addGrpC' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))
            return decval

        @staticmethod
        def validate(value: Union[dict, Any]) -> list:
            ''' Validates a value of type ``AddGrpC.RestrictionUserType_addGrpC``.

                Accepts the input value as ``dict`` or ``primitive type``.

                Returns a ``list`` of constraint violations (if any) or an empty list.
            '''
            errors = []

            encoding_rule: str = 'UPER'
            if (encoding_rule.upper() == "BER" or encoding_rule.upper() == "DER"):
                try:
                    from private.mycodec_der import RestrictionUserType_addGrpC
                    RestrictionUserType_addGrpC.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'RestrictionUserType_addGrpC' from 'private.mycodec_der' codec file") from exc
            elif (encoding_rule.upper() == "PER" or encoding_rule.upper() == "UPER" or
                    encoding_rule.upper() == "CPER" or encoding_rule.upper() == "CUPER"):
                try:
                    from private.mycodec_per import RestrictionUserType_addGrpC
                    RestrictionUserType_addGrpC.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'RestrictionUserType_addGrpC' from 'private.mycodec_per' codec file") from exc
            elif (encoding_rule.upper() == "OER" or encoding_rule.upper() == "COER"):
                try:
                    from private.mycodec_oer import RestrictionUserType_addGrpC
                    RestrictionUserType_addGrpC.validate(value, errors)
                    return errors
                except ImportError as exc:
                    raise ImportError("Could not load 'RestrictionUserType_addGrpC' from 'private.mycodec_oer' codec file") from exc
            else:
                raise ValueError('Unsupported or invalid {} encoding rule argument!'.format(encoding_rule))

DSRC.RegionId = AddGrpB.MsgCount
