from time import sleep
bonecocabeca = '  O'
bonecotorso = ' /|\ '
bonecopernas = ' / \ '
print(' ' + bonecocabeca, '\n',bonecotorso, '\n',bonecopernas)
a = int(input('Quantos passos eu vou dar? '))
for andar in range(1, a):
    print('\n' * 100)
    andarb = ' ' * andar
    print((' ' * 207) + '*')
    print(andarb + bonecocabeca)
    print(andarb + bonecotorso)
    print(andarb + bonecopernas)
    sleep(0.28)
if a == 206:
    print('Você chegou ao seu destino')
else:
    print(f'Faltaram {206 - a} passos para chegar ao seu destino')
