from poetry.console.application import Application
from poetry.plugins import ApplicationPlugin

from poetry_generate_plugin.commands.generate import GenerateCommand


class GeneratePlugin(ApplicationPlugin):
    def activate(self, application: Application):
        application.command_loader.register_factory(
            "my-command", lambda: GenerateCommand()
        )
