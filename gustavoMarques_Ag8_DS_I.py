# Pesquisa de Atendimento ao Cliente
# Autor: GM Tech

# Entradas
respostas = []
continuar = True
i = 0

# Processamento
while continuar and i < 50:
    i += 1
    print("\n--- Pesquisa de Atendimento TudoWeb ---")
    nome = input("Digite seu nome: ")
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            break
        except ValueError:
            print("Por favor, digite apenas números.")
    while True:
        try:
            opiniao = int(input("Digite sua opinião sobre nosso atendimento (1-Excelente, 2-Bom, 3-Ruim): "))
            if opiniao in [1, 2, 3]:
                break
            else:
                print("Por favor, digite 1 para 'Excelente', 2 para 'Bom' ou 3 para 'Ruim'.")
        except ValueError:
            print("Por favor, digite apenas números.")
    print("\nObrigado por participar da pesquisa!")
    while True:
        try:
            continuar_aux = int(input("Deseja passar a outro usuário? (1- Sim, 2- Não): "))
            if continuar_aux in [1, 2]:
                break
            else:
                print("Por favor, digite 1 para 'Sim' ou 2 para 'Não'.")
        except ValueError:
            print("Por favor, digite apenas números.")
    if continuar_aux == 2:
        continuar = False
    else:
        print("\nPróximo usuário, por favor.")
    respostas.append({"nome": nome, "idade": idade, "opiniao": opiniao})

qtd_excelente = 0
qtd_ruim = 0

for resposta in respostas:
    if resposta["opiniao"] == 1:
        qtd_excelente += 1
    elif resposta["opiniao"] == 3:
        qtd_ruim += 1


# Saída
print("\n--- Resultados da Pesquisa ---")
print(f"Total de respostas: {len(respostas)}")
print(f"Opiniões 'Excelente': {qtd_excelente}")
print(f"Opiniões 'Ruim': {qtd_ruim}")