from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):
    form_model = 'player'
    form_fields = ['surrogation', 'measure_skill']

class Introduction(Page):
    pass

class MyPage(Page):
    pass

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Introduction,
    MyPage,
    ResultsWaitPage,
    Results
]
