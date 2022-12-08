def liczby(c, *cyfry):
    suma = 0
    count = len(cyfry)
    print(c)
    print(cyfry)
    print(type(cyfry))
    for i in cyfry:
        suma += i
        print(i)
    print(suma / count)


# liczby(5)
# liczby(5, 4, 43, 7)
# liczby(43, 7)
# liczby()


def connect(**opcje):
    conn_param = {
        'host': '127.0.0.7',
        'port': '8080',
        'user': 'admin',
        'pass': '123456'
    }
    conn_param['pwd'] = opcje
    print(conn_param)
    print(opcje)


connect()
# connect("radek")
connect(root='/')


def wypisz_1(a, b, c):
    print(f"a={a} b={b} c={c}")


def wypisz_2(a, b, /, c):
    print(f"a={a} b={b} c={c}")


wypisz_1(c=1, a=2, b=3)
wypisz_1(1, 2, 3)
wypisz_1(1, 2, c=3)
wypisz_2(1, 2, 3)
wypisz_2(1, 2, c=3)


def allparams(a, b, /, c=42, *args, d=256, e, **kwargs):
    print('a, b, c:', a, b, c)
    print('d,e:', d, e)
    print('args:', args)
    print('kwargs:', kwargs)


allparams(2, 6, 7, 8, 9, 10, e=10, f=11)
allparams(2, 6, 7, 8, 9, 10, e=20, f=11, g=12)
allparams(2, 6, 7, args=(8, 9, 10), e=20, f=11, g=12)
