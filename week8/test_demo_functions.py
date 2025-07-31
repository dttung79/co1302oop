from demo_functions import add, convert

def test_add_01():
    a = 4
    b = 5
    expected = 9
    result = add(a, b)
    assert result == expected

def test_add_02():
    a = 4
    b = 0
    expected = 4
    result = add(a, b)
    assert result == expected


def test_convert_01():
    n = 5
    c = '*'
    expected = '*****'
    result = convert(n, c)
    assert result == expected

def test_convert_02():
    n = 5
    c = '+'
    expected = '+++++'
    result = convert(n, c)
    assert result == expected

def test_convert_03():
    n = 25
    c = '*'
    expected = '*************************'
    result = convert(n, c)
    assert result == expected

def test_convert_04():
    n = 26
    c = '*'
    expected = '*************************'
    result = convert(n, c)
    assert result == expected

def test_convert_05():
    n = 0
    c = '*'
    expected = ''
    result = convert(n, c)
    assert result == expected

def test_convert_06():
    n = -1
    c = '*'
    expected_message = 'n must be a positive integer'
    try:
        result = convert(n, c)
        # if no exception is raised, the test fails
        assert False
    except ValueError as e: # if ValueError is raised, code is correct
        assert str(e) == expected_message # but the error message must be correct

def test_convert_07():
    n = -100
    c = '*'
    expected_message = 'n must be a positive integer'
    try:
        result = convert(n, c)
        # if no exception is raised, the test fails
        assert False
    except ValueError as e: # if ValueError is raised, code is correct
        assert str(e) == expected_message # but the error message must be correct

def test_convert_08():
    n = 5
    c = ''
    expected_message = 'c must be a character'
    try:
        result = convert(n, c)
        # if no exception is raised, the test fails
        assert False
    except ValueError as e: # if ValueError is raised, code is correct
        assert str(e) == expected_message # but the error message must be correct

def test_convert_09():
    n = 5
    c = '++'
    expected_message = 'c must be a character'
    try:
        result = convert(n, c)
        # if no exception is raised, the test fails
        assert False
    except ValueError as e: # if ValueError is raised, code is correct
        assert str(e) == expected_message # but the error message must be correct

def test_convert_10():
    n = 50000000
    c = '*'
    expected = '*************************'
    result = convert(n, c)
    assert result == expected

def test_convert_11():
    n = 5.0
    c = '*'
    expected_message = 'n must be an integer'
    try:
        result = convert(n, c)
        # if no exception is raised, the test fails
        assert False
    except ValueError as e: # if ValueError is raised, code is correct
        assert str(e) == expected_message # but the error message must be correct