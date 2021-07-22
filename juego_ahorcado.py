import os
import random

IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def words():
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        secret_word = random.choice([i for i in f]).upper().strip()
        print(secret_word)
        return secret_word

def game(hidden_word, tries):
    print(IMAGES[tries])
    print("")
    print(hidden_word)


def run():
  print("""
    _________________________________________________________________________

    Bienvenido al juego del ahorcado.

    El objetivo del juego es adivinar la palabra secreta letra por letra.

    Tienes 7 vidas, pierdes una vida cada que te equivocas.

    Si te quedas sin vidas, pierdes.
    _________________________________________________________________________""")
  word = words()
  hidden_word = "_" * len(word)
  tries = 0

  while True:
    game(hidden_word, tries)
    letter = str(input("Escoge una letra: ")).upper()
    print(letter)

    ind_letter = []
    for i in range(len(word)):
      if letter == word[i]:
        ind_letter.append(i)

    if len(ind_letter) == 0:
      tries += 1

     #Aqui esta el error.
    else:
      for i in ind_letter:
       hidden_word[i] = letter

    ind_letter = []



if __name__ == "__main__":
  run()