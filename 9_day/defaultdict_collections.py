from collections import defaultdict

dict_normal = {"uno":"verde", "dos":"azul", "tres":"rojo"}
print(dict_normal["dos"]) # azul
# print(dict_normal["cuatro"]) # KeyError: 'cuatro'

# Esto puede ser un problema si quiero recorrer un dict usando una lista de numeros continuos, por ejemplo, como keys

mi_dic = defaultdict(lambda: 'nada')

mi_dic['uno'] = "verde"

print(mi_dic["uno"]) # verde
print(mi_dic["dos"]) # nada / Si la key no existe entonces me devuelve el valor establecido como lambda.

print(mi_dic) # defaultdict(<function <lambda> at 0x000001FF3098D260>, {'uno': 'verde', 'dos': 'nada'})
