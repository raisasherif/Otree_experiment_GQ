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
    num_rounds = 5

    with open('matching/student_data.csv') as student_data:
        students = list(csv.DictReader(student_data))

class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            randomized_students = random.sample(Constants.students, len(Constants.students))
            #p.participant.vars['questions'] = Constants.questions
            p.participant.vars['students'] = randomized_students
            student_data = p.current_student()
            p.age = int(student_data['id'])
            p.question = question_data['question']
            p.solution = question_data['solution']
            #Have the choices here



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

    def current_student(self):
        return self.participant.vars['students'][self.round_number - 1]