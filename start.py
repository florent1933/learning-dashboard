import jsonpickle
import requests
import sys
from datetime import *

from random import *

jsonpickle.set_encoder_options('simplejson', sort_keys=True, indent=4)


class Activity:
    def __init__(self, actor, verb, object, date):
        self.actor = actor
        self.timestamp = date
        self.verb = verb
        self.object = object

    def __str__(self):
        return "Activity: " + str(self.actor)+" " + str(self.verb)+ " " + str(self.object)



class Student:
    def __init__(self, id):
        self.email = str(id) + "@gmail.com"
        self.name = str(id)
        self.logged_in = False


    def __str__(self):
        return "Student: " + str(self.name)


    def start_day(self, date):
        if not self.logged_in:
            self.logged_in = True
            return Activity(self, "Logged in", "website", date)


    # overide Serializer of json pickle
    def __getstate__(self):
        state = self.__dict__.copy()
        del state['logged_in']
        return state


    def __setstate__(self, state):
        self.__dict__.update(state)



def create_fixtures():
    '''
    Create fixtures into Json
    '''

    historic = []

    today = datetime(2015, 1, 1)

    # represent days
    for i in range (20):
        today = today + timedelta(days=1)
        # represent number of students
        for x in range(1000):
            student = Student(x)

            # chances to be connected on the day
            if random() < 0.6:
                activity = student.start_day(today)
                historic.append(activity)

    print(jsonpickle.encode(historic, unpicklable=False))



def config_es():
    '''
    Create index placis in ES
    '''

    print('Create index placis in ES')
    r = requests.put("http://localhost:9200/placis?pretty")
    print('Response')
    print(r.text)


if __name__ == '__main__':
    '''
    If argv, we config ES
    '''

    if(len(sys.argv) > 1):
        config_es()
    
    create_fixtures()

