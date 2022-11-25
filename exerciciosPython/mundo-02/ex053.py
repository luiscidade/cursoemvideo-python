# Detector de Palíndromo

frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inversa = ''

for letra in range(len(frase) - 1, -1, -1):
    inversa += junto[letra]
print(junto, inversa)

