#ExercÃ­cio para saber se as medidas podem formar um triÃ¢ngulo
print('-=' * 15)
print('Analisador de TriÃ¢ngulos')
print('-=' * 15)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triÃ¢ngulo!')
else:
    print('Os segmentos acima NÃƒO PODEM FORMAR um triÃ¢ngulo!')
