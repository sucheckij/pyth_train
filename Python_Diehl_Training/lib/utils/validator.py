def isNumber(number):
    try:
        number = float(number)
        return True
    except Exception:
        return False
