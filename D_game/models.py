
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range, Page, WaitPage
)
cu = c

doc = ''

class Constants(BaseConstants):
    name_in_url = 'D_game'
    players_per_group = None
    num_rounds = 4

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    did_buy = models.IntegerField()

    treatment_mt = models.StringField()

    # ----- BETWEEN ROUNDS QUESTIONS ----- #
    pr_offer = models.IntegerField(
        label='I bought the product because of the good offers (high discounts).',
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Neither Agree or Disagree'], [4, 'Agree'],
                 [5, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )
    pr_notoffer = models.IntegerField(
        label='I would have made the same decision if the products were not discounted',
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Neither Agree or Disagree'], [4, 'Agree'],
                 [5, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )
    pr_urge = models.IntegerField(
        label='I bought something because I just felt like it.',
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Neither Agree or Disagree'], [4, 'Agree'],
                 [5, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )
    pr_spontaneous = models.IntegerField(
        label='The decision to buy was spontaneous.',
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Neither Agree or Disagree'], [4, 'Agree'],
                 [5, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )
    pr_thoughts = models.IntegerField(
        label='I deliberated a lot about whether I need the product or not before making the decision.',
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Neither Agree or Disagree'], [4, 'Agree'],
                 [5, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )
    pr_planned = models.IntegerField(
        label='I planned to buy this exact product anyways.',
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Neither Agree or Disagree'], [4, 'Agree'],
                 [5, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )
    pr_planned2 = models.IntegerField(
        label='I planned to buy products of the same category anyways.',
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Neither Agree or Disagree'], [4, 'Agree'],
                 [5, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )
    pr_reward = models.IntegerField(
        label='I bought the product to reward myself after the experiment.',
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Neither Agree or Disagree'], [4, 'Agree'],
                 [5, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )
    npr_wrongtype = models.IntegerField(
        label='I usually never buy the products offered in this round.',
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Neither Agree or Disagree'], [4, 'Agree'],
                 [5, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )
    npr_wrongtype2 = models.IntegerField(
        label='I do not like the products offered in this round.',
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Neither Agree or Disagree'], [4, 'Agree'],
                 [5, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )
    npr_time = models.IntegerField(
        label='I did not have enough time to buy something.',
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Neither Agree or Disagree'], [4, 'Agree'],
                 [5, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )
    np_changedecision = models.IntegerField(
        label='I would have bought something if I had more time to decide.',
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Neither Agree or Disagree'], [4, 'Agree'],
                 [5, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )
