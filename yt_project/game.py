import random
from rich.console import Console
console = Console()

item_list = ["Rock", "Paper", "Scissor"]

comp_choice = random.choice(item_list)

def Game():
    user_choice = input("Enter your move = Rock, Paper, Scissor :: ")
    if user_choice == "Rock":
        if comp_choice == "Rock":
            console.print("[bold yellow]Tie[/bold yellow]")
        elif comp_choice == "Scissor":
            console.print("[bold green]user win[/bold green]") 
        elif comp_choice == "Scissor":
            console.print("[bold red]computer win[/bold red]")
        else:
            console.print("[red]invalid chioce, Try it again[red]")
    elif user_choice == "Paper":
        if comp_choice == "Paper":
            console.print("[bold yellow]Tie[/bold yellow]")
        elif comp_choice == "Rock":
            console.print("[bold green]user win[/bold green]")
        elif comp_choice == "Scissor":
            console.print("[bold red]computer win[/bold red]")
        else:
            console.print("[red]invalid chioce, Try it again[red]")
    elif user_choice == "Scissor":
        if comp_choice == "Scissor":
            console.print("[bold yellow]Tie[/bold yellow]")
        elif comp_choice == "Paper":
            console.print("[bold green]user win[/bold green]")
        elif comp_choice == "Rock":
            console.print("[bold red]computer win[/bold red]")
        else:
            console.print("[red]invalid chioce, Try it again[/red]")
    else:
        console.print("[red]Try it again[/red]")
    
    
    print(f"User Choice : {user_choice}")
    print(f"computer Choice : {comp_choice}")

Game()