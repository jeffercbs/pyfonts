from typing import Dict, Callable, Any, Optional
from pyfonts.cli import ls, fetch, delete


class Cli:
    commands: Dict[str, Callable[..., None]]

    def __int__(self):
        self.commands = {}

    def add_command(self, name: str, action: Dict[..., None]):
        pass

    def add_commands(self, commands: Dict[str, Callable[..., None]]):
        pass

    def execute(self, command: Optional[str], args: Dict[..., Any]):
        pass


cli = Cli()
cli.add_commands({
    "ls": ls,
    "fetch": fetch,
    "delete": delete
})
