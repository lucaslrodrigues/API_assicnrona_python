class Token():
    def __init__(self) -> None:
        self.token = None
        pass
    
    def generate_token(self) -> str:
        self.token = "fake_token"
        return self.token
    
    def get_token(self) -> str:
        return self.token