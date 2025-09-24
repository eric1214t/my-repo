def foo():
    print("Hello")
    x =10/0  # <- 故意除以零，bandit 會檢查到
foo()
