from datetime import date, timedelta


class Student:
    """ A Student class as a basis for method testing """

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.start_date = date.today()
        self.enf_date = date.today() + timedelta(days=365)
        self.naughty_list = False

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def email(self):
        return f"{self.first_name.lower()}.{self.last_name.lower()}@email.com"

    def alert_santa(self):
        self.naughty_list = True
