#************************************************************
#   Copyright (C) 2023 OSS Nokalva, Inc.  All rights reserved.
#************************************************************

#   THIS FILE IS PROPRIETARY MATERIAL OF OSS NOKALVA, INC.
#   AND MAY BE USED AND DISTRIBUTED ONLY BY DIRECT LICENSEES OF OSS NOKALVA, INC.
#   THIS COPYRIGHT STATEMENT MAY NOT BE REMOVED.

#   Python 3.7 or higher is required!

#   This file was generated for 'Syed Kamal' by 'https://asn1.io/ASN1-Python-Compiler/' at '5/1/2024 2:38:09 PM'

from cmath import isnan
from typing import Any
from decimal import Decimal
from enum import Enum
from datetime import datetime
import re

class Asn1Type(Enum):
    INTEGER = 0,
    REAL = 1,
    BOOLEAN = 2,
    ENUMERATED = 3,
    String = 4,
    NULL = 5,
    OID	= 6,
    IRI = 7,
    GeneralizedTime = 8,
    UTCTime = 9,
    TIME = 10,
    BIT_STRING = 11,
    OCTET_STRING = 12,
    OpenType = 13,
    SEQUENCE_OF = 14,
    SEQUENCE = 15,
    CHOICE = 16,
    CHARACTER_STRING = 17,
    EMBEDDED_PDV = 18,
    EXTERNAL = 19,
    INSTANCE_OF = 20

def report_empty_value(value: Any, type_name: str, errors: list, comp_path: str) -> None:
    errors.append({
        'field reference': comp_path,
        'field value': value,
        'violations': [{
            'type': 'unexpected empty \'value\' for {}'.format(type_name)
        }]
    })

def report_missing_field(type_name: str, identifier: str, errors: list, comp_path: str) -> None:
    errors.append({
        'field reference': '{}/{}'.format(comp_path, identifier),
        'violations': [{
            'type': 'missing field \'{}\' in \'{}\''.format(identifier, type_name)
        }]
    })

def report_extra_field(value: Any, type_name: str, identifier: str, errors: list, comp_path: str, permitted_identifiers: list) -> None:
    errors.append( {
        'field reference': comp_path,
        'field value': value,
        'violations': [{
            'type': 'unexpected extra component \'{}\' in \'{}\''.format(identifier, type_name),
            'permitted': permitted_identifiers
        }]
    })

