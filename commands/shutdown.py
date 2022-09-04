import sys
import time

from rich.console import Console
from kernel.kernel import kmain


name = "shutdown"
description = "Shutdowns PyOS"
min_args = 1
max_args = 2
category = "system"
admin = False


def run(console: Console, args: list):
    global mode, delay, int_delay

    if args[0] == "/r":
        mode = "restart"
    elif args[0] == "/s":
        mode = "shutdown"
    elif args[0] == "/t":
        mode = "delay"

        if len(args) > 1:
            delay = args[1]

            try:
                int_delay = int(delay)
            except ValueError:
                console.print(f"[bold red]ERR: Expected integer not string when specifing delay[/bold red]")
                return
        else:
            console.print(f"[bold red]ERR: Delay mode selected but no delay specified[/bold red]")
            return
    else:
        console.print(f"[bold red]ERR: Invalid argument '{args[0]}'[/bold red]")
        return

    if mode == "shutdown":
        console.print("[bold green]Downing[/bold green] PyOS..")
        time.sleep(1)
        sys.exit(0)
    elif mode == "restart":
        console.print("[bold green]Restarting[/bold green] PyOS..")
        time.sleep(1)
        kmain()
    elif mode == "delay":
        console.print(f"[bold blue]INFO[/bold blue] PyOS will shutdown in {delay} seconds")
        time.sleep(int_delay)
        console.print("[bold green]Downing[/bold green] PyOS..")
        time.sleep(1)
        sys.exit(0)

    sys.exit()