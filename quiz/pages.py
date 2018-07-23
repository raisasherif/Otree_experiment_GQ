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


    def before_next_page(self):
        self.player.check_correct()
        self.player.calc_current_score()


class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        player_in_all_rounds = self.player.in_all_rounds()
        return {
            'player_in_all_rounds': player_in_all_rounds,
            'questions_correct': sum([p.is_correct for p in player_in_all_rounds])
        }

    def before_next_page(self):
        print(self.player.current_score)
        self.participant.vars['test_1_score'] = self.player.current_score

page_sequence = [
    Question,
    Results
]
