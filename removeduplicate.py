def remove_duplicate(p):
    w=[]
    for i in p:
        if i not in w:
            w.append(i)
    return w
p=[1,1,2,3,4,4,7]
print(remove_duplicate(p))