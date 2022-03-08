elem = 'O '
sor = [elem,elem,elem]
tarolo = [sor, sor, sor]
print (tarolo)
def rajzolas(): 
    for sor in tarolo: 
        for elem in sor: 
            print(elem, end='')
        if sor == xkord and elem == ykord:
            print('+ ', end ='')
        print()
xkord = int(input("add meg az x koordinátát "))
ykord = int(input("add meg az y koordinátát "))
rajzolas() 