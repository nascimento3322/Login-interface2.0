print("Olá, seja bem-vindo, para acessar nosso aplicativo preciso que digite seu login e sua senha")

# Definição de login correto
login_correto = "Vinicius"
tentativas_login = 3
tentativas_realizadas = 0

# Verificação do login
while tentativas_realizadas < tentativas_login:
    login = input("Digite seu login: ")
    if login == login_correto:
        print("Login correto")
        break
    else:
        tentativas_realizadas += 1
        print(f"Login inválido. Tentativas restantes: {tentativas_login - tentativas_realizadas}")
else:
    print("Você errou o login 3 vezes. Acesso negado.")
    exit()  # Encerra o programa

# Definição da senha correta
senha_correta = "123"
tentativas_senha = 3
tentativas_realizadas = 0

# Verificação da senha
while tentativas_realizadas < tentativas_senha:
    senha = input("Digite sua senha: ")
    if senha == senha_correta:
        print("Senha correta")
        print("Seja bem-vindo!")
        break
    else:
        tentativas_realizadas += 1
        print(f"Senha inválida. Tentativas restantes: {tentativas_senha - tentativas_realizadas}")
else:
    print("Você errou a senha 3 vezes. Acesso negado.")    
