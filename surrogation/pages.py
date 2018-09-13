from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):
    form_model = 'player'
    form_fields = ['surrogation', 'measure_skill']

class Introduction(Page):
    pass

class Choice(Page):
    pass

class Results(Page):
    pass


page_sequence = [
    Introduction,
    Choice,
    Results
]
