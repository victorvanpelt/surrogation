from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):
    pass
    form_model = 'player'
    form_fields = ['accept_instructions']

class Choice(Page):
    form_model = 'player'
    form_fields = ['accept_character', 'gender', 'intelligence', 'strength', 'charisma', 'agility', 'stamina']

class Results(Page):
    pass


page_sequence = [
    Introduction,
    Choice,
    Results
]
