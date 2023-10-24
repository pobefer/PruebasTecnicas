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

class Interpreter:

    def __init__(self, input_str):
        self.input_str = input_str
        self.MEMORY = [0]
        self.PUNTERO = 0
        self.index = 0
        self.result = []
        self.command_mapping = {
            '1': self.move_right_pointer,
            '2': self.move_left_pointer,
            '3': self.increment_memory,
            '4': self.decrement_memory,
            '5': self.output_result
        }

    @staticmethod
    def translate(bit):
        return chr(bit)

    def jump_forward(self):
        depth = 1
        while depth > 0:
            self.index += 1
            if self.input_str[self.index] == '(':
                depth += 1
            elif self.input_str[self.index] == ')':
                depth -= 1

    def jump_backward(self):
        depth = 1
        while depth > 0:
            self.index -= 1
            if self.input_str[self.index] == '(':
                depth -= 1
            elif self.input_str[self.index] == ')':
                depth += 1

    def move_right_pointer(self):
        if len(self.MEMORY) <= self.PUNTERO + 1:
            self.MEMORY.append(0)
        self.PUNTERO += 1

    def move_left_pointer(self):
        self.PUNTERO -= 1

    def increment_memory(self):
        self.MEMORY[self.PUNTERO] = (self.MEMORY[self.PUNTERO] + 1) % 256

    def decrement_memory(self):
        self.MEMORY[self.PUNTERO] = (self.MEMORY[self.PUNTERO] - 1) % 256

    def output_result(self):
        self.result.append(self.translate(self.MEMORY[self.PUNTERO]))

    def interpret(self):
        while self.index < len(self.input_str):
            char = self.input_str[self.index]

            if char in self.command_mapping:
                self.command_mapping[char]()
            elif char == '(' and self.MEMORY[self.PUNTERO] == 0:
                self.jump_forward()
            elif char == ')' and self.MEMORY[self.PUNTERO] != 0:
                self.jump_backward()

            self.index += 1

        return ''.join(self.result)


input_str = "133333333(423333333331)2511314(3)331331333(1(41333223331)22)1444445141333553335145223(1(313)11)244444444444444511533354444445444444445135135"
interpreter = Interpreter(input_str)
print(interpreter.interpret())
