#questão 4.
#Crie duas funções:
#○ A primeira função receberá dois parâmetros e retornará como resultado uma
#concatenação de texto colocando uma vírgula entre os dois parâmetros ao
#uní-los.
#○ A segunda função não receberá parâmetros; será feito a leitura de duas
#entradas que o usuário digitar; irá chamar a primeira função passando como
#argumento os dois textos lidos; por fim esta segunda função irá imprimir para
#o usuário informando qual foi o resultado que se obteve na chamada à
#primeira função.
#○ Exemplo da primeira entrada: “Olá”. Exemplo da segunda entrada: “Mundo”.
#Exemplo da saída do sistema: “Olá,Mundo”.


#concatenando função1
def soma(primeiro, segundo):
    return primeiro + ", " + segundo #botei um espaço depois da vírgula para não ficar grudado

#usuário escreve função2
def usuário():
    p = input("Primeira palavra/frase: ")
    s = input("Segunda palavra/frase: ")
    concatenação = soma(p, s)
    print(f'{concatenação}')

#terminal lê
usuário()