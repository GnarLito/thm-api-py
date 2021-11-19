
class NotImplemented(Exception):
    pass

class NotValidUrlParameters(Exception):
    def __init__(self, e):
        self.e = e
    def __str__(self):
        return self.e

class WebError(Exception):
    def __init__(self, r, data):
        self.request = r
        self.data = data
    
    def __str__(self):
        return f"{type(self).__name__}(code={self.request.status_code}, return_URL={self.request.url.__str__()}, data_length: {self.data.__len__()})"

class Unauthorized(WebError):
    pass

class ServerError(WebError):
    pass

class NotFound(WebError):
    pass