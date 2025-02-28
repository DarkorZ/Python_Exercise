#Ejercicio, script python que asigne como area de codigo a los 3 primeros numeros, y los 3 posteriores haga un espacio
number='2025551212'
def formatohora(number): #FUNCION QUE TRANSFORMARA EN FORMATO telefono UN NUMERO
    code="("+number[0:3]+")"    #asingamos un index que seleccione los 3 primeros dijistos y una los strings con parentesis 
    format=number[3:6]+"-"      #asignamos un los 3 posteriors numeros y unimos a un = para el formato numero
    separador=number[-4:] # asiganmos los ultimos numeros despues del separador

    number=(str(code)+str(format)+str(separador)) #unimos strings
    return number #retornamos el valor final

print(formatohora(str(number))) #ejecutamos funcion