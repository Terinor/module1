from .interface import UserInterface

class NoteDisplay(UserInterface):
    def display(self, notes):
        for note in notes:
            print(f"Note: {note}")