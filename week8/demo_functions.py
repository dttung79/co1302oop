def add(a, b):
    c = a + b
    return c


def convert(n, c):
    if not isinstance(c, str):
        raise ValueError('c must be a string')
    
    if len(c) == 0 or len(c) > 1:
        raise ValueError('c must be a character')

    if not isinstance(n, int):
        raise ValueError('n must be an integer')
    
    if n == 0:
        return ''
    
    if n < 0:
        raise ValueError('n must be a positive integer')
        #return 'Error'
    
    if n > 25:
        return c * 25
    
    return c * n