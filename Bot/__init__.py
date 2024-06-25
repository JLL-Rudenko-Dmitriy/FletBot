# class CallbackQuery:
#     def __init__(self, query) -> None:
#         self.callback_id : int = query.id
#         self.callback_data : str = query.data

#         self._message = query.message
#         self.message_id = self._message.id
#         self.text : str = self._message.text
#         self.date : int = self._message.date
#         self.chat_id : int = self._message.chat.id
        
#         self._user = query.from_user
#         self.user_id = self._user.id.user_id
#         self.is_bot = self._user.id.is_bot
#         self.first_name = self._user.id.first_name
#         self.last_name = self._user.id.last_name
#         self.username = self._user.id.username
#         self.language_code = self._user.id.language_code
#         self.is_premium = self._user.id.is_premium

# class MessageQuery:
#     def __init__(self, message) -> None:
#         print(message)
#         self.message_id : int = message.id
#         self.text : str = self.message.text
#         self.date : int = self.message.date
#         self.chat_id : int = self.message.chat.id
        
#         self._user = message.from_user
#         self.user_id = self._user.id.user_id
#         self.user_is_bot = self._user.id.is_bot
#         self.user_first_name = self._user.id.first_name
#         self.user_last_name = self._user.id.last_name
#         self.username = self._user.id.username
#         self.user_language_code = self._user.id.language_code
#         self.user_is_premium = self._user.id.is_premium 

# def msg(func):
#     async def message_handler(message, bot):
#         msgQ = MessageQuery(message=message)
#         await func(message, bot)
#     return message_handler

# def call(func):
#     def callback(query, bot):
#         callQ = CallbackQuery(query)
#         func(callQ, bot)
#     return callback