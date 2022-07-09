"""nome = "gabriel"
lista = {1, 3, 5, 9}
numeros = range(1, 10)
for indice, letra in enumerate(nome):
     print(nome[indice])
     é impresso na tela as letras do nome gabriel, uma por uma
      range= mostra de onde vai partir, nesse caso, o numero da letra
      """
print("Bem vindo a nossa pousada águia, o que deseja fazer?")
menu = int(input(print("digite [1] para agendar nova reserva:\n"
      f"Digite [2] para acessar sua conta:\n"
      f"Digite [3] para um novo cadastro:")))
if menu == 1:
    nome=str(input(print("Olá, Insira seu nome:")))
    senha=str(input("agora, sua senha: "))
    quartos=int(input('Quantos quartos deseja?'))
    dias=int(input('quantos dias deseja ficar hospedado?'))
    print('detalhes da reserva:\n')
    print(f'Nome: {nome}\n'
          f'Quantidade de quartos: {quartos}\n'
          f'Quantidade de dias de hospedagem: {dias}')
elif menu == 2:
        email= str(input('digite seu email: '))
        senha= str(input('Agora, digite sua senha: '))
        print('Bem vindo!')
elif menu ==3:
        print("cadastro de usuários")
        qtd = (int(input("quantas pessoas deseja adicionar? ")))
        for n in range(1, qtd+1):
         usuarios = (str(input(f"digite o nome: {n}/{qtd}")))
         email = (str(input(f'digite seu email: {n}/{qtd}')))
         criar_senha= (str(input(f'crie uma senha: {n}/{qtd}')))
         print(f'Você adicionou: {usuarios} e o email é: {email}')
         print('cadastro feito com sucesso.')