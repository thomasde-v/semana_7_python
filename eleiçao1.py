def exibir_menu():
    print("\n=== MENU ====")
    print("1. Candidato chiquinho")
    print("2. Candidato ze da manga")
    print("3. Candidato buiu")
    print("4. Sair")


eleitores = int(input("Digite o número total de eleitores: "))


votos = {"chiquinho": 0, "ze da manga": 0, "buiu": 0}


for i in range(eleitores):
    exibir_menu()  
    voto = input("Digite o número do candidato da sua escolha: ")
    
    
    if voto in ["1", "2", "3"]:
        candidato = {"1": "chiquinho", "2": "ze da manga", "3": "buiu"}[voto]
        votos[candidato] += 1  
    else:
        print("Número inválido. Tente novamente.")


for candidato, num_votos in votos.items():
    print(f"O candidato {candidato} teve {num_votos} votos.")
