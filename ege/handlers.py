from aiogram import Router
from aiogram import F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from ege.filters import IndentFilter, IsOwner
from ege.keyboards import default
from ege.utils import formatAnswer, formatSectionList, showAhui, cheerUp, dontGiveUp
from ege.fsm import SectionFSM
import ege.database as db

router = Router()
router.message.filter(IsOwner())


@router.message(Command('start'))
async def commandsStart(message: Message):
	await message.answer('Решаем ЕГЭ жоско 👽', reply_markup=default())


@router.message(IndentFilter())
async def handleNewTask(message: Message):
	if not message.document:
		lines = message.text.split('\n')
		document = None
	else:
		document = message.document.file_id
		lines = message.caption.split('\n')
	taskNumber = int(lines[0])
	taskAnswer = lines[1]
	taskComment = '\n'.join(lines[2:])
	formated = formatAnswer(taskNumber, taskAnswer, taskComment)
	db.addFormattedTask(taskNumber, formated, document)
	done, tasks= db.listTasks()
	await message.answer(cheerUp())
	await message.answer(f'Задание записано ✅ ({done}/{tasks})')


@router.message(F.text == '🍧 Поменять раздел')
async def changeTaskSectionStart(message: Message, state: FSMContext):
	await message.answer('Какой там раздел?')
	await state.set_state(SectionFSM.name)


@router.message(StateFilter(SectionFSM.name))
async def changeTaskSectionName(message: Message, state: FSMContext):
	if len(message.text.split('\n')) != 1:
		await message.answer('В одну строку!')
		return
	sections = db.listSections()
	if message.text in sections:
		db.changeCurrentSection(message.text)
		await message.answer('Выбран существующий раздел ✅')
		await state.clear()
		return
	else:
		db.addSection(message.text)
		db.changeCurrentSection(message.text)
		await message.answer('Создан новый раздел ✅\nСколько будет заданий?')
	await state.set_state(SectionFSM.number)


@router.message(StateFilter(SectionFSM.number))
async def changeTaskSectionNumber(message: Message, state: FSMContext):
	try:
		number = int(message.text)
	except:
		await message.answer('Я жду число.')
		return
	if number > 25:
		await message.answer(showAhui())
	db.defineNumberOfTasks(number)
	await message.answer(f'Кол-во заданий установлено {number} ✅')
	await state.clear()


@router.message(F.text == 'Разделы 🍨')
async def showExistingSections(message: Message):
	sections = db.listSections()
	currentSection = db.getSection()
	formated = formatSectionList(currentSection, sections)
	await message.answer(formated)
	

@router.message(F.text == '🫐 Выполнено')
async def listDoneTasks(message: Message):
	done, tasks = db.listTasks()
	await message.answer(dontGiveUp())
	await message.answer(f'Выполнено <b>{done}</b> из <b>{tasks}</b> заданий!')


@router.message(F.text == 'Вывести 🔮')
async def getDoneTasks(message: Message):
	doneTasks = db.getAllTasks()
	done, tasks = db.listTasks()
	for task in doneTasks:
		if task['document']:
			await message.answer_document(document = task['document'], caption = task['txt'])
		else:
			await message.answer(task['txt'])
	if done < tasks:
		await message.answer(f'Выполнены ещё не все задания! <b>({done}/{tasks})</b>')

	
