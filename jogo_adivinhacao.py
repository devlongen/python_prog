import random

loop_adivinha = True
# Define a variável de controle do loop principal do jogo
while loop_adivinha:
    tentativas = 3 # Número máximo de tentativas
# Gera um número aleatório de 1 a 100
    numero_aleatorio = random.randint(1,100)
    numero_proximo = numero_aleatorio
# Solicita e valida o nome do usuário
    print("-= Seja bem vindo ao jogo de adivinhação em Python =-")
    print("   Para começarmos preciso de suas informações  ")
    while True:
        nome_usuario = str(input("Diga o seu nome >"))
        if nome_usuario.isalpha():
            break
        else:
            print("As informações que inseriu está incorreto, tente novamente!")
    while True:
        idade_usuario = int(input("Diga a sua idade >"))
        if 0 <= idade_usuario <= 99:
            break
        else:
            print("Idade inválida você inseriu um valor não congruente!")
 # Solicita e valida a idade do usuário
    while True:
        resposta_usuario = str(input("Vamos começar a jogar? (sim ou não)"))
        if resposta_usuario == "sim":
            break
        elif resposta_usuario == "não":
            print("Espero que tenha um bom dia!")
            loop_adivinha = False
            break
        else:
            print("Você escreveu algo inválido ou algo diferente de sim ou não")
 # Verifica se o usuário deseja começar o jogo
    while loop_adivinha and tentativas:
    # Inicia o loop de tentativas enquanto o jogo estiver ativo e houver tentativas restantes
        tentativa_jogador = int(input("Você terá 3 tentativas de acertar um número aleatório de 1 até 100, BOA SORTE!"))
        if tentativa_jogador == numero_aleatorio:
            print("Parabéns! Você acertou o número!")
            loop_adivinha = False
            break
        elif tentativa_jogador > numero_aleatorio and tentativa_jogador <= 100:
                numero_proximo = numero_aleatorio + 15
                print("Boa tentativa, mas o número é menor que:", numero_proximo)
        elif tentativa_jogador < numero_aleatorio and tentativa_jogador >= 0:
            numero_proximo = numero_aleatorio - 15
            print("Boa tentativa, mas o número é maior que:", numero_proximo)
        else:
            print("Voce digitou um numero invalido tente novamente, lembrando e de 0 ate 100")
            tentativas += 1
        tentativas -= 1
        # Verifica se acabaram as tentativas
        if tentativas == 0:
            print(f"Fim das tentativas. O número era {numero_aleatorio}.")
            loop_adivinha = False
# Pergunta ao usuário se deseja tentar novamente
    while True:
            resposta_recomecar = str(input("Você deseja tentar novamente? (sim ou não)"))
            if resposta_recomecar == "sim":
                loop_adivinha = True
                break
            elif resposta_recomecar == "não":
                print("Espero que tenha gostado do jogo!")
                loop_adivinha = False
                break
            else:
                print("Você digitou algo inválido ou que não condiz com a pergunta, tente novamente!")
