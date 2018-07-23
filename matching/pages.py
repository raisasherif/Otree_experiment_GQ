from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class my_match(Page):
    form_model = 'player'
    form_fields = ['guess_1','guess_2','guess_3','guess_4','guess_5']

class Results(Page):
    pass

page_sequence = [
    my_match,
    Results
]
