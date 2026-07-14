from rich.console import Console
from rich.panel import Panel
from rich.align import Align

console = Console()

# 1. Create your centered content
centered_text = Align.center("This text is perfectly centered!")

# 2. Pass it directly into the Panel
panel = Panel(centered_text, title="My Panel")

console.print(panel)