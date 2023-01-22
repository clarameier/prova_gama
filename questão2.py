#questão 2.
#Elabore um programa que leia um número que o usuário digitar. Dependendo do
#número informado, das frases abaixo, o sistema imprimirá somente as que forem
#verdadeiras.
#○ O número é menor que 10.
#○ O número é par.
#○ O número está entre 8 e 16.
#○ O número é 51 ou 80.
#Por exemplo, se o usuário digitar o número “12”, o programa irá imprimir:
#O número é par.
#O número está entre 8 e 16.
#Se o usuário digitar o número “51”, então será impresso:
#O número é 51 ou 80.
#Ou, se o usuário digitar “101”, então o programa não imprime nada.


#número digitado pelo usuário:
user = int(input("Digite um número: "))

#regras:

if user < 10:
    print("O número é menor que 10.")

if user % 2 == 0:
    print("O número é par.")

if user >= 8 and user <= 16:
    print("O número está entre 8 e 16.")

if user == 51 or user == 80:
    print("O número é 51 ou 80.")

