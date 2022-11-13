
class GlobalState:
    def __init__(self):
        self.authenticated = False

    def setAuthenticated(self, value:bool)->None:
        self.authenticated = value

    def getAuthenticated(self)->bool:
        return self.authenticated