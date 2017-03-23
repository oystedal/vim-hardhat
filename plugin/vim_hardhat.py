import re

test_case_re = re.compile(r"^\s*TEST_CASE\s*\((?P<test_name>[^,\)\s]+),?.*\)\s*\{?\s*$")
test_case_with_base_re = re.compile(r"^\s*TEST_CASE_WITH_BASE\s*\([^,]+,\s*(?P<test_name>[^,\)\s]+),?.*\)\s*\{?\s*$")

def find_test_case_name(line):
    m = test_case_re.match(line)
    if m:
        return m.group("test_name")
    m = test_case_with_base_re.match(line)
    if m:
        return m.group("test_name")
    return None

def find_test_case_under_cursor(lines):
    lineno = len(lines) - 1
    while lineno >= 0:
        test_name = find_test_case_name(lines[lineno])
        if test_name:
            return test_name
        lineno -= 1

    return None
