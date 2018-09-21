from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range,
)
import random


author = 'Victor_Farah'

doc = """
The Surrogation Game
"""


class Constants(BaseConstants):
    name_in_url = 'surrogation'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):

    def creating_session(self):
        # randomize to treatments
        # Now always set to surrotation treatment
        for player in self.get_players():
            #player.surrogation = random.choice(['yes', 'no'])
            player.surrogation = 'yes'
            print('set player.surrogation to', player.surrogation)

            # Ranomly set measure if surrogation treatment
            if player.surrogation == 'yes':
                player.measure_skill = random.choice(['Intelligence', 'Strength', 'Charisma', 'Agility', 'Stamina'])
                print('set player.measure_skill to', player.measure_skill)

        # randomize avatar condition
        # Now always set to avatar treatment
        for player in self.get_players():
            #player.avatar = random.choice(['yes', 'no'])
            player.avatar = 'yes'
            print('set player.avatar to', player.avatar)

class Group(BaseGroup):
    pass


class Player(BasePlayer):

    accept_instructions = models.BooleanField(blank=False, widget=widgets.CheckboxInput)
    accept_character = models.BooleanField(blank=False, widget=widgets.CheckboxInput)
    surrogation = models.StringField()
    measure_skill = models.StringField()
    avatar = models.StringField()

    #Traits
    #intelligence = models.FloatField(
        #widget=widgets.SliderInput(attrs={'step': '1', 'style': 'width:500px'}, show_value=True),
        #min=0,
        #initial=None,
        #max=100,
    #)
    intelligence = models.IntegerField(blank=True)
    strength = models.IntegerField(blank=True)
    charisma = models.IntegerField(blank=True)
    agility= models.IntegerField(blank=True)
    stamina = models.IntegerField(blank=True)
    gender = models.IntegerField(
        blank=False,
        choices=[
            [1, 'Male'],
            [2, 'Female']
        ]
    )