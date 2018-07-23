from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import csv
import random
author = 'Raisa'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'matching'
    players_per_group = None
    num_rounds = 1

    with open('matching/student_data.csv') as student_data:
        students = list(csv.DictReader(student_data))

class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            print('new player')
            randomized_students = random.sample(Constants.students, len(Constants.students))
            p.participant.vars['all_students'] = randomized_students
            p.participant.vars['selected_students'] = p.select_students()
            print('sdsdsdsdsds')
            print(p.participant.vars)
            # p.age = int(student_data['id'])
            # print(p.age)



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField()
    branch = models.StringField()
    institute = models.StringField()
    state = models.StringField()
    language = models.StringField()
    #submitted_answer = models.StringField(widget=widgets.RadioSelect)
    #is_correct = models.BooleanField()

    def select_students(self):
        print( [self.participant.vars['all_students'][i] for i in range(0,5)])
        return [self.participant.vars['all_students'][i] for i in range(0,5)]