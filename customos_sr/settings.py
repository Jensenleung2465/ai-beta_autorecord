import yaml
from rich.console import Console


#<ai>
def load_config():
    with open('config.def.yaml') as f:
        config = yaml.safe_load(f)
    
    console = Console()
    console.print("[bold]Configuration Table:[/bold]")
    
    for section, values in config.items():
        console.print(f"[bold cyan]{section.upper()}[/bold cyan]")
        for key, value in values.items():
            console.print(f"  {key}: [green]{value}[/green]")
        console.print()  # Add empty line between sections
#</ai>

load_config()