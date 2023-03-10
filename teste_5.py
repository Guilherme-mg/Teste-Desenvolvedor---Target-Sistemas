"""
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
"""

string = input('Digite uma palavra: ')

def inverter(string):
    palavra_invertida =  string[::-1]
    return palavra_invertida


print(inverter(string))