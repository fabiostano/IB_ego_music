
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range, Page, WaitPage
)
cu = c

doc = ''

class Constants(BaseConstants):
    name_in_url = 'E_post_game'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    pmc_pna1 = models.IntegerField()
    pmc_pna2 = models.IntegerField()


    # ----- DEMOGRAPHICS ----- #
    money_available = models.StringField(
        label='How much money do you have available for free spending each month?',
        choices=["0€ - 150€", "150€ - 300€", "300€ - 450€", "450€ - 600€", "600€ - 750€", "750€ - 900€", "< 900€",
                 "Prefer Not To Say"]
    )
    occupation = models.StringField(
        label='Current Employment Status',
        choices=["Student", "Employed", "Self-Employed", "Other", "Prefer Not To Say"]
    )
    age = models.IntegerField(label='Age')
    gender = models.StringField(
        label='Gender',
        choices=["Male", "Female", "Diverse"]
    )

    # ----- DEBRIEFING QUESTIONS ----- #
    debriefing1 = models.IntegerField(
        label='I enjoyed shopping in the second task.',
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Neither Agree or Disagree'], [4, 'Agree'],
                 [5, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )
    debriefing2 = models.IntegerField(
        label='I would describe the background music tempo as fast.',
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Neither Agree or Disagree'], [4, 'Agree'],
                 [5, 'Strongly Agree'], [0, "I didn't hear any music"]],
        widget=widgets.RadioSelectHorizontal
    )
    debriefing3 = models.IntegerField(
        label='I would describe the background music tempo as slow.',
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Neither Agree or Disagree'], [4, 'Agree'],
                 [5, 'Strongly Agree'], [0, "I didn't hear any music"]],
        widget=widgets.RadioSelectHorizontal
    )
    debriefing7 = models.IntegerField(
        label='I am happy with the purchase(s) I made.',
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Neither Agree or Disagree'], [4, 'Agree'],
                 [5, 'Strongly Agree'], [0, "I didn't buy anything"]],
        widget=widgets.RadioSelectHorizontal
    )
    debriefing8 = models.IntegerField(
        label='I regret the purchase(s) I made.',
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Neither Agree or Disagree'], [4, 'Agree'],
                 [5, 'Strongly Agree'], [0, "I didn't buy anything"]],
        widget=widgets.RadioSelectHorizontal
    )

    debriefing13 = models.IntegerField(
        label='This is an attention check. Please choose "Agree".',
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Neither Agree or Disagree'], [4, 'Agree'],
                 [5, 'Strongly Agree']],
        widget = widgets.RadioSelectHorizontal
    )

    debriefing9 = models.IntegerField(
        label='I turned the music off at some point during the experiment.',
        choices=[[1, 'Yes'], [2, 'No'], [0, "I didn't hear any music"]],
        widget=widgets.RadioSelectHorizontal
    )

    debriefing10 = models.IntegerField(
        label='I  listened to the music at a comfortable volume.',
        choices=[[1, 'Never'], [2, 'Sometimes'], [3, 'Always'], [0, "I didn't hear any music"]],
        widget=widgets.RadioSelectHorizontal
    )

    debriefing11 = models.IntegerField(
        label='I enjoyed the music.',
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Neither Agree or Disagree'], [4, 'Agree'],
                 [5, 'Strongly Agree'], [0, "I didn't hear any music"]],
        widget=widgets.RadioSelectHorizontal
    )

    debriefing12 = models.IntegerField(
        label='I had technical problems during the experiment.',
        choices=[[1, 'Yes'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    debriefing14 = models.StringField(
        label='If you experienced technical problems, please try to describe them in a few words.',
        blank=True
    )

    first_name = models.StringField(
        label='First Name'
    )
    last_name = models.StringField(
        label='Last Name'
    )
    IBAN = models.StringField(
        label='IBAN',
        blank = True
    )
