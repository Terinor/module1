from .interface import UserInterface

class ContactDisplay(UserInterface):
    def display(self, contacts):
        for contact in contacts:
            print(f"Contact: {contact}")