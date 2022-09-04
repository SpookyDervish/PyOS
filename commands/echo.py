from rich.console import Console


name = "echo"
description = "Echos the specified text back to the user"
min_args = 1
max_args = 99999
category = "basic"
admin = False


def run(console: Console, args: list):
    console.print(args[0])