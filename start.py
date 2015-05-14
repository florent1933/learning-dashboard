import jsonpickle
import requests
import sys
from datetime import *
import random

from utils import *

jsonpickle.set_encoder_options('simplejson', sort_keys=True, indent=4)

historic = []
lessons_name = ['Maths', 'English', 'Computer Science']

class Activity:
    def __init__(self, actor, verb, object, date):
        self.actor = actor
        self.timestamp = date
        self.verb = verb
        self.object = object
        historic.append(self)


    def __str__(self):
        return "Activity: " + str(self.actor)+" " + str(self.verb)+ " " + str(self.object)



class Student:
    def __init__(self, id):
        self.email = str(id) + "@gmail.com"
        self.name = str(id)
        self.logged_in = False
        self.lessons = []


    def __str__(self):
        return "Student: " + str(self.name)


    def start_day(self, date):
        if not self.logged_in:
            self.logged_in = True
            Activity(self, "Logged in", "website", date)

    def stop_day(self, date):
        if self.logged_in:
            self.logged_in = False
            Activity(self, "Logged out", "website", date)

    def register_lesson(self, date):
        l = random.choice(lessons_name)

        if l not in self.lessons:
            self.lessons.append(l)
            Activity(self, "Registered in", l , date)

    def go_lesson(self, date):
        if not self.lessons or random.random() < 0.05:
            self.register_lesson(date)

        if random.random() < 0.8:
            l = random.choice(self.lessons)
            date = random_time(date, 0, 3)
            Activity(self, "started", l , date)

            date = random_time(date, 0, 30)
            Activity(self, "stopped", l , date)

        return date



    # overide Serializer of json pickle
    def __getstate__(self):
        state = self.__dict__.copy()
        del state['logged_in']
        del state['lessons']
        return state


    def __setstate__(self, state):
        self.__dict__.update(state)



def create_fixtures():
    '''
    Create fixtures into Json
    This is the scenario
    '''

    today_start = datetime(2015, 1, 1)

    # represent number of students
    for i in range (10):
        student = Student(i)

        # represent number of days
        for x in range(28):
            today = random_time(today_start + timedelta(days=x))
            today = random_time(today)

            # One day
            s=0
            while (s < 0.1):
                s = random.random()
                if random.random() < 0.6:
                    today = random_time(today, 3, 0)
                    student.start_day(today)

                    r=0
                    while (r < 0.3):
                        r = random.random()
                        if random.random() < 0.9:
                            today = random_time(today, 0, 20)
                            today = student.go_lesson(today)

                    today = random_time(today, 0, 5)
                    student.stop_day(today)


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

