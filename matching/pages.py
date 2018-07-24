from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class my_match(Page):
    form_model = 'player'
    form_fields = ['prediction_1','prediction_2','prediction_3','prediction_4','prediction_5']

    def vars_for_template(self):
        return {
            'students': self.participant.vars['selected_students'],
        }

    def before_next_page(self):
        self.player.calculate_deviation()

class Results(Page):
    pass

page_sequence = [
    my_match,
    Results
]
