from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Victor and Farah'

doc = """
The Surrogation Game
"""


class Constants(BaseConstants):
    name_in_url = 'surrogation'
    players_per_group = 1
    num_rounds = 1


class Subsession(BaseSubsession):

    def creating_session(self):
        # randomize to treatments
        for player in self.get_players():
            player.surrogation = random.choice(['yes', 'no'])
            print('set player.surrogation to', player.surrogation)

            if player.surrogation == 'yes':
                player.measure_skill = random.choice(['abilities', 'Attack', 'Socialize', 'Speed', 'Health'])
                print('set player.measure_skill to', player.measure_skill)

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    surrogation = models.StringField()
    measure_skill = models.StringField()
