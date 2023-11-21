from .interface import UserInterface

class HelpDisplay(UserInterface):
    def display(self, help_text):
        print(help_text)