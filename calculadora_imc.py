def calculo_imc(peso_usuario, altura_usuario):
    #calculando e arredondando o IMC.
    return  peso_usuario / (altura_usuario * altura_usuario)   
loop_calculadora = True
while loop_calculadora:
    while True:
        nome_usuario = str(input("Escreva o seu nome > "))
        while True:
            if nome_usuario.isalpha():
                break
            else:
                print("As informações que inseriu está incorreto, tente novamente!")
        try:
            idade_usuario = int(input("Digite a sua idade > "))
            if 0 <= idade_usuario <= 100:
                break
            else:
                print("Erro: número inválido")
        except ValueError as e:
            print(f"Erro de valor: {e}")

    while True:
        try:
            peso_usuario = float(input("Digite o seu peso em kg > "))
            if 0 <= peso_usuario <= 500.00:
                break
            else:
                print("Erro: número inválido")
        except ValueError as e:
            print(f"Erro de valor: {e}")
#Pedindo informação e validação do usuário.
    while True:
        try:
            altura_usuario = float(input("Digite a sua altura em metros > "))
            if 0 <= altura_usuario <= 2.20:
                break
            else:
                print("Erro: número inválido")
        except ValueError as e:
            print(f"Erro de valor: {e}") 
    resposta_usuario = str(input("Vamos calcular o seu IMC? (sim ou não)"))
    if resposta_usuario.lower() == 'sim':
        resultado_imc = round(calculo_imc(peso_usuario,altura_usuario),2)
        if resultado_imc < 18.5:
            print("Você se encontra abaixo do peso, pois seu resultado deu:", resultado_imc)
        elif 18.5 <= resultado_imc <= 24.9:
            print("Você se encontra com peso normal, pois seu resultado deu:", resultado_imc)
        elif 25 <= resultado_imc <= 29.9:
            print("Você se encontra sobrepeso, pois seu resultado deu:", resultado_imc)
        elif 30 <= resultado_imc <= 34.9:
            print("Você se encontra com obesidade grau I, pois seu resultado deu:", resultado_imc)
        elif 35 <= resultado_imc <= 39.9:
            print("Você se encontra com obesidade grau II, pois seu resultado deu:", resultado_imc)
        elif resultado_imc >= 40:
            print("Você se encontra com obesidade grau III, pois seu resultado deu:", resultado_imc)
    #saída da informação e definição.
    else:
        print("Tudo bem, tenha um bom dia!")
    resposta_loop = str(input("Deseja continuar? (sim ou não)"))
    if resposta_loop.lower() != 'sim':
        loop_calculadora = False
        print("Espero que tenha ajudado!")
    else:
        print("Seja bem-vindo de volta!")
    #Retorno de loop_calculadora caso ao contrário irá finalizar o programa