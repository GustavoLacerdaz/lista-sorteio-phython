clientes = []

while True:

     name = input("informe o nome, para sair digite FIM ")

     if name.upper() == "FIM":
        break

     telefone = input("informe o telefone ")
     endereco = input("informe o endereco ")

     cliente = {
        'name': name,
        'telefone': telefone,
        'endereco': endereco
    }
     clientes.append(cliente)
     print("Usuario adicionado")

if clientes:
    import random
    sorteado = random.choice(clientes)
    print("O sorteado foi:")
    print(f"Nome: {sorteado['name']}")
    print(f"Telefone: {sorteado['telefone']}")
    print(f"Endereço: {sorteado['endereco']}")
else:
    print("Nenhum cliente para sortear.")






        
