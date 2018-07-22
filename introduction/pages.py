from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Welcome(Page):
    pass

class Consent(Page):
    pass

class Description(Page):
    pass


page_sequence = [
    Welcome,
    Consent,
    Description
]
