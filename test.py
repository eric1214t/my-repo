def foo():
    print("Hello")
    try:
        x = 10/0
    except ZeroDivisionError:
        x = None
foo()
