# n1 = int(input('Um valor '))
# n2 = int(input('Outro valor '))
# s = n1 + n2
# m = n1 * n2
# d = n1 / n2
# p = n1 ** n2
# di = n1 // n2
# rd = n1 % n2
# print('A soma vale {}, a multiplicação vale {}, a divisão vale {:.3f}'. format(s, m, d), end=' ')
# print('a potência vale {}, a divisão inteira vale {}, o resto da divisão vale {}'.format(p, di, rd))
n1 = int(input('Coloque o número inteiro: '))
print(n1, 'Seu antecessor {}, Seu Sucessor {}'. format((n1-1), (n1+1)))

n2 = int(input('Digite outro número '))
print('Seu dobro {}, Seu triplo {}, Sua raiz {:.2f}'. format((n2*2), (n2*3), (n2**(1/2))))

n3 = float(input('Sua primeira nota: '))
n4 = float(input('Sua segunda nota: '))
print('A média do Aluno é: {}'.format((n3+n4)/2))

n5 = float(input('Coloque os metros: '))
print('Centímetros {}, Milímetros {}'. format((n5*10), (n5*100)))

n6 = int(input('Número para tabuada: '))
print(n6*1)
print(n6*2)
print(n6*3)
print(n6*4)
print(n6*5)
print(n6*6)
print(n6*7)
print(n6*8)
print(n6*9)
