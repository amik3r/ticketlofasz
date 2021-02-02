class User:
    def __init__(self, role='', groups=[], permissions='00000000'):
        self.role = role
        self.groups = groups
        self.permissions = permissions

class NaturalUser(User):
    def __init__(self, firstname, lastname, email):
        super().__init__()
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

class ServiceUser(User):
    def __init__(self, name, can_login=False, has_password=False, api_key=None):
        super().__init__(self)

