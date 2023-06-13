import json

class studentDB:
    def __init__(self):
        self.__data = None

    def connect(self, dataFile):
        with open(dataFile) as jsonFile:
            self.__data = json.load(jsonFile)

    def getData(self, name):
        for student in self.__data['students']:
            if student['name'] == name:
                return student
            
    def close(self):
        print('closed')