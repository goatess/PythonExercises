class TextBuilder:
   
    def read():
        file = open('entradaSalida/ej1/note.txt', 'r')
        text = file.readlines()
        file.close()
        print(text)

    def write(text):
        file = open('entradaSalida/ej1/note.txt', 'w')
        file.write(text)
        print(text)
        file.close()

TextBuilder.write("Este es el nuevo texto de la nota")
TextBuilder.read()



