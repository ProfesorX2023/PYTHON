def contar_primos(numero):

    for k in range(2,numero):
        for n in range(2,k):
            if k%n==0:
                print(" No Es primo", k)

        print(" Es primo", k)



print(contar_primos(8))