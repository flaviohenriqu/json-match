"""
    Json match
"""
import json


def match(expected, actual, debug=False):
    """
        Description:
            Looks up the hierarchy in 'expected' json within the 'actual' json.
        Required arguments:
            expected: a json represented as a string with
            the expected hierarchy to be found within 'actual'
            actual: the json represented as string on which the lookups
            will occur.
        Optional arguments:
            debug: If True print parameters values.
        Return value:
            If True value found, false otherwise.
    """
    if debug:
        print("Expected: %s" % expected)
        print("Actual: %s" % actual)

    # Extract both json strings.
    expected_json = json.loads(expected)
    actual_json = json.loads(actual)

    # check if the actual json is a list
    if isinstance(actual_json, list):
        # search the list of objects
        return _search_in_list(actual_json, expected_json)

    return _search_in_dict(actual_json, expected_json)


def _search_in_list(actual, expected):
    """
        Description:
            Search in structure list by the result expected
        Required arguments:
            actual: the json represented as string on which the lookups
            will occur.
            expected: a json represented as a string with
            the expected hierarchy to be found within 'actual'
        Optional arguments:
            None
        Return value:
            If True, json found in structure list, false otherwise.
    """
    found = None

    if isinstance(expected, list) and [item for item in expected if found or _search_in_list(actual, item)]:
        return True

    for item in actual:
        if isinstance(item, list):
            found = _search_in_list(item, expected)
        else:
            found = _search_in_dict(item, expected)

        if found:
            return True

    return found


def _search_in_dict(actual, expected):
    """
        Description:
            Search in dict by the result expected
        Required arguments:
            actual: the json represented as string on which the lookups
            will occur.
            expected: a json represented as a string with
            the expected hierarchy to be found within 'actual'
        Optional arguments:
            None
        Return value:
            If True, value found in dict, False otherwise.
    """
    found = None
    for key in actual:
        if key in expected:
            if found is None:
                found = (actual[key] == expected[key])
            else:
                found = found and (actual[key] == expected[key])

            if found:
                pass
            elif isinstance(actual[key], dict):
                found = _search_in_dict(actual[key], expected[key])
            elif isinstance(actual[key], list):
                found = _search_in_list(actual[key], expected[key])
            else:
                return actual[key] == expected[key]
    return found
