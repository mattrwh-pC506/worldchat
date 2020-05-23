from exception_handling.exceptions.base import CustomBaseException

class UsernameTaken(CustomBaseException):
    status_code = 400

    def __init__(self, username):
        super().__init__(username)
        self.message = "{} is taken".format(username)

class IncorrectPassword(CustomBaseException):
    status_code = 401
    message = "bad password"

class UserDoesNotExist(CustomBaseException):
    status_code = 401
    message = "bad username"
