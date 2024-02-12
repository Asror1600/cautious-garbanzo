class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year


cobalt = Car(color='White', model='Chevrolet', year=2023)
gentra = Car('Ravon', 'Black', 2022)


print(cobalt.model, cobalt.color, cobalt.year)



class Comment:
    def __init__(self, username, text):
        self.username = username
        self.text = text


chel = Comment(username='Bek', text='ogon')
print(chel.text,chel.username)




class User:
    def __init__(self, name, inbox, age, numberphone):
        self.name = name
        self.inbox = inbox
        self.age = age
        self.numberphone = numberphone
    def change_name(self, new_name):
        self.change_name = new



