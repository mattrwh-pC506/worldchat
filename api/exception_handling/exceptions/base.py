class CustomBaseException(Exception):
    status_code = None
    message = None
    def __init__(self, message):
        self.message = message
