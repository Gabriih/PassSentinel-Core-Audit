import getpass
import sys
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

console = Console()

def show_banner():
    console.print(
        Panel.fit(
            "[bold cyan]PASS-SENTINEL[/bold cyan] [green]v0.1.0[/green]\n"
            "[dim]Auditoria de Segurança e Análise Criptográfica de Senhas[/dim]",
            border_style="cyan"
        )
    )

def check_single_password():
    console.print("\n[yellow]Digite a senha para a checagem:[/yellow]")
    password = getpass.getpass("Senha: ")

    if not password:
        console.print("[red]Erro: Senha não pode ser vazia[/red]")
        return

    console.print("\n[cyan]Analisando sua senha...[/cyan]")

    #insira aqui o codigo para checagem da senha, vai ficar uma mensagem de debug por enquanto
    console.print(f"[dim]Tamanho da senha:[/dim] {len(password)}")

def main():
    show_banner()

    while True:
        console.print("\n[bold]Selecione uma opção:[/bold]")
        console.print("1. Checar uma senha")
        console.print("2. Checar um arquivo em lote")
        console.print("3. Sair")

        choice = Prompt.ask("Escolha", choices=["1", "2", "3"], default="1")

        if choice == "1":
            check_single_password()
        elif choice == "2":
            console.print("[yellow]Modulo ainda em desenvolvimento...[/yellow]")
        elif choice == "3":
            console.print("[cyan]Encerrando programa...[/cyan]")
            sys.exit(0)

if __name__ == "__main__":
    main()