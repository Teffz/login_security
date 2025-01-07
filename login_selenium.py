from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Banco de dados simples (em memória)
users_db = {}

# Função para enviar mensagem pelo WhatsApp
def send_whatsapp_message(phone, message):
    # Configuração das opções do Chrome
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Maximiza a janela do navegador
    
    # Usando webdriver_manager para baixar e gerenciar o ChromeDriver
    service = Service(ChromeDriverManager().install())
    
    # Inicializando o driver com o serviço e as opções
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Abrindo o WhatsApp Web
    driver.get("https://web.whatsapp.com/")
    print("Escaneie o QR Code.")
    time.sleep(15)  # Espera para escanear o QR Code, você pode aumentar o tempo se necessário

    # Formatando o número de telefone
    phone = f"+{phone}"

    # Acessando o link para o WhatsApp
    url = f"https://web.whatsapp.com/send?phone={phone}&text={message}"
    driver.get(url)

    # Esperando até que o campo de mensagem esteja visível
    try:
        # Aguardando o campo de mensagem aparecer
        message_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="1"]'))
        )
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)
        print(f"Mensagem enviada para {phone}!")
    except Exception as e:
        print(f"Erro ao enviar a mensagem: {e}")
    
    # Fechar o navegador
    time.sleep(2)  # Dê tempo para a mensagem ser enviada
    driver.quit()

# Função para criar a conta e enviar a mensagem
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
    send_whatsapp_message(phone, "Você está cadastrado como usuário! 🎉")

# Função de login
def login():
    username = input("Digite o nome de usuário: ")
    password = input("Digite a senha: ")

    if username in users_db and users_db[username]["password"] == password:
        print("Login bem-sucedido!")
    else:
        print("Usuário ou senha incorretos!")

# Função para formatar o número de telefone
def format_phone(phone):
    """Formata o número de telefone no estilo XX-XXXXX-XXXX."""
    return f"({phone[:2]}) {phone[2:7]}-{phone[7:]}"

# Função para listar os usuários cadastrados
def list_users():
    if not users_db:
        print("Nenhum usuário cadastrado!")
        return

    print("\nUsuários cadastrados:")
    for username, details in users_db.items():
        formatted_phone = format_phone(details["phone"])
        print(f"- {username} (E-mail: {details['email']}, Telefone: {formatted_phone})")

# Função principal
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
