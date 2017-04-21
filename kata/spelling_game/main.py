# coding=utf-8
"""
Start with a list of words.

Remove a letter at random. Have the user guess the correct spelling of the word.

Run in two modes- where the user must give the intended letter, or where the user
gives any letter that creates an English word. (English being any word on the list,
there is no time to type a real dictionary!)
"""

from __future__ import print_function, unicode_literals, absolute_import

# configure logging for file and console output.
import logging
import os.path
from random import randint, choice
from string import ascii_letters
if os.path.isfile("log.txt"):
    os.remove("log.txt")
logging.basicConfig(filename='log.txt', level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler())

# strongly discourage using console input and output.
# You can make testable code full of input and print statements, but it introduces
# unnecessary complexity. See kata on testing input and print with fakes
# and spies.


def input(*args, **kwargs):
    raise TypeError(
        "Don't use input, log or get input from function arguments.")


def raw_input(*args, **kwargs):
    raise TypeError(
        "Don't use raw_input, either, log or get input from function arguments.")


def run():
    """
    Main entry point for your application.
    """
    words = ['Intended', 'letter', 'apple', 'red', 'create', 'pear', 'fruit']

    while True:
        mode = randint(0, 1)
        print("Select a mode (0 - guess the correct spelling of the word; 1 - create new word): ", mode)
        # try:
        #     mode = int(input(
        #         "Select a mode (0 - guess the correct spelling of the word; 1 - create new word): "))
        # except ValueError:
        #     print("That is not integer!")
        #     continue

        if mode == 0:
            guess_the_word(words)
        elif mode == 1:
            create_word(words)
        else:
            print("Wrong mode!")

        while True:
            char = 'n'  # input("Repeat game? (y/n): ")
            print("Repeat game? (y/n): ", char)
            if char == 'n':
                return
            elif char == 'y':
                break
            else:
                print("only 'y' or 'n'")
                continue
    return

# the functions/classes you write here should have no print or input
# statements.


def guess_the_word(words):
    '''Docstring'''
    rand_word = words[randint(0, len(words) - 1)].lower()
    rand_letter = randint(0, len(rand_word) - 1)
    incorrect_word = rand_word[:rand_letter] + rand_word[rand_letter + 1:]
    attempts = 5
    for i in range(attempts):
        print("Guess correct spelling of the word '{0}' (attempt #{1}): ".format(
            incorrect_word, i + 1))
        guess = words[randint(0, len(words) - 1)].lower()
        print(guess)
        # guess = input(
        #     "Guess correct spelling of the word '{0}' (attempt #{1}): ".format(incorrect_word, i + 1)).lower()
        if guess == rand_word:
            print("You are winner!")
            return
        else:
            if i == attempts - 1:
                print("Game over!")
                return


def create_word(words):
    '''Docstring'''
    letter = None
    good_words = []
    while True:
        letter = choice(ascii_letters).lower()
        print("Give me one letter for creation of word: ", letter)
        # letter = input("Give me one letter for creation of word: ").lower()
        if not letter.isalpha() and len(letter) == 1:
            print(
                "It's not one letter or not alphabetical. Try again, please.")
            continue
        for word in words:
            # if word.lower().startswith(letter):
            if letter in word.lower():
                good_words.append(word)

        if good_words:
            print(good_words[randint(0, len(good_words) - 1)])
            return
        else:
            print(
                "We don't have words that start with '{}'. Try to give other letter.".format(letter))


if __name__ == "__main__" or __name__ == "builtins":
    # Need an environment to run this?
    # https://repl.it/languages/python3
    logging.info("The application is starting.")
    run()
