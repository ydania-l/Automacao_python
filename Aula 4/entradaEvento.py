'''
Criar um novo arquivo chamado entradaEvento.py;
Receber a idade do usuário - utilize int() para converter a
variável para o tipo inteiro;
Se o usuário for maior de idade, exiba:
“Bom evento para você que tem {idade} anos!ˮ
'''
idade = int(input())


if(idade > 18):
    print("Bom evento para você que tem " + str(idade) + " anos")
