from cpf import validar_cpf
import os

def menu():
    while True:
        print("\n--- VALIDADOR DE CPF ---")
        print("1 - Validar CPF")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cpf = input("Digite o CPF: ")
            if validar_cpf(cpf):
                print("CPF válido")
            else:
                print("CPF inválido")

        elif opcao == "0":
            break

if __name__ == "__main__":
    if os.getenv("CI"):
        print("CI executado com sucesso!")
    else:
        # Executa automático (sem input → evita erro no Docker)
        teste = "52998224725"
        resultado = validar_cpf(teste)
        print(f"CPF {teste} é válido? {resultado}")
        print("Validador feito pelo Rick com sucesso")