def safe_div(a, b):
    return a / b if b != 0 else None

print(safe_div(10, 2))