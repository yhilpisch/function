# coding: utf-8
def f(x):
    ''' Function to compute the square of a number.
    
    Parameters
    ==========
    x: float
        input number
    
    Returns
    =======
    y: float
        (positive) output number
        
    Raises
    ======
    TypeError if x is neither int or float
    '''
    if type(x) not in [int, float]:
        raise TypeError('Parameter must be integer or float.')
    y = x ** 2
    return y
