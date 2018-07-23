from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class Question(Page):
    form_model = 'player'
    form_fields = ['submitted_answer']

    def submitted_answer_choices(self):

        return [
            self.player.choice_1,
            self.player.choice_2,
            self.player.choice_3,
            self.player.choice_4
        ]

    # def vars_for_template(self):
    #     return {'question': self.player.question}

    def before_next_page(self):
        self.player.check_correct()

class Welcome(Page):
    pass

class Consent(Page):
    pass

class Description(Page):
    pass

class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        player_in_all_rounds = self.player.in_all_rounds()
        return {
            'player_in_all_rounds': player_in_all_rounds,
            'questions_correct': sum([p.is_correct for p in player_in_all_rounds])
        }

page_sequence = [
    Question,
    Results
]
