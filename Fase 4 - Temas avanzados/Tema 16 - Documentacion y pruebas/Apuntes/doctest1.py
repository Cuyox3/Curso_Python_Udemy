def suma (a:int,b:int)-> int : 
    """
    La función de suma (a,b) recibe dos paámetros a y b 
    Devuelve la suma de ambos

    >>> suma (5,10)
    15
    >>> suma (0,0)
    0
    >>> suma (-5,7)
    2

    Podemos sumar letras
    >>> sumar ('aa'+'bb')
    'abb'

    O listas 

    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    [1, 2, 3, 4, 5, 6]

    Sumar distintos tipos:

    >>> suma(10,'hola')
    Traceback (most recent call last):
      ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """
    return a+b

if __name__ == "__main__":
    import doctest
    doctest.testmod()