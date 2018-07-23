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
            if self.round_number == 1:
                randomized_questions = random.sample(Constants.questions, len(Constants.questions))
                p.participant.vars['questions'] = randomized_questions

            question_data = p.current_question()
            p.question_id = int(question_data['id'])
            p.question = question_data['question']
            p.solution = question_data['solution']
            p.choice_1 = question_data['choice1']
            p.choice_2 = question_data['choice2']
            p.choice_3 = question_data['choice3']
            p.choice_4 = question_data['choice4']


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    question_id = models.IntegerField()
    question = models.StringField()
    choice_1 = models.StringField()
    choice_2 = models.StringField()
    choice_3 = models.StringField()
    choice_4 = models.StringField()
    solution = models.StringField()
    current_score = models.IntegerField(min=0, max=5, initial=0)
    submitted_answer = models.StringField(widget=widgets.RadioSelect)
    is_correct = models.BooleanField()

    def current_question(self):
        return self.participant.vars['questions'][self.round_number - 1]

    def check_correct(self):
        self.is_correct = (self.submitted_answer == self.solution)

    def calc_current_score(self):
        player_in_all_rounds = self.in_all_rounds()
        self.current_score = sum([p.is_correct for p in player_in_all_rounds])