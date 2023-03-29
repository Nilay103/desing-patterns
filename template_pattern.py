"""Template pattern lives here."""

class DBRecord:
    def validate(self):
        pass

    def save(self):
        self.validate()
        print("obj stored successfully.") # db write call.


class User(DBRecord):
    def validate(self):
        print("custom validation check logic.")
        pass


user: User = User()
user.save()
