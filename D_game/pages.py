
from .models import *

class SalesPage(Page):
    form_model = 'player'

    form_fields = ['did_buy']

    def vars_for_template(self):
        payout = self.participant.payoff_plus_participation_fee()
        round_nr = self.round_number

        mt = self.participant.vars['treatment_mt']

        return {
            "payout": payout,
            "round_number": round_nr,
            "mt": mt,
        }

    def before_next_page(self):
        self.player.treatment_mt = self.participant.vars['treatment_mt']

        if self.player.round_number == 4:
            purchaselist = [self.player.in_round(1).did_buy, self.player.in_round(2).did_buy,
               self.player.in_round(3).did_buy, self.player.in_round(4).did_buy]
            self.participant.vars["purchases"] = purchaselist

class IBQuestions_Purchase(Page):
    form_model = 'player'
    form_fields = ['pr_offer', 'pr_notoffer', 'pr_urge', 'pr_thoughts', 'pr_planned', 'pr_planned2', 'pr_reward',
                   'pr_spontaneous']

    def is_displayed(self):
        if self.player.did_buy > 0:
            return True
        else:
            return False

    def vars_for_template(self):
        return {
            "mt": self.participant.vars['treatment_mt']
        }

class IBQuestions_NoPurchase(Page):
    form_model = 'player'
    form_fields = ['npr_wrongtype', 'npr_wrongtype2', 'npr_time', 'np_changedecision']

    def is_displayed(self):
        if self.player.did_buy == 0:
            return True
        else:
            return False

    def vars_for_template(self):
        return {
            "mt": self.participant.vars['treatment_mt']
        }


page_sequence = [SalesPage, IBQuestions_Purchase, IBQuestions_NoPurchase]
