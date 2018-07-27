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
            p.age_1 = p.participant.vars['selected_students'][0]['age']
            p.age_2 = p.participant.vars['selected_students'][1]['age']
            p.age_3 = p.participant.vars['selected_students'][2]['age']
            p.age_4 = p.participant.vars['selected_students'][3]['age']
            p.age_5 = p.participant.vars['selected_students'][4]['age']
            p.branch_1 = p.participant.vars['selected_students'][0]['branch']
            p.branch_2 = p.participant.vars['selected_students'][1]['branch']
            p.branch_3 = p.participant.vars['selected_students'][2]['branch']
            p.branch_4 = p.participant.vars['selected_students'][3]['branch']
            p.branch_5 = p.participant.vars['selected_students'][4]['branch']
            p.institute_1 = p.participant.vars['selected_students'][0]['institute']
            p.institute_2 = p.participant.vars['selected_students'][1]['institute']
            p.institute_3 = p.participant.vars['selected_students'][2]['institute']
            p.institute_4 = p.participant.vars['selected_students'][3]['institute']
            p.institute_5 = p.participant.vars['selected_students'][4]['institute']
            p.gender_1 = p.participant.vars['selected_students'][0]['gender']
            p.gender_2 = p.participant.vars['selected_students'][1]['gender']
            p.gender_3 = p.participant.vars['selected_students'][2]['gender']
            p.gender_4 = p.participant.vars['selected_students'][3]['gender']
            p.gender_5 = p.participant.vars['selected_students'][4]['gender']

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age_1 = models.IntegerField()
    age_2 = models.IntegerField()
    age_3 = models.IntegerField()
    age_4 = models.IntegerField()
    age_5 = models.IntegerField()
    branch_1 = models.StringField()
    branch_2 = models.StringField()
    branch_3 = models.StringField()
    branch_4 = models.StringField()
    branch_5 = models.StringField()
    institute_1 = models.StringField()
    institute_2 = models.StringField()
    institute_3 = models.StringField()
    institute_4 = models.StringField()
    institute_5 = models.StringField()
    gender_1 = models.StringField()
    gender_2 = models.StringField()
    gender_3 = models.StringField()
    gender_4 = models.StringField()
    gender_5 = models.StringField()
    language_1 = models.StringField()
    language_2 = models.StringField()
    language_3 = models.StringField()
    language_4 = models.StringField()
    language_5 = models.StringField()
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
    deviation_1 = models.IntegerField(min=0, max=20)
    deviation_2 = models.IntegerField(min=0, max=20)
    deviation_3 = models.IntegerField(min=0, max=20)
    deviation_4 = models.IntegerField(min=0, max=20)
    deviation_5 = models.IntegerField(min=0, max=20)
    total_deviation = models.IntegerField(initial=0, min=0)


    def select_students(self):
        return [self.participant.vars['all_students'][i] for i in range(0,5)]

    def calculate_deviation(self):
        self.deviation_1 = abs(self.prediction_1 - self.actual_1)
        self.deviation_2 = abs(self.prediction_2 - self.actual_2)
        self.deviation_3 = abs(self.prediction_3 - self.actual_3)
        self.deviation_4 = abs(self.prediction_4 - self.actual_4)
        self.deviation_5 = abs(self.prediction_5 - self.actual_5)
        self.total_deviation = sum([
            self.deviation_1,
            self.deviation_2,
            self.deviation_3,
            self.deviation_4,
            self.deviation_5])
