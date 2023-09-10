# Avaliativa

Exercicio 1:

- A função def tabuleiro serve para imprimir o tabuleiro do jogo da velha 4x4.

Já o argumento board (list) faz o tabuleiro do jogo representado com uma lista de listas, usados em todas as funções

- A função def vencedor verifica se um jogador venceu o jogo.

O argumento player (str) leva em consideração X o player e O como o computador

E retorna booleano se caso for True o jogador vence e False caso contrario e a maquina ganhe

- A função def fileira_c verifica se o tabuleiro está completamente preenchido.

Retorna booleano se caso for True o tabuleiro esta cheio e False caso contrario

- A função def fileira_v obtém uma lista das células vazias no tabuleiro.

Retorna uma lista com coordenadas (linhas e colunas) das células vazias

- A função def computador faz o computador ou IA fazer uma jogada aleatória.

Retorna uma tupla das coordenadas (linha e coluna) das jogadas do computador 

- A função main é a função principal que executa o jogo da velha 4x4 com um usuário jogando contra o computador.

O loop while usado serve para rodar até haver um vencedor ou empate.


Exercicio 2:

- Todas as funções são as mesmas da questão anterior

- A unica diferença é que criado junto no main um print para ler a quantidade de linhas e colunas para o usuario entrar


Exercicio 3:

- A função def escolher_palavra nessa função ela puxa uma palavra aleatoria de um arquivo aleatorio

Então vai retornar de uma pasta criada noemada lista_palavras aleatoriamente 

- A função def mostra_palavra monta a representação da palavra secreta com as letras corretamente adivinhadas.

Os argumentos dentro dessa função são: palavra (str): A palavra secreta e letras_corretas (list): Lista de letras corretamente adivinhadas.

Retornando a representação da palavra com letras corretas e "-" para letras para adivinhar ainda.

- A função def jogar_forca inicia e executa o jogo da Forca.

O jogador tenta adivinhar a palavra oculta dentro do limite de tentativas permitidas.

- E dentro do main foi criado um paramentro para mostras as letras que ja foram usadas no decorrer do jogo

Exercicio 4:

- A função def cadastrar_usuarios cadastra um novo usuário no banco de dados.

Utilizando como argumentos dentro da função campos_obrigatorios uma lista de strings com os campos obrigatórios para o cadastro.
    
O usuário será solicitado a inserir valores para os campos obrigatórios e poderá adicionar campos adicionais até decidir encerrar o cadastro. Os dados do usuário são armazenados no banco de dados.

- A função def imprimir_usuarios imprime a lista de usuários cadastrados no banco de dados.

Para cada usuário, esta função imprime todos os campos e seus respectivos valores.    