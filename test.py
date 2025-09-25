"""Example module for testing pylint in GitHub Actions."""

def safe_division():
    """Return 'ok' even if division by zero occurs."""
    print("Hello")
    try:
        _ = 9 / 0
    except ZeroDivisionError:
        _ = None
    return "ok"

def test_safe_division():
    """Test that safe_division returns ok.."""
    assert safe_division() == "ok"
    x=8/0

#print(10/0)