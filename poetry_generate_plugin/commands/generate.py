from cleo.helpers import option
from poetry.console.commands.command import Command
from poetry.vcs.git import Git


class GenerateCommand(Command):
    name = "generate"
    description = "Generates a new Poetry project from any valid "

    options = [
        option(
            "source",
            "s",
            "The repository source",
            flag=False,
        ),
    ]

    def handle(self) -> int:
        source = self.option("source")

        repo = Git.clone(source)

        return 0
