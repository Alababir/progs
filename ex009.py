preco = float(input('Qual o valor do produto? R$'))
valor = (preco / 100) *5
total = preco - valor
print('O produto que custaria {:.2f} na promoção de 5% vai sair por {:.2f}'.format(preco, total))