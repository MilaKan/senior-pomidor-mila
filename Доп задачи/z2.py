def same_elements(a , b):
    if a is None or b is None:
        return False
    if any(x is None for x in a) or any(y is None for y in b):
        return False
    if len(a) != len(b):
        return False
    if len(a) ==0 and len(b)==0:
        return True
    try:
        a_squared = [x**2 for x in a]
    except (TypeError, ValueError):
        return False
    a_sorted = sorted(a_squared)
    return a_sorted == sorted(b)

    """Если a и b 'одинаковые' вернуть True
    Если в a и b пустые списки[] вернуть True
    Если в a и b есть None вернуть False.
    Если в списке не одинаковое кол - во
    элементов вернутьFalse
    Входные данные:"""
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
b1 = [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
print(same_elements(a1, b1))
a2 = [121, 144, 19, 161, 19, 144, 19, 11]
b2 = [11 * 21, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
print(same_elements(a2, b2))
a3 = [121, 144, 19, 161, 19, 144, 19, 11]
b3 = [11 * 11, 121 * 121, 144 * 144, 190 * 190, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
print(same_elements(a3, b3))
a4 = []
b4 = []
print(same_elements(a4, b4))
a5 = None
b5 = [11 * 11, 121 * 121, 144 * 144, 19 * 19, 144 * 144, 19 * 19]
print(same_elements(a5, b5))
a6 = [121, 144, 19, 161, 19, 11]
b6 = []
print(same_elements(a6, b6))