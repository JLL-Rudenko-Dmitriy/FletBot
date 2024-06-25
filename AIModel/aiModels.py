from openai import OpenAI as OpenAIClient
import openai
from AIModel.BasePrompt.prompt import Prompt
from AIModel.BaseAI import BaseAI as BAI

class OpenAI(BAI):

    def __init__(self, TOKEN):
        super().__init__(TOKEN)
        
        self.client = OpenAIClient(
            api_key = super().getToken()
        )

        self.__model = 'gpt-3.5-turbo'
    

    def send_text_request(self, prompt: Prompt, max_tokens = 1000, temperature = 0.9):
        super()._send_request(prompt)
        _request = self.__generate_request(prompt)

        response = self.client.chat.completions.create(model = self.__model,
                                                        messages = _request, 
                                                        max_tokens = max_tokens,
                                                        temperature = temperature)
        return response.choices[0].message.content
        

    def __generate_request(self, prompt: Prompt):
        _role = prompt.get_role()
        _messages = []

        if (_role != None):
            _messages.append(self.__add_message_obj("system", _role))

        _messages.append(self.__add_message_obj("user", prompt.build()))

        return _messages
    
    
    def __add_message_obj(self, role, content):
        return {"role": role, "content": content}