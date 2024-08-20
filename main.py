import random
import hangman_art
import hangman_words
import logo
import os
import time

def EveryTimeList():
    wordlength = len(ThisGameWord)
    empty_list = ['_'] * wordlength
    return empty_list

def clear_console():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Mac and Linux (os.name is 'posix')
    else:
        _ = os.system('clear')
def whatUguess():
    print(' '.join(list_1))


def SnowChecker(char):
    return char in ThisGameWord


def replace_item(lst, char):
    indices = [index for index, value in enumerate(ThisGameWord) if value == char]
    for index in indices:
        lst[index] = char


ThisGameWord = random.choice(hangman_words.word_list)
# print(f"Pssst, the solution is {ThisGameWord}.")  # لأغراض التحقق فقط

counter = 0
WinOrLose = False
list_1 = EveryTimeList()
Guess = ''
lives = 6

while lives >= 0 and '_' in list_1:
    Guess = input("Guess a letter: ").lower()
    clear_console()
    if SnowChecker(Guess) and Guess not in list_1:
        replace_item(list_1, Guess)
        from hangman_art import stages
        print(stages[lives])
    else:
        from hangman_art import stages
        print(stages[lives])
        lives -= 1
    whatUguess()
if '_' not in list_1:
    print("Congratulations, you win!")
else:
    print("Sorry, you lost. The word was:", ThisGameWord)
