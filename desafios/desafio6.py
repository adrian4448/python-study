frutas = ['maca', 'banana', 'manga', 'uva']

print(frutas)

print(frutas[0])
print(frutas[3])

frutas[1] = 'morango'

frutas.append('abacaxi')

print(frutas)

frutas.remove('manga')

del frutas[-1]

print(frutas)

for fruta in frutas:
    print(f'Eu gosto de {fruta}')