from rich.console import Console
import platform

def help() :
    help_table = Table(title="How To Use?")
    help_table.add_column("command", justify="right", style="cyan", no_wrap=True)
    help_table.add_column("Can", style="magenta")
    help_table.add_column("os version")
    help_table.add_row("help", "go to there", "v1.0.0.1 dev")
    help_table.add_row("pull", "download file at network", "v1.0.0.1 dev")
    help_table.add_row("logout", "logout device", "v1.0.0.1 dev")
    help_table.add_row("shutdown", "close your device", "v1.0.0.1 dev")
    console = Console()
    console.print(help_table)


def info() :
    table = Table(title="BOIS Info")
    table.add_column("Name", justify="right", style="cyan", no_wrap=True)
    table.add_column("Value")
    table.add_row("Machine", platform.machine())
    table.add_row("Version", platform.version())
    table.add_row("Platform", platform.platform())
    table.add_row("System", platform.system())
    table.add_row("Processor", platform.processor())
    console = Console()
    console.print(table)
    with open("config.def.yaml", "r") as file :
        config = yaml.safe_load(file)
    table = Table(title="ai Info(Powered by customos_lite? )") 
    table.add_column("Name", justify="right", style="cyan", no_wrap=True)
    table.add_column("Value")
    table.add_row("Name", config['settings']['name'])
    table.add_row("SN-CODE", config['system']['sn-code'])
    table.add_row("GTIMESTAMP", platform.platform())
    table.add_row("Version", platform.system())
    table.add_row("Processor", platform.processor())
    table.add_row("email", "info@givemetocode.com")
    console = Console()
    console.print(table)
