acessorios = []
for lista in dados: #cria uma lista pegando a lista de dados(lista criada anteriormente)
  for item in lista:#cria uma lista pegando a lista de lista(criada no primeiro for)
    acessorios.append(item)# adiciona items na lista de acessorios
print(acessorios)

#comando set() remove duplicatas 
list(set(acessorios))

#exercicio
dados = [ 
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I']
]

result = []
  for lista in dados:
    for item in lista:
      result.append(item)
print(result)
#vai imprimir todos os items apenas em result
#caso2
result_2 = []
for lista in dados:
    result_2 += lista
result_2
#vai imprimir todos os items apenas em result_2
#caso3

[item for lista in dados for item in lista]
#vai pegar o mesmo resultado adc na lista item:

# INSTRUÇÃO IF
# 1º item da lista - Nome do veículo
# 2º item da lista - Ano de fabricação
# 3º item da lista - Veículo é zero km?

dados = [
    ['Jetta Variant', 2003, False],
    ['Passat', 1991, False],
    ['Crossfox', 1990, False],
    ['DS5', 2019, True],
    ['Aston Martin DB4', 2006, False],
    ['Palio Weekend', 2012, False],
    ['A5', 2019, True],
    ['Série 3 Cabrio', 2009, False],
    ['Dodge Jorney', 2019, False],
    ['Carens', 2011, False]
]

print(dados)

zero_km_y = []

for lista in dados:
  if(lista[2]==True):
    zero_km_y.append(lista)
print(zero_km_y)

# instrução em uma unica linha
[lista for lista in dados if lista[2] == True] # List comprehensions


#IF E ELIF
if <condição 1>:
    <instruções caso a condição 1 seja verdadeira>
elif <condição 2>:
    <instruções caso a condição 2 seja verdadeira>
elif <condição 3>:
    <instruções caso a condição 3 seja verdadeira>
                        .
                        .
                        .
else:
    <instruções caso as condições anteriores não sejam verdadeiras>

print('AND')
print(f'(True and True) o resultado é: {True and True}')
print(f'(True and False) o resultado é: {True and False}')
print(f'(False and True) o resultado é: {False and True}')
print(f'(False and False) o resultado é: {False and False}')

print('OR')
print(f'(True or True) o resultado é: {True or True}')
print(f'(True or False) o resultado é: {True or False}')
print(f'(False or True) o resultado é: {False or True}')
print(f'(False or False) o resultado é: {False or False}')

#instrução if com elif usando operadores and e or
A, B, C = [], [], []
for lista in dados:
  if(lista[1] <= 2000):
    A.append(lista)
  elif (lista[1] > 2000 and lista[1] <= 2010):
     B.append(lista)
  else:
    C.append(lista)

#OPERAÇÕES COM ARRAYS NUMPY

#Considere o seguinte array:
dados = np.array(
    [
        ['Roberto', 'casado', 'masculino'],
        ['Sheila', 'solteiro', 'feminino'],
        ['Bruno', 'solteiro', 'masculino'],
        ['Rita', 'casado', 'feminino']
    ]
)

print(dados[0::2, :2])
array([['Roberto', 'casado'],
       ['Bruno', 'solteiro']], dtype='<U9')


# 6.3 TAMANHO DE LISTAS
""" 
L = [12, 9, 5]
print(len(L))
 """
# prog 6.4 - repetição com tamanho da lista
l = [1, 2, 3]
x = 0
while x < 3:
    print(l[x])
    x += 1