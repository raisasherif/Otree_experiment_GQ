from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import csv
import random
author = 'Your name here'

doc = """
A Intro_raisa app that reads its questions from a spreadsheet
(see Intro_raisa.csv in this directory).
There is 1 question per page; the number of pages in the game
is determined by the number of questions in the CSV.
See the comment below about how to randomize the order of pages.
"""


class Constants(BaseConstants):
    name_in_url = 'quiz'
    players_per_group = None

    with open('quiz/quiz.csv') as questions_file:
        questions = list(csv.DictReader(questions_file))

    num_rounds = 5


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            randomized_questions = random.sample(Constants.questions, len(Constants.questions))
            print(Constants.questions, randomized_questions)
            #p.participant.vars['questions'] = Constants.questions
            p.participant.vars['questions'] = randomized_questions
            question_data = p.current_question()
            p.question_id = int(question_data['id'])
            p.question = question_data['question']
            p.solution = question_data['solution']
            #Have the choices here


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    question_id = models.IntegerField()
    question = models.StringField()
    solution = models.StringField()
    submitted_answer = models.StringField(widget=widgets.RadioSelect)
    is_correct = models.BooleanField()

    def current_question(self):
        return self.participant.vars['questions'][self.round_number - 1]

    def check_correct(self):
        self.is_correct = (self.submitted_answer == self.solution)