def validate_value_type(value: Any, component_path: str, errors: list, asn1Type: Asn1Type):
    if (asn1Type is Asn1Type.INTEGER):
        if (not isinstance(value, int)):
            try:
                _ = int(value)
            except Exception as _:
                __report_mismatching_type(value, component_path, errors, "'int' or compatible numeric value")
    elif (asn1Type is Asn1Type.REAL):
        if (not isinstance(value, Decimal) and not isinstance(value, float) and not isinstance(value, int)):
            try:
                _ = float(value)
            except Exception as _:
                if (isinstance(value, str)):
                    if (value.upper() != "INF" and value.upper() != "-INF" and value != "-0" and value != "0" and value.upper() != "NAN"):
                        __report_mismatching_type(value, component_path, errors, "'str' allowed only for special REAL values {}".format(["0", "-0", "INF", "-INF"]))
                elif (isinstance(value, dict)):
                    if ('base10Value' not in value):
                        if ("mantissa" not in value or "exponent" not in value or "base" not in value ):
                            __report_mismatching_type(value, component_path, errors, "'dict' value must contain all the following fields: 'mantissa', 'base', 'exponent'")
                else:
                    __report_mismatching_type(value, component_path, errors, "'float' or compatible floating point value")
    elif (asn1Type is Asn1Type.String):
        if (not isinstance(value, str)):
            try:
                _ = str(value)
            except Exception as _:
                __report_mismatching_type(value, component_path, errors, "'str' or compatible string value")
    elif (asn1Type is Asn1Type.BOOLEAN):
        if (not isinstance(value, bool)):
            try:
                _ = bool(value)
            except Exception as _:
                __report_mismatching_type(value, component_path, errors, "'bool' or compatible boolean value")
    elif (asn1Type is Asn1Type.ENUMERATED):
        if (not isinstance(value, str) and not isinstance(value, int)):
            try:
                _ = int(value)
            except Exception as _:
                __report_mismatching_type(value, component_path, errors, "'str' compatible identifiers or 'int' values")
    elif (asn1Type is Asn1Type.GeneralizedTime or asn1Type is Asn1Type.UTCTime):
        if (not isinstance(value, str) and not isinstance(value, datetime)):
            try:
                _ = str(value)
            except Exception as _:
                __report_mismatching_type(value, component_path, errors, "'datetime' or compatible time values")
    elif (asn1Type is Asn1Type.OID or asn1Type is Asn1Type.IRI):
        if (not isinstance(value, str)):
            try:
                _ = str(value)
            except Exception as _:
                __report_mismatching_type(value, component_path, errors, "numeric separated OID values as a 'str'")
    elif (asn1Type is Asn1Type.BIT_STRING):
        if (isinstance(value, str)):
            try:
                if (len(value) > 0 and value[-1] != 'B'):
                    _ = bytearray.fromhex(value)
            except Exception as _:
                __report_mismatching_type(value, component_path, errors, "valid hexadecimal 'str' value")
        elif (isinstance(value, dict)):
            if ("containing" in value):
                pass
            elif ("length" in value and "value" in value):
                try:
                    _ = bytearray.fromhex(value["value"])
                except _:
                    __report_mismatching_type(value, component_path, errors, "valid hexadecimal 'str' value")
            else:
                __report_mismatching_type(value, component_path, errors, "valid hexadecimal 'str' value")
        else:
            __report_mismatching_type(value, component_path, errors, "valid hexadecimal 'str' value")
    elif (asn1Type is Asn1Type.OCTET_STRING):
        if (isinstance(value, str)):
            try:
                if (len(value) > 0 and value[-1] != 'H'):
                    _ = bytearray.fromhex(value)
            except _:
                __report_mismatching_type(value, component_path, errors, "valid hexadecimal 'str' value")
        elif (isinstance (value, dict) and "containing" in value):
            pass
        else:
            __report_mismatching_type(value, component_path, errors, "valid hexadecimal 'str' value")
    elif (asn1Type is Asn1Type.SEQUENCE_OF):
        if (not isinstance(value, list) and not isinstance(value, set)):
            __report_mismatching_type(value, component_path, errors, "'list' or 'set' of values")
    elif (asn1Type is Asn1Type.SEQUENCE or asn1Type is Asn1Type.CHOICE):
        if (not isinstance(value, dict)):
            __report_mismatching_type(value, component_path, errors, "constructed type as 'dict'")
    elif (asn1Type is Asn1Type.CHARACTER_STRING or asn1Type is Asn1Type.EXTERNAL or asn1Type is Asn1Type.EMBEDDED_PDV):
        if (not isinstance(value, dict)):
            __report_mismatching_type(value, component_path, errors, "presentation context switching type as 'dict'")
    elif (asn1Type is Asn1Type.INSTANCE_OF):
        if (not isinstance(value, dict)):
            __report_mismatching_type(value, component_path, errors, "INSTANCE OF type as 'dict'")

