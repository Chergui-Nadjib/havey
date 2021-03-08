"""
Module for generate interface for your console applications.

Functions:
    bcolored: background colored text
    unicolored: background & foreground colored text
    cinput: colored input
    colored: return colored text
    cwelcome: return colored from welcome function
    error: return red colored message
    warning: return yellow colored message
    welcome: return star border message
    init: run colorama init for windows console
"""

import sys
import time
import colorama


def colored(text, color):
    if color == "blue":
        color = colorama.Fore.BLUE
    if color == "red":
        color = colorama.Fore.RED
    if color == "black":
        color = colorama.Fore.BLACK
    if color == "white":
        color = colorama.Fore.WHITE
    if color == "cyan":
        color = colorama.Fore.CYAN
    if color == "blue":
        color = colorama.Fore.BLUE
    if color == "yellow":
        color = colorama.Fore.YELLOW
    if color == "lightblack":
        color = colorama.Fore.LIGHTBLACK_EX
    if color == "lightyellow":
        color = colorama.Fore.LIGHTYELLOW_EX
    if color == "lightcyan":
        color = colorama.Fore.LIGHTCYAN_EX
    if color == "lightblue":
        color = colorama.Fore.LIGHTBLUE_EX
    if color == "green":
        color = colorama.Fore.GREEN

    return color+text+colorama.Style.RESET_ALL


def bcolored(text, color):
    if color == "blue":
        color = colorama.Back.BLUE
    if color == "red":
        color = colorama.Back.RED
    if color == "black":
        color = colorama.Back.BLACK
    if color == "white":
        color = colorama.Back.WHITE
    if color == "cyan":
        color = colorama.Back.CYAN
    if color == "blue":
        color = colorama.Back.BLUE
    if color == "yellow":
        color = colorama.Back.YELLOW
    if color == "lightblack":
        color = colorama.Back.LIGHTBLACK_EX
    if color == "lightyellow":
        color = colorama.Back.LIGHTYELLOW_EX
    if color == "lightcyan":
        color = colorama.Back.LIGHTCYAN_EX
    if color == "lightblue":
        color = colorama.Back.LIGHTBLUE_EX
    if color == "green":
        color = colorama.Back.GREEN

    return color+text+colorama.Style.RESET_ALL


def unicolored(text, bg, fg):
    return colored(bcolored(text, bg), fg)


def error(text):
    stars = ""
    return colored(f"Error: {text}", "red")


def warning(text):
    return colored(text, "lightyellow")


def init():
    colorama.init(wrap=True)


def welcome(text):
    stars = ""
    for _ in range(len(text)+4):
        stars += "*"
    return f"{stars}\n* {text} * \n{stars}"


def cwelcome(text, color):
    return colored(welcome(text), color)


def progress(text):
    print(colored(text, "lightyellow"), end="")
    sys.stdout.flush()
    for a in range(3):
        time.sleep(1)
        print(colored(".", "lightyellow"), end="")
        sys.stdout.flush()
    print("")


def main_menu(text):
    menu = "Choose a number:\n\n"
    menu = colored(menu, "lightcyan")
    counter = 0
    for _ in range(len(text)):
        counter += 1
        menu += f"\t{counter}. {text[counter-1]}\n"
    return menu


def imain_menu(text, itext):
    print(main_menu(text))
    return input(itext)


def icmain_menu(text, itext, color):
    return imain_menu(text, colored(itext, color))
