def sett(x,y):
    set_lst = set(x) & set(y)
    return set_lst

print(sett(["a","b","c","f"], ["b","c","d","g"]))