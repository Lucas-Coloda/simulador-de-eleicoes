import random


def dia_de_votacao(meu_voto):
    coligacao_vegana = 0
    coligacao_carnivora = 0

    for a in range(99):
        votos = random.randint(1, 2)
        if votos == 1:
            coligacao_vegana += 1
            print("Coligacao vegana  obteve 1 voto")
        elif votos == 2:
            coligacao_carnivora += 1
            print("coligacao_carnivora obteve 1 voto")

    if meu_voto == "1":
        coligacao_vegana += 1
        print("Coligacao vegana  obteve o SEU voto")
    elif meu_voto == "2":
        coligacao_carnivora += 1
        print("coligacao_carnivora obteve o SEU voto")

    return coligacao_vegana, coligacao_carnivora


def resultado_eleicoes(total_de_votos, meu_voto):
    coligacao_vegana = total_de_votos[1]
    coligacao_carnivora = total_de_votos[0]

    print("\n" + "Coligacao vegana obteve um total de", coligacao_vegana, "% dos votos" + "\n",
          "\n" + "Coligacao carnivora obteve um total de", coligacao_carnivora, "% dos votos" + "\n")

    if coligacao_carnivora > coligacao_vegana:
        print("\n" + "Coligacao carnivora ganhou as eleicoes.")

        if meu_voto == "2":
            print("Ainda nao acabou, nao esqueca de cobrar as promecas de campanha.")
        else:
            print("Nao foi dessa vez, mas sempre lute pelo seu ideal!")

    elif coligacao_vegana > coligacao_carnivora:
        print("\n" + "Coligacao vegana ganhou as eleicoes.")

        if meu_voto == "1":
            print("Ainda nao acabou, nao esqueca de cobrar as promecas de campanha.")
        else:
            print("Nao foi dessa vez, mas sempre lute pelo seu ideal!")

    else:
        print("As eleicoes empataram, os dois administraram a associacao")


def votar():
    voto = 0

    print("Neste ano ira ocorrer as eleicoes da associacao internacional dos restaurantes, vote sabiamente:"
          + "\n\t" + "Vote chapa 1, candidato da coligacao vegana, viva ao mundo VERDE!"
          + "\n\t" + "Vote chapa 2, candidato da coligacao carnivora, viva ao CHURRASCO!")

    while voto != "1" and voto != "2":
        voto = str(input("O voto e secreto, entao nao contarei a ninguem....\tChapa: "))
        if voto != "1" and voto != "2":
            print("Sinto muito, esse candidato nao se cadastrou.")

    return voto


def programa():
    while True:
        meu_voto = votar()
        total_de_votos = dia_de_votacao(meu_voto)
        resultado_eleicoes(total_de_votos, meu_voto)

        print("\n" + "Caro cozinheiro selecione:"
              + "\n\t" + "maquina do tempo"
              + "\n\t" + "sair da associacao")
        opcao = input("E agora?: ")

        if opcao == "maquina do tempo":
            print("Voce avancou 1 ano a frente" + "\n")
        elif opcao == "sair da associacao":
            print("Irei as eleicoes da associacao de engenharia ano que vem, "
                  + "parece que eles nao gostam que alguem fique cutucando a comida toda hora.... "
                  + "Nos vemos por ai")
            break
        else:
            print("Nao entendi muito bem... Enquanto eu analizava passou-se um ano, e' hora de votar novamente!" + "\n")


programa()
