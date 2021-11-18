
class NotImplemented(Exception):
    pass
class WebError(Exception):
    def __init__(self, r, data):
        self.request = r
        self.data = data
    
    def __str__(self):
        return f"{self.request.status} {self.request.url.__str__()}, data length: {self.data.__len__()}"

class Unautherized(WebError):
    pass

class ServerError(WebError):
    pass

class NotFound(WebError):
    pass