# Notação BigO
Notação Big O informa o quão rápido é um algoritmo.
Ela não usa segundos ou milisegundos, usa o número de operações para se resolver um algoritmo, esse é o conceito da rapidez de um algoritmo também.
Enquanto uma pesquisa simples tem notação O(n), uma pesquisa binária usa O(log n), o que a torna mais rápida
Apesar de poder haver casos onde uma pesquisa simples ache o item procurado na primeira execução, ela NUNCA será mais 
lenta do que O(n).

## Exercícios
### Forneça o tempo de executação para cada um dos casos a seguir em termos da notação Big O:

1 - Você tem um nome e deseja encontrar o número de telefone para esse nome em uma agenda telefônica
R -> O(log n)

2 - Você tem um número de telefone e deseja encontrar o dono dele em uma agenda telefônica (Dica: Deve procurar pela agenda inteira!)
R -> O(n), já que não seria uma lista ordenada.

3 - Você quer ler o número de cada pessoa da agenda telefônica
R -> O(n)