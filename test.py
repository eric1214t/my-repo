def foo():
    print("Hello")
    try:
        x = 9/0
    except ZeroDivisionError:
        x = None
x = 8/0
foo()
