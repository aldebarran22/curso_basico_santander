"""
Control de excepciones en python
"""


def test1():
    try:
        L = [1,2,3,4,5]
        print(L[30])
        print('fin')
    except IndexError as e:
        print(e.__class__.__name__, e)
    

def test2():
    try:
        L = [1,2,3,4,5]
        d = {"a": 1, "b": 2, "c": 3}
        print(d['a'])
        print(L[30])
        print('fin')
    except (IndexError,KeyError) as e:
        print(e.__class__.__name__, e)

if __name__ == "__main__":
    test2()
