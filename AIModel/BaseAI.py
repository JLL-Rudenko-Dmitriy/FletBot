from AIModel.BasePrompt.prompt import Prompt

class BaseAI:
    def __init__ (self, TOKEN):
        self.__TOKEN = TOKEN
    
    def __validate_request(self, prompt: Prompt = None):
        if prompt == None or not(isinstance(prompt, Prompt)):
            raise RuntimeError("prompt can't be None or not instance of class Prompt")
        return True
    
    def _send_request(self, prompt: Prompt):
        if not(self.__validate_request(prompt)):
            return None
        
    def getToken(self):
        return self.__TOKEN
    