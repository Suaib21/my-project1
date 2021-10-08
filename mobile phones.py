class Mobile_phones:
    iphone="iphone 13 pro"
    def __init__(self, phones):
        self.phones = phones
        print(self.iphone)
        print(self.phone)
        

    def list_phones(self):
        print("Available phones ")
        for phone in self.phones:
            print(phone)
