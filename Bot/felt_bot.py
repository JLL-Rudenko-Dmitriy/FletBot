from telebot.async_telebot import AsyncTeleBot
from telebot.asyncio_filters import StateFilter
from telebot.asyncio_storage import StateMemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from asyncio import sleep as async_sleep

from Bot.Handlers.base_handler import Handler
from Bot.Handlers.derived_handlers import *


from telebot.asyncio_handler_backends import State, StatesGroup

class FletBot:
    """
    This is a class which provides usefull interfaces and othe abilities!
    """
    def __init__(self, TOKEN):
        self.BOT_TOKEN = TOKEN
        self.scheduleManager = None
        self.AsyncBot = AsyncTeleBot(self.BOT_TOKEN, state_storage=StateMemoryStorage())
        self.ai_model = None

    def addSheduller(self):
        self.scheduleManager = AsyncIOScheduler()
        return self
    
    def addJob(self, job, type = 'cron', **kwargs):
        self.scheduleManager.add_job(job, type, args=[self.AsyncBot], **kwargs)
        return self
    
    def addAiModel(self, ai_model):
        self.ai_model = ai_model

    def registerHandler(self,handler: Handler):        
        if(isinstance(handler, MessageHandler)):
            self.AsyncBot.register_message_handler(**handler.register())
            return None
        
        if(isinstance(handler, CallbackHandler)):
            self.AsyncBot.register_callback_query_handler(**handler.register())
            return None
            
    def registerHandlers(self,handlers_list: Optional[List[Handler]]):
        for handler in handlers_list:
            if (type(handler) is list):
                self.registerHandlers(handler)
            else:
                self.registerHandler(handler)

    def set_state_filter(self):
        self.AsyncBot.add_custom_filter(StateFilter(self.AsyncBot))

    async def __bot_launch(self):
        await self.AsyncBot.polling(non_stop=True)

        
    async def launch(self):
        if (self.scheduleManager != None):
            self.scheduleManager.start()
        
        await self.__bot_launch()
        while True:
            await async_sleep(1)