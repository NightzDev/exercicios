# Aqui o usuário digitará o texto para ser invertido
texto = input("Digite uma string: ")

# Neste ele usa a própria propriedade do python que é o slice, para fazer o texto ficar em inverso
# Ele não usa uma função pronta,por exemplo:reverse(), e sim uma propriedade da própria linguagem
# Porém sem este [::-1], daria pra fazer um loop, onde ele percorria a string ao contrario e colocaria em "ordem" na varivel texto_invertido
texto_invertido = texto[::-1]

# Mostra o resultado com o texto original e invertido
print("String original:", texto)
print("String invertida:", texto_invertido)
