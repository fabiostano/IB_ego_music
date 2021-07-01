
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range, Page, WaitPage
)
cu = c

doc = ''

class Constants(BaseConstants):
    name_in_url = 'C_pre_game'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):

    # ----------- UNDERSTANDING QUESTIONS ------------ #
    uq1 = models.BooleanField(
        label='In each of the four rounds of the task, you need to buy at least one product.',
        widget=widgets.RadioSelectHorizontal)
    uq2 = models.BooleanField(
        label='You can save money by buying a product in this task, compared to buying it in a regular store.',
        widget=widgets.RadioSelectHorizontal)
    uq3 = models.BooleanField(
        label='Every participant will receive the products they purchased after the experiment.',
        widget=widgets.RadioSelectHorizontal)
    uq4 = models.BooleanField(
        label='If you are the randomly chosen participant, you will get the products you purchased after the experiment. The discounted prices of your purchased products will be subtracted from the payout transferred to your bank account.',
        widget=widgets.RadioSelectHorizontal)
    uq5 = models.BooleanField(
        label='If you are not chosen to receive your products, the price of the products you purchased will be subtracted from your payout anyways.',
        widget=widgets.RadioSelectHorizontal)
    uq6 = models.BooleanField(
        label='In each round you can decide between two products.',
        widget=widgets.RadioSelectHorizontal)
    uq7 = models.BooleanField(
        label='You can buy between 0 and 4 different products in this task.',
        widget=widgets.RadioSelectHorizontal)

    def uq1_choices(self):
        import random
        choices = [[True, 'Wrong'], [False, 'Correct']]
        random.shuffle(choices)
        return choices

    def uq2_choices(self):
        import random
        choices = [[True, 'Correct'], [False, 'Wrong']]
        random.shuffle(choices)
        return choices

    def uq3_choices(self):
        import random
        choices = [[True, 'Wrong'], [False, 'Correct']]
        random.shuffle(choices)
        return choices

    def uq4_choices(self):
        import random
        choices = [[True, 'Correct'], [False, 'Wrong']]
        random.shuffle(choices)
        return choices

    def uq5_choices(self):
        import random
        choices = [[True, 'Correct'], [False, 'Wrong']]
        random.shuffle(choices)
        return choices

    def uq6_choices(self):
        import random
        choices = [[True, 'Correct'], [False, 'Wrong']]
        random.shuffle(choices)
        return choices

    def uq7_choices(self):
        import random
        choices = [[True, 'Correct'], [False, 'Wrong']]
        random.shuffle(choices)
        return choices
