def IntToListInt(arv:int)->list:
    """
    """
    arv=list(str(arv))
    for i in range(len(arv)):
        arv[i]=int(arv[i])
    return arv

def CountNumber(arv:int):
    """
    """
    for i in range(10):
        if not(str(arv).count(str(i))<=0):
            print(str(arv).count(str(i))*str(i))
        else:
            print("Нет",i)