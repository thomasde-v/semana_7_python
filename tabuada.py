def tabuada(numero):
    print(f"Tabuada de {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} X {i} = {resultado}")

numero_escolhido = int(input("Digite um número (de 1 a 10) para ver a tabuada: "))
tabuada(numero_escolhido)
