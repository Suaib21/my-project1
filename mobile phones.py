class Mobile_phones:
    def __init__(self, phones):
        self.phones = phones

    def list_phones(self):
        print("Available phones ")
        for phone in self.phones:
            print(phone)