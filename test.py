def foo():
    print("Hello")
    try:
        x = 6/0
    except ZeroDivisionError:
        x = None
foo()
