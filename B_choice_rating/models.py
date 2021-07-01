
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range, Page, WaitPage
)
cu = c

doc = ''
class Constants(BaseConstants):
    name_in_url = 'B_choice_rating'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    def creating_session(self):
        import itertools

        choice_rating = itertools.cycle(['choice', 'rating'])
        for p in self.get_players():
            p.treatment_cr = next(choice_rating)

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    treatment_cr = models.StringField()
    treatment_mt = models.StringField()

    # ----- PRE TASK SURVEY ----- #

    pts1 = models.IntegerField(
        label='Shopping is a relaxing activity for me.',
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Neither Agree or Disagree'], [4, 'Agree'],
                 [5, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )
    pts2 = models.IntegerField(
        label='I enjoy going shopping.',
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Neither Agree or Disagree'], [4, 'Agree'],
                 [5, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )
    pts3 = models.IntegerField(
        label='I look forward to my shopping trips.',
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Neither Agree or Disagree'], [4, 'Agree'],
                 [5, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )
    pts4 = models.IntegerField(
        label='I often buy things spontaneously',
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Neither Agree or Disagree'], [4, 'Agree'],
                 [5, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )
    pts5 = models.IntegerField(
        label='"Just do it" describes the way i buy things.',
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Neither Agree or Disagree'], [4, 'Agree'],
                 [5, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )
    pts6 = models.IntegerField(
        label='I often buy things without thinking.',
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Neither Agree or Disagree'], [4, 'Agree'],
                 [5, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )
    pts7 = models.IntegerField(
        label='"I see it, I buy it" describes me.',
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Neither Agree or Disagree'], [4, 'Agree'],
                 [5, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )
    pts8 = models.IntegerField(
        label='"Buy now, think about it later" describes me.',
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Neither Agree or Disagree'], [4, 'Agree'],
                 [5, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )
    pts9 = models.IntegerField(
        label='Sometimes I feel like buying things on the spur-of-the-moment.',
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Neither Agree or Disagree'], [4, 'Agree'],
                 [5, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )
    pts10 = models.IntegerField(
        label='I buy things according to how I feel at the moment.',
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Neither Agree or Disagree'], [4, 'Agree'],
                 [5, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )
    pts11 = models.IntegerField(
        label='I carefully plan most of my purchases.',
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Neither Agree or Disagree'], [4, 'Agree'],
                 [5, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )
    pts12 = models.IntegerField(
        label='Sometimes I am a bit reckless about what I buy.',
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Neither Agree or Disagree'], [4, 'Agree'],
                 [5, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )
    pts13 = models.IntegerField(
        label='This is an attention check. Please choose "Disagree".',
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Neither Agree or Disagree'], [4, 'Agree'],
                 [5, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )

    # ----- CHOICES TASK ----- #
    choices = models.StringField()

    # ----- CHOICES TASK ----- #
    ratings = models.StringField()

    # ----- MANIPULATION CHECK EGO DEPLETION ----- #

    egodep1 = models.IntegerField()

    egodep2 = models.IntegerField(
        label='By the end of the choices task, how fatigued did you feel?',
        choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'],
                 [5, '5'], [6, '6'], [7, '7']],
        widget=widgets.RadioSelectHorizontal
    )
    egodep3 = models.IntegerField(
        label='By the end of the choices task, how frustrated did you feel?',
        choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'],
                 [5, '5'], [6, '6'], [7, '7']],
        widget=widgets.RadioSelectHorizontal
    )
    egodep4 = models.IntegerField(
        label='How effortful was the choices task?',
        choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'],
                 [5, '5'], [6, '6'], [7, '7']],
        widget=widgets.RadioSelectHorizontal
    )
    egodep5 = models.IntegerField(
        label='How difficult was the choices task?',
        choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'],
                 [5, '5'], [6, '6'], [7, '7']],
        widget=widgets.RadioSelectHorizontal
    )

    # ----- MANIPULATION CHECK CHOICES ----- #
    mc_choices1 = models.IntegerField(
        label='How many decisions did you feel you made in the previous task?',
        choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'],
                 [5, '5'], [6, '6'], [7, '7']],
        widget=widgets.RadioSelectHorizontal
    )
    mc_choices2 = models.IntegerField(
        label='How much careful consideration did you put into the decisions you made in the previous task?',
        choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'],
                 [5, '5'], [6, '6'], [7, '7']],
        widget=widgets.RadioSelectHorizontal
    )
    mc_choices3 = models.IntegerField(
        label='How much did you deliberate before making each decision in the previous task?',
        choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'],
                 [5, '5'], [6, '6'], [7, '7']],
        widget=widgets.RadioSelectHorizontal
    )
    mc_choices4 = models.IntegerField(
        label='How much did you think about your options prior to making each decision?',
        choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'],
                 [5, '5'], [6, '6'], [7, '7']],
        widget=widgets.RadioSelectHorizontal
    )
    mc_choices5 = models.IntegerField(
        label='How active did you feel in making your decisions in the previous task?',
        choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'],
                 [5, '5'], [6, '6'], [7, '7']],
        widget=widgets.RadioSelectHorizontal
    )
    mc_choices6 = models.IntegerField(
        label='How tired do you feel right now?',
        choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'],
                 [5, '5'], [6, '6'], [7, '7']],
        widget=widgets.RadioSelectHorizontal
    )

    # ----- MANIPULATION CHECK PLEASURE & AROUSAL ----- #
    mc_pna1 = models.IntegerField()

    mc_pna2 = models.IntegerField()

    # ----- DELIBERATION CHECK ----- #

    dc1 = models.IntegerField()
    dc2 = models.IntegerField()
    dc3 = models.IntegerField()