def foo():
    print("Hello")
    try:
        x = 9/0
    except:
        x = None
#x = 8/0
foo()
