# Ordenação por Seleção

Basicamente aqui há um comparativo de duas formas de criar conjuntos de dados: Arrays e Listas Encadeadas.

## Arrays

Você reserva um espaço de memória para colocar o seu item. 

### Vantagens

O que você deseja é atendido, porém não é sempre que vai haver espaço de memória junto aos outros itens.

### Desvantagens

É preciso realocar os outros itens caso você queira adicionar mais um e esse espaço de memória estiver ocupado.

## Listas Encadeadas

Os itens são alocados onde há espaço de memória livre, não precisando que estejam juntos. Cada espaço de memória vai alocar também o endereço do próximo item da lista.

### Vantagens

Listas encadeadas permitem que os itens sejam salvos onde quer que haja espaço disponível.

### Desvantagens

Não é possível acessar diretamente o último item da lista, ou o penúltimo pois não há endereço exposto. Você precisaria acessar o primeito item para saber o espaço do segundo e assim por diante.

## Terminologia

O tempo de dexecução para operações comuns de arrays e listas:

Arrays tem tempo de leitura de O(1), enquanto de inserção tem O(n).
Listas tem tempo de leitura de O(n), enquanto de insercção tem O(1).

O(n) = tempo de execução linear.
O(1) = tempo de execução constante.

## Inserindo algo no meio da lista

No caso das listas, basta inserir o item no espaço de memória que o item anterior estava apontando.

Já nos arrays, deve-se mover todos os itens que estão abaixo do endereço de inserção. Caso não haja local, é preciso mover tudo para um novo local. Ou seja, listas são melhores nesses casos.

## Deleções

As listas ainda serão melhores já que é preciso apenas mudar o endereço para o qual o elemento anterior está apontando.

## Qual é mais usado?

Depende do caso, mas os arrays são mais comuns por permitirem acesso aleatório. Existem dois tipos de acessos: aleatórios e sequenciais.

### Acesso Sequencial

Você lê os elementos um por um, começando pelo primeiro. Listas encadeadas só podem lidar com acesso sequencial.

### Acesso Aleatório

Permite pular direto para o décimo item. Muitos dos casos requerem o acesso aleatório, o que faz os arrays serem mais utilizados.