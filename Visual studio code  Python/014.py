salario = float(input('Qual é o salário do funcionario?'))
novo = salario + (salario*15/100)
print('O funcionario que ganhava R${:.2f}, com o aumento de 15% passa a receber R${:.2f}'.format(
    salario, novo))
