my_str = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
my_str = my_str.lstrip(",:_#,,,,,,:::____##")

print(my_str)

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"] 

frutas.insert(3,"naranja")

print(frutas)

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)

print(conjuntos_aislados)

A = {1, 2, 3}
B = {4, 5, 6}
C = {6, 7, 8}

print('A and B are disjoint:', A.isdisjoint(B))
print('B and C are disjoint:', B.isdisjoint(C))