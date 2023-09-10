"""
Nessa questão eu repito o mesmo codigo da questão anterior e as mesmas funções a unica diferença que implemento mais uma função fazendo 
o jogador entrar com o numero de linhas e colunas.
"""


import random

def print_board(board):
    for row in board:
        print(" | ".join(row))  
        print("-" * (4 * len(board[0]) + 1))  

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(len(board[0])):
        if all(board[row][col] == player for row in range(len(board))):
            return True

    if all(board[i][i] == player for i in range(min(len(board), len(board[0])))) or all(
            board[i][len(board[0]) - 1 - i] == player for i in range(min(len(board), len(board[0])))):
        return True

    return False

def is_full(board):

    return all(cell != " " for row in board for cell in row)

def get_empty_cells(board):

    empty_cells = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == " ":
                empty_cells.append((row, col))
    return empty_cells

def computer_move(board): 
    empty_cells = get_empty_cells(board)
    return random.choice(empty_cells)

def main():
    try:
        rows = int(input("Digite o número de linhas: "))
        cols = int(input("Digite o número de colunas: "))

        board = [[" " for _ in range(cols)] for _ in range(rows)]
        winner = None

        print(f"Bem-vindo ao Jogo da Velha {rows}x{cols} contra a IA!")
        print_board(board)

        while not winner and not is_full(board):
            try:
                print("Sua vez!")
                row = int(input(f"Digite o número da linha (1-{rows}): ")) - 1
                col = int(input(f"Digite o número da coluna (1-{cols}): ")) - 1

                if 0 <= row < rows and 0 <= col < cols and board[row][col] == " ":
                    board[row][col] = "X"
                    print_board(board)

                    if check_winner(board, "X"):
                        winner = "Você"
                    else:
                        print("Vez da IA...")
                        ai_row, ai_col = computer_move(board)
                        board[ai_row][ai_col] = "O"
                        print_board(board)

                        if check_winner(board, "O"):
                            winner = "IA"

                else:
                    print("Essa posição não é válida ou já está ocupada. Tente novamente.")

            except (ValueError, IndexError):
                print("Entrada inválida. Certifique-se de digitar um número de linha e coluna válido.")

        if winner:
            print(f"{winner} venceu!")
        else:
            print("Empate! O jogo terminou sem vencedor.")

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar um número inteiro válido para o número de linhas e colunas.")

if __name__ == "__main__":
    main()
