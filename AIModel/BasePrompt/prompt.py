from .Constants.CONST import Formatting, Languages

class Prompt:
    def __init__ (self):
        self.__role     : str = None
        self.__title    : str = None
        self.__content  : str = None
        self.__format   : str = None 
        self.__params   : str = None
        self.__language : str = None 
        self.__result   : str = ""
    
    def set_role(self, role : str):
        self.__role = role
        return self

    def set_title(self, title : str):
        self.__title = title
        return self

    def set_content(self, content : str):
        self.__content = content
        return self

    def set_format(self, format : Formatting = Formatting.NOFM):
        self.__format = format
        self.add_parameter("Formatting", format)
        return self

    def set_language(self, language : Languages):
        self.__language = language
        self.add_parameter("Language", language)
        return self
    
    def add_parameter(self, p_name: str, p_value: str):
        if self.__params is None:
            self.__params = ""
        self.__params += f"{p_name}: {p_value}\n"
        return self

    def get_role(self):
        return self.__role

    def build(self):
        if self.__title is not None:
            self.__result += f"Use this title: {self.__title}\n"

        if self.__content is not None:
            self.__result += f"Content: {self.__content}\n"

        if self.__params is not None:
            self.__result += f"Pay attention to the following parameters for the response:\n{self.__params}"
        
        return self.__result