def validate_value(value: Any, constraints: dict, component_path: str, errors: list) -> bool:
    tmp_errors = []
    for constraint in constraints:
        if (not "type" in constraint):
            continue
        elif (constraint["type"] == "subtype constraint"):
            __validate_subtype_constraint(value, constraint, component_path, tmp_errors)
        elif (constraint["type"] == "single value"):
            __validate_single_value_constrait(value, constraint, tmp_errors)
        elif (constraint["type"] == "value range"):
            __validate_value_range_constraint(value, constraint, tmp_errors)
        elif (constraint["type"] == "size constraint"):
            __validate_size_constraint(value, constraint, tmp_errors)
        elif (constraint["type"] == "alphabet constraint"):
            __validate_alphabet_constraint(value, constraint, tmp_errors)
        elif (constraint["type"] == "inner type constraint"):
            __validate_inner_type_constraint(value, constraint, tmp_errors)
        elif (constraint["type"] == "pattern" and isinstance(value, str)):
            __validate_pattern_constraint(value, constraint, tmp_errors)
        elif (constraint["type"] == "constraint union"):
            __validate_constraint_union(value, constraint, tmp_errors)
        elif (constraint["type"] == "constraint intersection"):
            __validate_constraint_intersection(value, constraint, tmp_errors)
        elif (constraint["type"] == "constraint difference"):
            __validate_constraint_difference(value, constraint, tmp_errors)
        elif (constraint["type"] == "constraint complement"):
            __validate_constraint_complement(value, constraint, tmp_errors)
        elif (constraint["type"] == "contained subtype constraint"):
            __validate_contained_subtype_constraint(value, constraint, tmp_errors)
        elif (constraint["type"] == "type constraint"):
            __validate_type_constraint(value, constraint, tmp_errors)
        elif (constraint["type"] == "simple table constraint"):
            __validate_simple_table_constraint(value, constraint, tmp_errors)
        elif (constraint["type"] == "contents constraint"):
            __validate_contents_constraint(value, constraint, tmp_errors)
        elif (constraint["type"] == "component relation constraint"):
            __validate_component_relation_constraint()

    if (len(tmp_errors) > 0):
        errors.append({
            "field reference": component_path,
            "field value": value,
            "violations": tmp_errors })
        return False

    return True

def __validate_subtype_constraint(value: Any, constraint: dict, component_path: str, errors: list) -> bool:
    tmp_errors = []
    if ("root expression" in constraint):
        root = constraint["root expression"]
        if (len(root) > 0 and validate_value(value, [root], component_path, tmp_errors)):
            return True

    if ("extension expression" in constraint):
        extension = constraint["extension expression"]
        if (validate_value(len(extension) > 0 and value, [extension], component_path, tmp_errors)):
            return True

    for error in tmp_errors:
        if ("violations" in error):
            errors.append(error["violations"])

    return False

def __validate_single_value_constrait(value: Any, constraint: dict, errors: list) -> bool:
    if ("permitted" in constraint and constraint["permitted"] is not None):
        if (value != constraint["permitted"]):
            errors.append(__build_violation_report(constraint))
            return False

    return True

def __validate_value_range_constraint(value: Any, constraint: dict, errors: list) -> bool:
    if ("permitted" in constraint):
        permitted = constraint["permitted"]

        value2 = value
        if (isinstance(value, str) and value == "-INF"):
            value2 = float("-inf")
        elif (isinstance(value, str) and value == "INF"):
            value2 = float("inf")
        elif (isinstance(value, str) and value == "0"):
            value2 = float(0)
        elif (isinstance(value, str) and value == "-0"):
            value2 = float(-0.0)
        elif (isinstance(value, str) and value == "NaN"):
            value2 = float("nan")
        elif(isinstance(value, str)):
            return True
        elif (isinstance(value, dict)):
            report = __build_violation_report(constraint)
            errors.append(report)
            return False

        for rng in permitted:
            lower, upper = rng

            if (isnan(value2)):
                if (isnan(lower) or isnan(upper)):
                    return True
                else:
                    break
            elif (lower == float("-inf") and value2 <= upper):
                return True
            elif(upper == float("inf") and value2 >= lower):
                return True
            elif (value2 >= lower and value2 <= upper):
                return True

        report = __build_violation_report(constraint)
        errors.append(report)

    return False

def __validate_size_constraint(value: Any, constraint: dict, errors: list) -> bool:
    if "permitted" in constraint:
        permitted = constraint["permitted"]

        for rng in permitted:
            _min, _max = rng
            length = float("inf")

            if isinstance(value, str):
                length = len(value)
                if ("isOctetString" in constraint and constraint["isOctetString"]):
                    length = length // 2
                elif ("isBitString" in constraint and constraint["isBitString"]):
                    length = length * 4
            elif isinstance(value, int):
                length = value
            elif isinstance(value, list):
                length = len(value)
            elif isinstance(value, dict):
                if "length" in value:
                    length = value["length"]

            if (length >= _min and length <= _max):
                return True

        report = __build_violation_report(constraint, ["type", "definition", "permitted"])
        errors.append(report)

    return False

