from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


class SectionFSM(StatesGroup):
	name = State()
	number = State()