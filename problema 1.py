def devolver_distintos(num1,num2,num3):
    lista_suma=[num1,num2,num3]
    if sum(lista_suma)>15:
        return max(lista_suma)
    elif sum(lista_suma)<10:
        return min(lista_suma)
    elif sum(lista_suma)>=10 and sum(lista_suma) <=15:
        if lista_suma[0]>=lista_suma[1] and lista_suma[1]>=lista_suma[2]:
            return lista_suma[1]
        elif lista_suma[0]>=lista_suma[2] and lista_suma[2]>=lista_suma[1]:
            return lista_suma[2]
        elif lista_suma[1]>=lista_suma[0] and lista_suma[0]>=lista_suma[2]:
            return lista_suma[0]
        elif lista_suma[1]>=lista_suma[2] and lista_suma[2]>=lista_suma[1]:
            return lista_suma[2]
        elif lista_suma[2]>=lista_suma[0] and lista_suma[0]>=lista_suma[1]:
            return lista_suma[0]
        elif lista_suma[2]>=lista_suma[1] and lista_suma[1]>=lista_suma[0]:
            return lista_suma[1]

print(devolver_distintos(5,9,6))
