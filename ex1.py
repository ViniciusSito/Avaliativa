"""
    Neste exercicio é um jogo de xadrez simples, 4x4. Mas estava em duvida se era um usuario contra o outro ou contra a maquina. 
    Preferi fazer contra a maquina para ser mais dinâmico.
    Utilizei | e - para separar os espaços de cada letra para as jogadas feitas 
    As teclas para selecionar para jogar é do 1 até o 4
    Você começa jogando e então o computador faz a jogada logo em seguida sem pausas
    Utilizei a biblioteca random para as jogadas do computador serem aleatorias
"""


import random

def tabuleiro(board):
    for row in board:
        print(" | ".join(row))  
        print("-" *13) 

def vencedor(board, player):

    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(4):
        if all(board[row][col] == player for row in range(4)):
            return True
        
    if all(board[i][i] == player for i in range(4)) or all(board[i][3 - i] == player for i in range(4)):
        return True

    return False

def fileira_c(board):

    return all(cell != " " for row in board for cell in row)

def fileira_v(board):
    empty_cells = []
    for row in range(4):
        for col in range(4):
            if board[row][col] == " ":
                empty_cells.append((row, col))
    return empty_cells

def computador(board):
    empty_cells = fileira_v(board)
    return random.choice(empty_cells)

def main():
    board = [[" " for _ in range(4)] for _ in range(4)]
    winner = None
    
    tabuleiro(board)  

    while not winner and not fileira_c(board):
        try:
            print("Sua vez!")
            row = int(input("Digite o número da linha (1-4): ")) - 1
            col = int(input("Digite o número da coluna (1-4): ")) - 1

            if board[row][col] == " ":
                board[row][col] = "X"  
                tabuleiro(board)

                if vencedor(board, "X"): 
                    winner = "Você"
                else:
                    print("Vez da Máquina")
                    ai_row, ai_col = computador(board)
                    board[ai_row][ai_col] = "O" 
                    tabuleiro(board)

                    if vencedor(board, "O"):  
                        winner = "Computador"

            else:
                print("Essa posição já está ocupada. Tente novamente.")

        except (ValueError, IndexError):
            print("Entrada inválida. Certifique-se de digitar um número de linha e coluna válido.")

    if winner:
        print(f"{winner} venceu!")
    else:
        print("Empate! O jogo terminou sem vencedor.")

if __name__ == "__main__":
    main()

