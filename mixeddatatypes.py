def count_datatypes(list):
    type_count={"int":0,"bool":0,"float":0,"str":0}
    for i in list:
        if isinstance(i,bool):
            type_count["bool"]+=1
        elif isinstance(i,int):
            type_count["int"]+=1
        elif isinstance(i,float):
            type_count["float"]+=1
        elif isinstance(i,str):
            type_count["str"]+=1
    return type_count
mixed_list=[1,2,2.3,"rohith",False,0,5]
print(count_datatypes(mixed_list))