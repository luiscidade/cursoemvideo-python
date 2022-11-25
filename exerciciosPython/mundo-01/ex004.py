# dissecando variaveis

n = input('Digite algo: \n')
print('É do tipo', type(n))
print('É numérico? ', n.isnumeric())
print('É decimal? ', n.isdecimal())
print('É composto exclusivamento por letras maiúsculas? ', n.isupper())
print('É composto exclusivamento por letras minúsculas? ', n.islower())
print('É alfanumérico? ', n.isalnum())
print('É alfabético? ', n.isalpha())
print('É composto apenas de espaços? ', n.isspace())