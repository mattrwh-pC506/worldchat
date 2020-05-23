from exception_handling.exceptions.base import CustomBaseException

class MethodNotSupported(CustomBaseException):
    status_code = 405

    def __init__(self, method):
        self.message = "{} method not supported".format(method)