def __validate_alphabet_constraint(value: str, constraint: dict, errors: list) -> bool:
    if ("permitted" in constraint):
        permitted = constraint["permitted"]

        offending_chars = __validate_codepoint_ranges(value, permitted)

        if (len(offending_chars) > 0):
            report = __build_violation_report(constraint, ["type", "definition"])
            report["prohobited"] = ''.join(offending_chars)
            errors.append(report)
            return False

    return True

def __validate_pattern_constraint(value: str, constraint: dict, errors: list):
    if ("expression" in constraint):
        try:
            if re.fullmatch(constraint["expression"], value) is None:
                report = __build_violation_report(constraint, ["type", "definition"])
                errors.append(report)
                return False
        except Exception:
            return True

    return True

def __validate_constraint_union(value: Any, constraint: dict, errors: list) -> bool:
    if "constraints" in constraint:
        constraints = constraint["constraints"]
        local_errors = []

        for c in constraints:
            if (validate_value(value, [c], None, local_errors)):
                return True

        report = __build_violation_report(constraint, ["type", "definition"])
        errors.append(report)
    
    return False

def __validate_constraint_intersection(value: Any, constraint: dict, errors: list) -> bool:
    if ("constraints" in constraint):
        constraints = constraint["constraints"]
        local_errors = []

        for c in constraints:
            if (not validate_value(value, [c], None, local_errors)):
                report = __build_violation_report(constraint, ["type", "definition"])
                errors.append(report)
                return False
        
    return True

def __validate_constraint_difference(value: Any, constraint: dict, errors: list) -> bool:
    if ("constraints" in constraint):
        constraints = constraint["constraints"]
        local_errors = []

        if (len(constraints) == 2):
            if (not validate_value(value, [constraints[0]], None, local_errors)):
                report = __build_violation_report(constraint, ["type", "definition"])
                errors.append(report)
                return False
            
            if (validate_value(value, [constraints[1]], None, local_errors)):
                report = __build_violation_report(constraint, ["type", "definition"])
                errors.append(report)
                return False

    return False

def __validate_constraint_complement(value: Any, constraint: dict, errors: list) -> bool:
    if ("constraints" in constraint):
        constraints = constraint["constraints"]

        if (validate_value(value, [constraints], None, [])):
            report = __build_violation_report(constraint, ["type", "definition"])
            errors.append(report)
            return False
    
    return True

def __validate_contained_subtype_constraint(value: Any, constraint: dict, errors: list) -> bool:
    if ("constraints" in constraint):
        constraints = constraint["constraints"]

        if (not validate_value(value, constraints, None, [])):
            report = __build_violation_report(constraint, ["type", "definition"])
            errors.append(report)
            return False

    return True

def __validate_type_constraint(value: Any, constraint: dict, errors: list) -> bool:
    if ("constraints" in constraint):
        constraints = constraint["constraints"]

        if (not validate_value(value, constraints, None, [])):
            report = __build_violation_report(constraint, ["type", "definition"])
            errors.append(report)
            return False

    return True

