# Prueba tecnica de 160K

# Tengo un imput en cadena de texto
# y un array de longitud indeterminada inicialmente inicializado a 0
# Si leo un 1 me muevo a la derecha
# Si leo un 2 me muevo a la izauierda
# Si leo un 3 sumo 1 a mi posicion actual
# Si leo un 4 resto 1 a mi posicion actual
# Si leo un (  y mi valor actual en el array es 0 me muevo a la derecha hasta mi )
# Si leo un )  y mi valor actual en el array no es 0 me muevo a la izquierda hasta mi (
# Si leo un 5  imprimo el valor actual del array en ASCII

# Ejemplo INPUT :
# INPUT = "4(4444444132)1454(41333332)13353333333553335"
# devuelve "HELLO"



INPUT = "4(4444444132)1454(41333332)13353333333553335"

VALUES = [0]

MAX = 255
MIN = 0
INDEX = 0
SUBINDEX = 0

retorno = []

def translate(bit):
    return chr(bit)

def operate(puntero, INDEX):
    if INPUT[puntero] == "1":
        return 0, 1 
    if INPUT[puntero] == "2":
        return 0 , -1 
    if INPUT[puntero] == "3":
        return  1 if VALUES[INDEX] != 255 else 0, 0
    if INPUT[puntero] == "4":
        return - 1 if VALUES[INDEX] != 0 else 255, 0
    if INPUT[puntero] == "5":
        retorno.append(translate(VALUES[INDEX]))
        return 0, 0

# elemento = (1* || 2* || 3* || 4*  || 5* || objeto) *
# objeto = "(" elemento ")"


puntero = 0
while puntero < len(INPUT):
    a = INPUT[puntero]
    if INPUT[puntero] == "(" and VALUES[INDEX] == 0:
        SUBINDEX += 1
        counter = 1
        while puntero < len(INPUT):
            if not SUBINDEX:
                puntero += counter - 1
                SUBINDEX = 0
                break
            if INPUT[puntero + counter] == ")":
                SUBINDEX -= 1
            elif INPUT[puntero + counter] == "(":
                SUBINDEX += 1
            counter += 1
    elif INPUT[puntero] == ")" and VALUES[INDEX] != 0:
        SUBINDEX += 1
        counter = 1
        while puntero < len(INPUT):
            if not SUBINDEX:
                puntero -= counter - 1
                SUBINDEX = 0
                break
            if INPUT[puntero - counter] == "(":
                SUBINDEX -= 1
                counter -= 1
            elif INPUT[puntero - counter] == ")":
                SUBINDEX += 1
                counter -= 1
            counter += 1
    else:
        if INPUT[puntero] == "(" or INPUT[puntero] == ")":
            puntero += 1
        else:
            add_value, add_index = operate(puntero, INDEX)
            INDEX += add_index
            if len(VALUES) == INDEX:
                VALUES.append(0)
            else:
                VALUES[INDEX] += add_value
            puntero += 1
    

print("a")

    