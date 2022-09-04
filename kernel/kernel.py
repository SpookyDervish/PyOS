"""
########################################
# KERNEL MAIN
########################################

This file contains the essential functions for the PyOS kernel to work correctly.

The `kmain()` function sets up the process table, interupt vectors, and task schuduling. It then boots the system.
"""


import os
import sys
import pyfiglet
import time
import json

from kernel.globals import Global
from kernel.cmd import handle_command


def kmain():
    try:
        print = Global.console.print
        input = Global.console.input

        os.system("cls")
        print(f"[bold magenta]{pyfiglet.figlet_format('PyOS', font='alligator2')}[/bold magenta]")
        print("[bold green]Booting[/bold green] PyOS..")
        time.sleep(1)
        print("Bootloader found at fs0")
        os.system("cls")
        time.sleep(1)

        data_file = open("data/data.json")
        data = json.load(data_file)

        print("Welcome to [yellow]Py[/yellow][blue]OS[/blue] version [bold white]1.0.0[/bold white]! Type 'help' for a list of commands.")
        print("[dim white](c) Thenna. All rights reserved.[/dim white]")
        print("")

        while True:
            user_input = input(f"[bold green]{data['logged_in']}@{data['computer_name']}[/bold green]:[bold blue]~[/bold blue]$ ")

            handle_command(Global.console, user_input)
    except Exception as e:
        print(os.getcwd())
        print(e)
        input()
        os.system("cls")
        print(f"[bold white reverse]{pyfiglet.figlet_format('PyOS', font='alligator2')}[/bold white reverse]")
        print("")
        print("A severe error has occured while running PyOS and it is unable to recover.")
        print(f"[bold red]ERR: {e.args[0]}[/bold red]")
        print("")
        print("* Press enter to restart")
        print("* Press Ctrl+C to shutdown")
        input("", password=True)
        kmain()
        return