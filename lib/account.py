class Account:
    def __init__(self, email, user_name):
        self.email = email
        self.user_name = user_name

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"User Name:{self.user_name},Email:{self.email}"
