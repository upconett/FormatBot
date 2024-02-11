from random import choice

from ege.database import getSection
from ege.constants import ahuiVariations, cheerUpVariations, dontGiveUpVariations


def formatAnswer(taskNumber: int, taskAnswer: str, taskComment: str = None):
	taskSection = getSection()
	result = f'<b>Дз {taskSection} №{taskNumber}</b>\n'
	result += f'<b>Ответ:</b> {taskAnswer}\n'
	if taskComment:
		result += f'\n{taskComment}'
	return result


def formatSectionList(currentSection: str, sections: list):
	result = '🧊 <b>Существующие разделы:</b>\n'
	result += f' • <b>{currentSection}</b>\n'
	for section in sections:
		if section != currentSection:
			result += f' • {section}\n'
	return result


def showAhui():
	return choice(ahuiVariations)


def cheerUp():
	return choice(cheerUpVariations)


def dontGiveUp():
	return choice(dontGiveUpVariations)