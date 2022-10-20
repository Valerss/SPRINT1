"""testing methods"""

__version__ = "0.1"

class Calculator:

    def sum(arg1: float, arg2: float) -> float:
        '''returns the sum of 2 floats for example:
        >>> Calculator.nroot(9,2)
        3.0'''
        return (arg1 + arg2)

    def subtraction(arg1: float, arg2: float) -> float:
        '''returns the difference of 2 floats for example:
        >>> Calculator.subtraction(9,4)
        5'''
        return (arg1 - arg2)

    def nroot(base: float, root: float) -> float:
        '''given a base and a root it returns the n^th root
        of the given base for example:
        >>> Calculator.nroot(9,2)
        3.0'''
        return (base**(1/(root)))

    memory = 0

    def delete(result: float) -> float:
        memory= 0
        return(memory)

if __name__=='__main__':
    import doctest
    print(doctest.testmod())


