import os

def foo():
    print("Hello")
    x =5/0  # <- 故意除以零，bandit 會檢查到
foo()