def __validate_inner_type_constraint(value: Any, constraint: dict, errors: list) -> bool:
    for component in constraint["components"]:
        for key in component:
            if ("status" in component[key] and component[key]["status"] == "PRESENT" and key not in value):
                report = __build_violation_report(constraint, ["type", "definition"])
                report[key] = component[key]
                errors.append(report)
                return False
            elif ("status" in component[key] and component[key]["status"] == "ABSENT" and key in value):
                report = __build_violation_report(constraint, ["type", "definition"])
                report[key] = component[key]
                errors.append(report)
                return False
            elif ("constraint" in component[key]):
                innerConstr = component[key]["constraint"]
                mantissa, base, exponent = None, None, None
                if (isinstance(value, str)): #special real
                    report = __build_violation_report(constraint, ["type", "definition"])
                    report["permitted"] = "Special Real values are prohibited"
                    errors.append(report)
                    return False

                if (isinstance(value, float)): #base10
                    base = 10
                    sign, digits, exponent = Decimal(str(value)).as_tuple()
                    mantissa = int(''.join(map(str, digits)))
                    if (sign != 0):
                        mantissa = -abs(mantissa)
                elif (isinstance(value, dict)): #base2
                    if "base" in value:
                        base = value["base"]	
                    if "mantissa" in value:
                        mantissa = value["mantissa"]
                    if "exponent" in value:
                        exponent = value["exponent"]
                else:
                    return True

                fragment = None
                if key == "base":
                    fragment = base
                elif key == "mantissa":
                    fragment = mantissa
                elif key == "exponent":
                    fragment = exponent

                if (not validate_value(fragment, [innerConstr], None, [])):
                    report = __build_violation_report(constraint, ["type", "definition"])
                    report[key] = fragment
                    if ("permitted" in innerConstr):
                        report["permitted"] = innerConstr["permitted"]
                    errors.append(report)
                    return False
    return True

def __validate_simple_table_constraint(value: Any, constraint: dict, errors: list) -> bool:
    if ("isExtensible" in constraint and constraint["isExtensible"]):
        return True

    if ("fields" in constraint):
        fields = constraint["fields"]
        if (not validate_value(value, [fields], None, [])):
            report = __build_violation_report(constraint, ["type", "definition"])
            errors.append(report)
            return False
    elif ("entities" in constraint):
        entities = constraint["entities"]
        for entity in entities:
            if (entity[0] == "type" or entity[0] == "braced value set"):
                fn = getattr(entity[1], "validate")
                errors2 = []
                fn(value, errors2)

                if (len(errors2) > 0):
                    for error in errors2:
                        errors.append(error)
                return False
            elif (entity[0] == "value"):
                if (value is not None and entity[1] != value):
                    report = __build_violation_report(constraint, ["type", "definition"])
                    report["permitted"] = entity[1]
                    errors.append(report)
                    return False
            else:
                if (value is not None and entity[0] != value):
                    report = __build_violation_report(constraint, ["type", "definition"])
                    report["permitted"] = entity[0]
                    errors.append(report)
                    return False
                
                fn = getattr(entity[1], "validate")
                errors2 = []
                fn(value, errors2)

                if (len(errors2) > 0):
                    for error in errors2:
                        errors.append(error)
                return False	

    return True

def __validate_contents_constraint(value: Any, constraint: dict, errors: list) -> bool:
    if (isinstance(value, dict) and "containing" in value):
        if ("value" in constraint):
            fn = getattr(constraint["value"], "validate")
            if (value.get("containing") != None):
                local_errs = []
                fn(value["containing"], local_errs)

                if (len(local_errs) > 0):
                    report = __build_violation_report(constraint, ["type", "definition"])
                    report["violations"] = local_errs
                    errors.append(report)
                    return False
    return True

def __validate_component_relation_constraint() -> bool:
    return True

def __validate_codepoint_ranges(value: str, code_ranges: list) -> list:
    offending_chars = []

    for ch in str(value):
        is_valid = any(ord(ch) in range(code_range[0], code_range[1] + 1) for code_range in code_ranges)
        if (not is_valid):
            offending_chars.append(ch)

    return offending_chars

def __build_violation_report(constraint: dict, keys: list = None) -> dict:
    report = {}
    for key in constraint:
        if (keys is not None and key in keys):
            report[key] = constraint[key]
        elif (keys is None):
            report[key] = constraint[key]
    return report

def __report_mismatching_type(value: Any, component_path: str, errors: list, violations: str):
    errors.append({
        "field reference": component_path,
        "field value": value,
        "field type": type(value),
        "violations": {
            "type": "wrong value type",
            "permitted": violations
        }})