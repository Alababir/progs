s = float(input('Qual o salário do funcionário? R$'))
r = ((s / 100) * 15) + s
print('Um funcionário que recebe R${:.2f} com um reajuste de 15%, vai começar a receber R${:.2f}.'. format(s, r))