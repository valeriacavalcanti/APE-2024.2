PASSWORD = 2002

while True:
    senha = int(input('Digite a senha: '))
    if senha == PASSWORD:
        print('Acesso permitido')
        break
    
    print('Senha inválida')
