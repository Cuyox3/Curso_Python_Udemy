def palindromo (palabra:str)-> bool:
    """
    La función palindromo (palabra) recibe una palabra.
    Si la palabra es un palíndormo devuelve True, Si no False

    Un palíndromo es una palabra o frase que se lee igual 
    tanto de izquierda a derecha como derecha a izquierda

    >>> palindromo("radar")
    True
    >>> palindromo("somos")
    True
    >>> palindromo("holah")
    False
    >>> palindromo("Atar a la rata") #Tambien se toman los espacios
    True
    """

    if palabra.lower().replace(" ", "") == palabra.lower().replace(" ", "")[::-1]: 
        return True
    else:
        return False
    
if __name__=="__main__": 
    import doctest
    doctest.testmod()