def contar_ceros(*args):
    x=0
    for n in args:
        if x+1 == len(args):
            return False
        elif args[x]==0 and args[x+1]==0:
            return True
        else:
            pass
        x = x + 1

    return False

print(contar_ceros(0,7,4,9,9,0,6,4,0))