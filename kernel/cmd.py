from ast import arg
import os
import imp

from rich.console import Console


def handle_command(console: Console, command: str):
    split_string = command.split(" ")
    command_name = split_string[0]
    command_name = command_name.lower()

    args = []

    for i in range(1, len(split_string)):
        if split_string[i].startswith('"'):
            res = ""

            pos = i

            while pos <= len(split_string):
                try:
                    res += f"{split_string[pos]} "
                except IndexError:
                    console.print(f"[bold red]ERR: Unterminated string in command arguments[/bold red]")
                    return False
                if split_string[pos].endswith('"'):
                    break
                pos += 1

            if pos == len(split_string):
                if not split_string[pos].endswith('"'):
                    console.print(f"[bold red]ERR: Unterminated string in command arguments[/bold red]")
                    return False

            res = res.replace('"', "")

            args.append(res)
            continue

        args.append(split_string[i])

    commands_dir = os.path.join(os.getcwd(), "commands")
    
    if os.path.exists(commands_dir) and os.path.isdir(commands_dir):
        for f in os.listdir(commands_dir):
            if os.path.isfile(os.path.join(commands_dir, f)):
                try:
                    cmd = imp.load_source(command_name, os.path.join(commands_dir, f))

                    if cmd.name == command_name:
                        if cmd.min_args <= len(args):
                            if cmd.max_args >= len(args):
                                cmd.run(console, args)

                                return True
                            else:
                                console.print(f"[bold red]ERR: {command_name} takes a maximum of {cmd.max_args} arguments[/bold red]")
                                return False
                        else:
                            console.print(f"[bold red]ERR: {command_name} requires atleast {cmd.min_args} argument[/bold red]")
                            return False
                except Exception as e:
                    console.print(f"[bold red]ERR: An error occured while running this command[/bold red]")
                    return False

        console.print(f"[bold red]ERR: Invalid or unkown command '{command_name}'[/bold red]")
        return False
    else:
        raise FileNotFoundError("Commands directory is corrupted or does not exist")