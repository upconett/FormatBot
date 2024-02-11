import json


def writeData(data):
	with open('files/ege.json', 'w') as file:
		json.dump(data, file, indent=4, ensure_ascii=False)


def getData():
	try:
		with open('files/ege.json', 'r') as file:
			return json.load(file)
	except:
		writeData({'currentSection': ''})


def getSection():
	data = getData()
	return data['currentSection']


def listSections():
	data = getData()
	return list(data.keys())[1:]


def addSection(name: str):
	data = getData()
	data[name] = {}
	writeData(data)


def changeCurrentSection(name: str):
	data = getData()
	data['currentSection'] = name
	writeData(data)


def defineNumberOfTasks(number: int):
	data = getData()
	section = getSection()
	for i in range(1, number+1):
		try:
			data[section][str(i)] == True
		except:
			data[section][str(i)] = ''
	writeData(data)


def addFormattedTask(number: int, text: str, document: str = None):
	data = getData()
	section = getSection()
	data[section][str(number)] = {'txt': text, 'document': document}
	writeData(data)


def getAllTasks():
	data = getData()
	section = getSection()
	result = []
	for key in data[section]:
		if data[section][key] != '':
			result.append(data[section][key])
	return result


def listTasks():
	data = getData()
	section = getSection()
	tasks = len(data[section])
	done = 0
	for key in data[section]:
		if data[section][key] != '':
			done += 1
	return done, tasks