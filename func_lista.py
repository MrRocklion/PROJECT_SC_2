prueba1 = [[1,2,3,4,5,6],[7,8,9,10],[11,'a','b','c']]
prueba2 = 108
prueba3 = ([1, 2, ['a', 'b'], [10]])
prueba4 = [[1,2,[3]],[4]]
prueba5 = [[[1]],2,[[[[3]]]],[[[[[[[[[[[[[[8]]]]]]]]]]]]]]]

def tipo_lista(lista):
    nueva_lista = []
    if type(lista) == type(nueva_lista):
        for i in range(len(lista)):
            if type(lista[i]) == type(nueva_lista):
                for j in range(len(lista[i])):
                    nueva_lista.append(lista[i][j])
            else:
                nueva_lista.append(lista[i])

        return  nueva_lista
    else:
        return None
def funcion_final(lista):
    prueba = lista
    if type(lista) == type([]):
        for i in range(100):
            prueba = tipo_lista(prueba)
            for i in range(len(prueba)):
                if type(prueba[i]) == type([]):
                    prueba = tipo_lista(prueba)
                    if(prueba)== None:
                        return None
        return prueba
    else:
        return None



print(funcion_final(prueba5))
print('termino')





