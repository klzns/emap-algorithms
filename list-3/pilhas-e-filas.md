> Discutir a implementação de pilhas e filas com listas encadeadas ou arrays. Vantagens, desvantagens, custo das operações básicas nestas estruturas.

# Pilhas
É um tipo abstrato de dados do tipo "Last In, First Out", ou seja, o último elemento a entrar, é o primeiro a sair.
Uma pilha seria mais eficiente implementada utilizando a estrutura de uma lista encadeada, já que o custo para adicionar e retirar um elemento do início da lista é de O(1), pois é necessário apenas trocar a referência para o início da lista.
Utilizando um array para implementar uma pilha seria vantajoso apenas se fosse guardada uma referência ao último elemento do array, fazendo com que as operações de inserção e remoção tenham custo O(1). Caso contrário, tais operações teriam um custo O(n). 

# Filas
É um tipo abstrato de dados do tipo "First In, First Out", ou seja, o primeiro elemento a entrar, é o primeiro a sair.
Utilizando uma lista encadeada em sua implementação seria vantajoso no momento de inserção de um novo elemento no fim da fila, já que tal operação tem custo O(1). Porém, seria desvantajoso no momento de remoção de um elemento da fila, já que teria que percorrer toda ela até achar o elemento a ser retirado, fazendo com essa operação tenha custo O(n). Esse custo poderia ser reduzido a O(1) caso uma referência ao último elemento fosse sempre armazenada.
Utilizando um array para implementar uma fila seria desvantajoso já que inserir um novo elemento no final array tem custo O(n), pois teria que ser percorrido todo array até encontrar o primeiro espaço vazio para inserção do novo valor. O custo de remover o primeiro elemento do array é de O(n), já que todos os outros elementos devem se realocar para uma posição em direção ao início do array.

Em nenhum dos dois casos foi citado a limitação do espaço de memória de um array, já que essa estrutura aloca os dados de forma contígua na memória. Isso significa que caso o limite de espaço do array seja ultrapassado, deve ser criado um novo array com um tamanho maior, essa operação custaria O(n), pois ela teria que copiar todos os valores para o novo array.