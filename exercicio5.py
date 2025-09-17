from dataclasses import dataclass
from datetime import datetime

#classes:

@dataclass
class CadastroCliente:
    nome: str
    numero: str
    email: str

class Agendamento:
    data_hora: datetime
    barbeiro: str
    cortes: str
    nome: str
    
def menu():
    print("\n--- Bem vindo a barbearia Los Pintos!! ---")
    print("1 - Efetue o cadastro")
    print("2 - Realizar o agendamento do serviço")
    print("3 -  Visualizar carrinho")
    print("4 - Cancelar agendamento")
    print("5 - Sair")
    return input("Escolha uma opção: ")

    
while True:
    opcao = menu()
            
    if opcao == "1":
        nome = input("Digite seu nome: ")
        numero = input("Seu número: ")
        email = input("Seu E-mail: ")
        print(f"Nome '{nome}' Cadastrado com sucesso!")
             
    elif opcao == "2":
        if nome is None:
            data_hora = input ("Digite o dia desejado:")
            
            print("Agendamento do serviço concluido☻!")
            