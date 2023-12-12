import random
def jogar():
    print("********************************")
    print("Bem vindo ao Jogo da Adivinhação")
    print("********************************/n")

    numero_secreto = random.randrange(1, 101)
    total_tentativas = 5
    rodada = 1
    total_pontos = 1000

    print("Selecione a dificuldade:")
    dificuldade = int(input("Fácil(1), Médio(2), Difícil(3): "))

    if (dificuldade == 1):
        total_tentativas = 20
    elif (dificuldade == 2):
        total_tentativas = 10
    elif (dificuldade == 3):
        total_tentativas = 5
    else:
        print("Comando desconhecido, por padrão, a dificuldade será difícil!")


    while(rodada <= total_tentativas):
        print("Rodada {} de {}".format(rodada, total_tentativas))
        chute = int(input("Adivinhe o número: "))

        print("Você digitou:", chute)

        if (chute > 100 or chute < 1):
            print("Você deve digitar um número de 1 a 100")
            continue

        acertou = chute == numero_secreto
        chuteMaior = chute > numero_secreto
        chuteMenor = chute < numero_secreto

        if (acertou):
            print("Acertou!")
            print("Você fez {} pontos!".format(total_pontos))
            break
        else:
            if (chuteMaior):
                print("O seu chute é maior que o número secreto")
            elif (chuteMenor):
                print("O seu chute é menor que o número secreto")
        rodada = rodada + 1
        total_pontos -= abs(numero_secreto - chute)


    print(f"O número era: {numero_secreto}")
    print("Fim de jogo!")

#Para executar diretamente o arquivo do jogo da adivinhação é necessário esta condição
#Quando você executa diretamente um arquivo em python, ele cria essa variavel name e atribui o valor main pra ela
#Isso não acontece quando importamos este arquivo igual estamos fazendo no jogos.py, pq ele não é executado diretamente
if (__name__ == "__main__"):
    jogar()