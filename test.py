def foo():
    print("Hello")
    try:
        x = 9/0
    except ZeroDivisionError:
        x = None
foo()
