def merge_dictionaries(dic1,dic2):
    return dic1|dic2
d1={'a':1,'b':2}
d2={'b':3,'d':4}
merge_dic=merge_dictionaries(d1,d2)
print(merge_dic)