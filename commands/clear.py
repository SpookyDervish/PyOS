import os

from rich.console import Console


name = "clear"
description = "Clears the console for the user"
min_args = 0
max_args = 0
category = "basic"
admin = False


def run(console: Console, args: list):
    os.system("cls")