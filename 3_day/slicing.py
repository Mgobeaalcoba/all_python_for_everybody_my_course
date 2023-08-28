texto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
fragmento = texto[2] # C
print(fragmento)
fragmento = texto[2:5] # CDE
print(fragmento)
fragmento = texto[2:] # CDEFGHIJKLMNOPQRSTUVWXYZ
print(fragmento)
fragmento = texto[:5] # ABCDE
print(fragmento) 
fragmento = texto[2:10:2] # CEGI
print(fragmento) 
fragmento = texto[::3] # ADGJMPSVY
print(fragmento) 
fragmento = texto[::-1] # ZYXWVUTSRQPONMLKJIHGFEDCBA
print(fragmento) 