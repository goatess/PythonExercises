class TextBuilder:
   
    def read():
        file = open('entradaSalida/note.txt', 'r')
        text = file.readlines()
        print(text)
        file.close()

    def write(text):
        file = open('entradaSalida/note.txt', 'w')
        file.write(text)
        file.close()

TextBuilder.write("Este es el nuevo texto de la nota")
TextBuilder.read()



