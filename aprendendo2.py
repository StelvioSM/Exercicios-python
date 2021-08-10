from stringprep import in_table_c11_c12

a = int (input ('Entre com um numero:'))
b = int (input ('Entre com um numero:'))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
print('soma: {soma}.'
      '\nsubtracao: {subtracao}. '
      '\nMultiplicacao:{multiplicacao}'
      '\nDivisao: {divisao}'.format(soma = soma,
                         subtracao = subtracao,
                         divisao = divisao,
                         multiplicacao=multiplicacao) )
