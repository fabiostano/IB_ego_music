
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range, Page, WaitPage
)
cu = c

doc = ''
class Constants(BaseConstants):
    name_in_url = 'A_intro'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    def creating_session(self):
        import random

        for p in self.get_players():
            p.participant.vars['treatment_mt'] = random.choice(['mt_fast', 'mt_slow', 'mt_none'])
            p.treatment_mt = p.participant.vars['treatment_mt']


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    treatment_mt = models.StringField()
