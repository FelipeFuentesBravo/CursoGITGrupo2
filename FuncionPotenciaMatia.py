#Matia Cornejo
#Curso Git Grupo 2
#Este programa calcula potencias de numeros

#Funcion potencia:
#Entrada:Recibe dos numeros, la base y el exponente
#Salida:Entrega el resultado de la operacion
def potencia(base,exponente):
    contador=0
    acumulador=1
    if contador == exponente:
        return acumulador
    else:
        acumulador=base**exponente
        contador=contador+1
        return acumulador
#Funcion raiz:
#Entrada:Recibe dos numeros, la base y el numero de raiz
#Salida:Entrega el resultado de la operacion
def raiz(base,raiz):
    raiz=raiz*1.0
    raiz=1/raiz
    acumulador=base**raiz
    return acumulador


        
        
