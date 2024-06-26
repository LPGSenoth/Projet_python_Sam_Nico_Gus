print("jet taime vraiment c est pas une blague ")

class personne:
    def __init__(self,name,age):
        self.name = name
        self.age = age


    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set(self,name,age):
        self.name = name
        self.age = age

class Sportif:
    def __init__(self):