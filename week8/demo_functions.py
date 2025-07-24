def add(a, b):
    c = a + b
    return c


def convert(n, c):
    if not isinstance(c, str):
        return 'Error'
    
    if len(c) == 0 or len(c) > 1:
        return 'Error'

    if not isinstance(n, int):
        return 'Error'
    
    if n == 0:
        return ''
    
    if n < 0:
        return 'Error'
    
    if n > 25:
        return c * 25
    
    return c * n