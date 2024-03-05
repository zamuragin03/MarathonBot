from aiogram.dispatcher.filters.state import State, StatesGroup

class FSMAdmin(StatesGroup):
    choosing_action = State()