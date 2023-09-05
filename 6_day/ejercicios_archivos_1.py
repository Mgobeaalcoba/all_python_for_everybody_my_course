my_file = open("texto.txt","r")
print(my_file.readline().rstrip()) # .rstrip quita el enter de la derecha de la linea
print(my_file.readline().rstrip())
my_file.close()


my_file = open("texto.txt", "r")
print(my_file.readline())
my_file.close()


my_file = open("texto.txt", "r")
my_lines = my_file.readlines()
print(my_lines[1])
my_file.close()


