#Agora você precisa contar quantos testes foram bem-sucedidos e quantos falharam. Além disso, você precisa exibir informações mais detalhadas sobre eles. As variáveis passed e failed são fornecidas como entrada.
passed = 3
failed = '2'

count = (passed + int(failed)) # Aqui você precisa calcular o número total de testes realizados

message_result = 'Realizamos no total ' + str(count) + ' testes' # Use a variável count aqui
message_details = 'Quantidade de testes aprovados: ' + str(passed) + ', reprovados: ' + str(failed)   # Use as variáveis passed e failed aqui

print(message_result)
print(message_details)

