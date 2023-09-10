"""
Nesse exercicio faço o jogo TERMOO importando a biblioteca random para escolher aleatoriamente de um arquivo que no caso é a "lista_palavras.txt"
"""

import random

def escolher_palavra():
    with open("lista_palavras.txt", "r") as arquivo:
        palavras = arquivo.readlines()
    return random.choice(palavras).strip()

def mostrar_palavra(palavra, letras_corretas):
    resultado = ""
    for letra in palavra:
        if letra in letras_corretas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado

def jogar_forca():
    palavra = escolher_palavra().upper()
    letras_corretas = []
    letras_usadas = [] 
    tentativas = 6

    print("Bem-vindo ao jogo da Forca!")
    print(f"A palavra tem {len(palavra)} letras.")
    
    while tentativas > 0:
        print("\nPalavra: " + mostrar_palavra(palavra, letras_corretas))
        print("Tentativas restantes:", tentativas)
        print("Letras usadas:", ", ".join(letras_usadas))  
        letra = input("Digite uma letra: ").upper()
        
        if letra in letras_usadas:
            print("Você já tentou essa letra.")
        else:
            letras_usadas.append(letra) 
            if letra in palavra:
                letras_corretas.append(letra)
                if len(set(letras_corretas)) == len(set(palavra)):
                    print("Você venceu! A palavra era:", palavra)
                    break
            else:
                tentativas -= 1
                print("Letra incorreta. Tente novamente.")

    if tentativas == 0:
        print("Você perdeu! A palavra era:", palavra)

if __name__ == "__main__":
    jogar_forca()
