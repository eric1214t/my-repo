# hello.py
def foo():
    print("Hello")
    try:
        x = 9/0
    except:
        x = None
    return "ok"
x=5/0
# pytest 測試函式
def test_foo():
    assert foo() == "ok"
