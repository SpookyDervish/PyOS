import os
import imp

from rich.console import Console
from rich.table import Table


name = "help"
description = "Displays a help message to the screen"
min_args = 0
max_args = 0
category = "basic"
admin = False


def run(console: Console, args: list):
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("Name", min_width=20)
    table.add_column("Category", min_width=12)
    table.add_column("Description", min_width=20)

    commands_dir = os.path.join(os.getcwd(), "commands")

    if os.path.exists(commands_dir) and os.path.isdir(commands_dir):
        for f in os.listdir(commands_dir):
            if os.path.isfile(os.path.join(commands_dir, f)):
                cmd = imp.load_source(f, os.path.join(commands_dir, f))

                table.add_row(cmd.name, cmd.category, cmd.description)

        console.print(table)
    else:
        raise FileNotFoundError("Commands directory is corrupted or does not exist")