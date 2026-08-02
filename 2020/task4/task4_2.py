class Person:
    
    def __init__(self, full_name, date_of_birth):

        self.full_name = full_name
        self.date_of_birth = date_of_birth

    def is_adult(self):

        birth_year = int(self.date_of_birth[:4])
        current_year = 2026

        age = current_year - birth_year

        if age > 18:
            return True

        else:
            return False

    def screen_name(self):

        name = ""

        for char in self.full_name:
            if char.isalpha():
                name += char

        month = int(self.date_of_birth[5:7])
        date = int(self.date_of_birth[8:10])

        return name + month + date
