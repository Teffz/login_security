import pywhatkit
import time

# Banco de dados simples (em memória)
users_db = {}

def create_account():
    username = input("Digite o nome de usuário: ")
    if username in users_db:
        print("Usuário já existe!")
        return

    password = input("Digite a senha: ")
    email = input("Digite o e-mail: ")
    phone = input("Digite o número de telefone (somente números): ")

    # Verifica se o telefone contém apenas números e tem o tamanho esperado
    if not phone.isdigit() or len(phone) != 11:
        print("Número de telefone inválido! Insira 11 dígitos (código de área + número).")
        return

    # Armazenando os dados do usuário
    users_db[username] = {
        "password": password,
        "email": email,
        "phone": phone
    }
    print(f"Conta criada para {username}!")

    # Enviar mensagem via WhatsApp para o número cadastrado
    send_whatsapp_message(phone)

def send_whatsapp_message(phone):
    "Envia uma mensagem de confirmação para o número via WhatsApp"
    # Formatar o número no formato internacional
    formatted_phone = f"+55{phone}"

    # Aguardar até um pouco antes do horário para enviar a mensagem
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min + 1  # Envia 1 minutos após a execução

    if minute >= 60:
        hour += 1
        minute -= 60

    # Envia a mensagem de confirmação para o número via WhatsApp
    pywhatkit.sendwhatmsg(formatted_phone, "Você está cadastrado como usuário! 🎉", hour, minute)

    print(f"Mensagem de confirmação enviada para {formatted_phone}!")

def login():
    username = input("Digite o nome de usuário: ")
    password = input("Digite a senha: ")

    if username in users_db and users_db[username]["password"] == password:
        print("Login bem-sucedido!")
    else:
        print("Usuário ou senha incorretos!")

def format_phone(phone):
    """Formata o número de telefone no estilo XX-XXXXX-XXXX."""
    return f"({phone[:2]}) {phone[2:7]}-{phone[7:]}"

def list_users():
    if not users_db:
        print("Nenhum usuário cadastrado!")
        return

    print("\nUsuários cadastrados:")
    for username, details in users_db.items():
        formatted_phone = format_phone(details["phone"])
        print(f"- {username} (E-mail: {details['email']}, Telefone: {formatted_phone})")

def main():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Criar conta")
        print("2 - Fazer login")
        print("3 - Ver usuários cadastrados")
        print("4 - Sair")
        option = input("Digite o número da opção: ")

        if option == "1":
            create_account()
        elif option == "2":
            login()
        elif option == "3":
            list_users()
        elif option == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
