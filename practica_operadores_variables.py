>>> 123 + 222 = #345
>>> 1.5 * 4 = #6.0
>>> 2 ** 100 = #1267650600228229401496703205376
>>> len(893) = #TypeError: object of type 'int' has no len()
>>> len("893") = #3
>>> len([2, 3, 4, 5]) = #4
>>> len(str(2 ** 1000000)) = #ValueError: Exceeds the limit (4300) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
>>> import math = #Importa la libreria Math
>>> Math.pi = #NameError: name 'Math' is not defined
>>> math.sqrt(85) = #9.219544457292887
>>> import random = #implementa generadores de números pseudoaleatorios para varias distribuciones
>>> random.random() = #0.6515005670431295
>>> random.choice([1, 2, 3, 4]) = #2
>>> st = 'Spam' = #None
>>> len(st) = #4
>>> st[0] = #'S'
>>> st[-1] = #'m'
>>> st[1:3] = #'pa'
>>> st[1:] = #'pam'
>>> st[:] = #'Spam'
>>> st + "Hola" = #'SpamHola'
>>> st * 5 = #'SpamSpamSpamSpamSpam'
>>> st[0] = 'z' = #TypeError: 'str' object does not support item assignment
>>> st = 'z' + st[1:] = #None
>>> print(st) = #zpam

# Transformar string a lista:
>>> S = 'shrubbery' = #'shrubbery'
>>> L = list(S) = #['s', 'h', 'r', 'u', 'b', 'b', 'e', 'r', 'y']
>>> L = #['s', 'h', 'r', 'u', 'b', 'b', 'e', 'r', 'y']
>>> L[1] = 'c' = #None
>>> ''.join(L) = #'scrubbery'
>>> B = bytearray(b'spam') = #bytearray(b'spam')
>>> B.extend(b'eggs') = #bytearray(b'spameggs')
>>> B= #bytearray(b'spameggs')
>>> B.decode() = #'spameggs'

#Métodos especiales para strings:
>>> S = 'Spam' = #'Spam'
>>> S.find('pa') = #1
>>> S = #'Spam'
>>> S.replace('pa', 'XYZ') = #'SXYZm'
>>> S = #'Spam'

>>> line = 'aaa,bbb,ccccc,dd' = #'aaa,bbb,ccccc,dd'
>>> line.split(',') = #['aaa', 'bbb', 'ccccc', 'dd']
>>> S = 'spam' = #'spam'
>>> S.upper()  = #'SPAM'
>>> S.isalpha()  = #True
>>> line = 'aaa,bbb,ccccc,dd\n' = #'aaa,bbb,ccccc,dd\n'
>>> line.rstrip() = #'aaa,bbb,ccccc,dd'
>>> line.rstrip().split(',') = #['aaa', 'bbb', 'ccccc', 'dd']

#Plantillas para strings:
>>> '%s, eggs, and %s' % ('spam', 'SPAM!')  = #'spam, eggs, and SPAM!'
>>> '{0}, eggs, and {1}'.format('spam', 'SPAM!') = #'spam, eggs, and SPAM!'
>>> '{}, eggs, and {}'.format('spam', 'SPAM!')  = #'spam, eggs, and SPAM!'
>>> f'{S}, eggs, and {line}' = #'spam, eggs, and aaa,bbb,ccccc,dd\n'

#Visualizar los métodos de un objecto:
>>> dir(S) = #['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(S.replace) = #Help on built-in function replace:
>>> S = 'A\nB\tC' = #'A\nB\tC'
>>> len(S) = #5
>>> ord('\n') = #10
>>> S = 'A\0B\0C' = #'A\x00B\x00C'
>>> len(S) = #5
>>> S = #'A\x00B\x00C'
>>> msg = #SyntaxError: invalid syntax

Entradas de usuario:
>>> color = input("Introduce el color de tu camisa?: ") = #Introduce el color de tu camisa?: Gris
>>> print(color) = #Gris
>>> n = int(input("Cuantas camisas tienes?: ")) = #Cuantas camisas tienes?: 13
>>> print(n) = #13
>>> price = float(input("Cuanto costo la mas bonita?: ")) = #Cuanto costo la mas bonita?: 500
>>> print(price) = #500.0