from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class my_match(Page):
    # form_model = 'player'
    # form_fields = ['guess_1','guess_2','guess_3','guess_4','guess_5']
    def vars_for_template(self):
        return {
            'students': self.participant.vars['selected_students'],
        }

class Results(Page):
    pass

page_sequence = [
    my_match,
    Results
]
