
from .models import *

class Pre_Task_Survey(Page):
    form_model = 'player'
    form_fields = ["pts1", "pts2", "pts3", "pts4", "pts5", "pts6", "pts7", "pts8", "pts9", "pts10", "pts11", "pts12", "pts13"]

    def before_next_page(self):
        if self.player.pts13 == 2:
            self.participant.vars["ac_items"] += 1
        if self.player.treatment_cr == "rating":
            self.participant.vars["dc_result"] = "noDC"
        elif self.player.treatment_cr == "choice":
            self.participant.vars["dc_result"] = 0

class ChoiceTask_Instructions(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.treatment_cr == "choice"

class ChoiceTask(Page):
    form_model = 'player'
    form_fields = ["choices"]

    def vars_for_template(self):
        return {
            "mt": self.participant.vars['treatment_mt']
        }

    def is_displayed(self):
        return self.player.treatment_cr == "choice"

    def before_next_page(self):
        if "PASSED" in self.player.choices:
            self.participant.vars["ac_decisions"] = "PASSED"
        elif "FAILED" in self.player.choices:
            self.participant.vars["ac_decisions"] = "FAILED"

class RatingTask_Instructions(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.treatment_cr == "rating"

class RatingTask(Page):
    form_model = 'player'
    form_fields = ["ratings"]

    def vars_for_template(self):
        return {
            "mt": self.participant.vars['treatment_mt']
        }

    def is_displayed(self):
        return self.player.treatment_cr == "rating"

    def before_next_page(self):
        if "PASSED" in self.player.ratings:
            self.participant.vars["ac_decisions"] = "PASSED"
        elif "FAILED" in self.player.ratings:
            self.participant.vars["ac_decisions"] = "FAILED"

class ManipCheck_EgoDep(Page):
    form_model = 'player'
    form_fields = ["egodep1", "egodep2", "egodep3", "egodep4", "egodep5"]

    def vars_for_template(self):
        return {
            "mt": self.participant.vars['treatment_mt']
        }

class ManipCheck_Choices(Page):
    form_model = 'player'
    form_fields = ["mc_choices1", "mc_choices2", "mc_choices3", "mc_choices4", "mc_choices5", "mc_choices6"]

    def vars_for_template(self):
        return {
            "mt": self.participant.vars['treatment_mt']
        }

class ManipCheck_PleasureArousal(Page):
    form_model = 'player'
    form_fields = ["mc_pna1", "mc_pna2"]

    def vars_for_template(self):
        return {
            "mt": self.participant.vars['treatment_mt']
        }

class DeliberationCheck0(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.treatment_cr == "choice"

    def vars_for_template(self):
        return {
            "mt": self.participant.vars['treatment_mt']
        }

class DeliberationCheck1(Page):
    form_model = 'player'
    form_fields = ["dc1"]

    def vars_for_template(self):
        return {
            "choices" : self.player.choices,
            "mt": self.participant.vars['treatment_mt']
        }

    def is_displayed(self):
        return self.player.treatment_cr == "choice"


class DeliberationCheck2(Page):
    form_model = 'player'
    form_fields = ["dc2"]

    def vars_for_template(self):
        return {
            "choices" : self.player.choices,
            "mt": self.participant.vars['treatment_mt']
        }

    def is_displayed(self):
        return self.player.treatment_cr == "choice"

class DeliberationCheck3(Page):
    form_model = 'player'
    form_fields = ["dc3"]

    def vars_for_template(self):
        return {
            "choices" : self.player.choices,
            "mt": self.participant.vars['treatment_mt']
        }

    def is_displayed(self):
        return self.player.treatment_cr == "choice"

    def before_next_page(self):
        score = self.player.dc1 + self.player.dc2 + self.player.dc3
        if score < 2:
            self.player.payoff -= 1
        if score == 3:
            self.player.payoff += 1

        self.participant.vars["dc_result"] = score

page_sequence = [Pre_Task_Survey, ChoiceTask_Instructions, ChoiceTask, RatingTask_Instructions, RatingTask,
                 DeliberationCheck0, DeliberationCheck1, DeliberationCheck2, DeliberationCheck3, ManipCheck_EgoDep,
                 ManipCheck_Choices, ManipCheck_PleasureArousal]