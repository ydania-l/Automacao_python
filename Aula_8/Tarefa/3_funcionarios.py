#Tarefa 3. 
# O departamento de desenvolvimento possui duas equipes: testadores e desenvolvedores. 
# Imprima os nomes de todos os funcionários do departamento. 

equipe_qa = ['Jordan Lee', 'Alex Patel'] 
equipe_dev = ['Taylor Nguyen', 'Casey Johnson'] 

departamento =  [equipe_qa + equipe_dev]

print('Funcionários:') 
for qa_funcionario in equipe_qa:
    print(qa_funcionario)

for dev_funcionario in equipe_dev:
    print(dev_funcionario)


#Saída esperada: 
# Funcionários: Jordan Lee Alex Patel Taylor Nguyen Casey Johnson 