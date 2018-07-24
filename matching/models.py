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
            randomized_students = random.sample(Constants.students, len(Constants.students))
            p.participant.vars['all_students'] = randomized_students
            p.participant.vars['selected_students'] = p.select_students()
            p.actual_1 = p.participant.vars['selected_students'][0]['score']
            p.actual_2 = p.participant.vars['selected_students'][1]['score']
            p.actual_3 = p.participant.vars['selected_students'][2]['score']
            p.actual_4 = p.participant.vars['selected_students'][3]['score']
            p.actual_5 = p.participant.vars['selected_students'][4]['score']

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField()
    branch = models.StringField()
    institute = models.StringField()
    state = models.StringField()
    language = models.StringField()
    prediction_1 = models.IntegerField(min=0, max=20, label="")
    prediction_2 = models.IntegerField(min=0, max=20, label="")
    prediction_3 = models.IntegerField(min=0, max=20, label="")
    prediction_4 = models.IntegerField(min=0, max=20, label="")
    prediction_5 = models.IntegerField(min=0, max=20, label="")
    actual_1 = models.IntegerField(min=0, max=20)
    actual_2 = models.IntegerField(min=0, max=20)
    actual_3 = models.IntegerField(min=0, max=20)
    actual_4 = models.IntegerField(min=0, max=20)
    actual_5 = models.IntegerField(min=0, max=20)
    total_deviation = models.IntegerField(initial=0, min=0)
    
    #submitted_answer = models.StringField(widget=widgets.RadioSelect)
    #is_correct = models.BooleanField()

    def select_students(self):
        return [self.participant.vars['all_students'][i] for i in range(0,5)]

    def calculate_deviation(self):
        comparison_list = [
            (self.prediction_1, self.actual_1),
            (self.prediction_2, self.actual_2),
            (self.prediction_3, self.actual_3),
            (self.prediction_4, self.actual_4),
            (self.prediction_5, self.actual_5)
        ]

        for pair in comparison_list:
            self.total_deviation += abs(pair[0] - pair[1])
