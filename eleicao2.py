def exibir_menu():
    print("\n=== MENU ====")
    print("1. Candidato chiquinho")
    print("2. Candidato ze da manga")
    print("3. Candidato buiu")
    

eleitores = int(input("Digite o número total de eleitores: "))

votos = {"chiquinho": 0, "ze da manga": 0, "buiu": 0}
candidato_vencedor = None  
for i in range(eleitores):
    exibir_menu()
    voto = input("Digite o número do candidato de sua escolha: ")
    
    if voto in ["1", "2", "3"]:
        candidato = {"1": "chiquinho", "2": "ze da manga", "3": "buiu"}[voto]
        votos[candidato] += 1
        
        if candidato_vencedor is None or votos[candidato] > votos[candidato_vencedor]:
            candidato_vencedor = candidato
    else:
        print("Número inválido. Tente novamente.")


for candidato, num_votos in votos.items():
    print(f"{candidato}: {num_votos} voto(s)")

#
if candidato_vencedor:
    print(f"Candidato vencedor: {candidato_vencedor}")
else:
    print("Nenhum voto registrado.")
