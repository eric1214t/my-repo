def foo():
    print("Hello")
    try:
        x = 5/0
    except ZeroDivisionError:
        x = None
foo()
