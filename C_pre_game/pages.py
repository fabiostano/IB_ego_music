
from .models import *

class GameInstructions(Page):
    form_model = 'player'

class GameInstructionsImg(Page):
    form_model = 'player'

class ComprehensionCheck1(Page):
    form_model = 'player'
    form_fields = ['uq1']

    def vars_for_template(self):
        return {
            "mt": self.participant.vars['treatment_mt']
        }

class ComprehensionCheck2(Page):
    form_model = 'player'
    form_fields = ['uq2']

    def vars_for_template(self):
        return {
            "mt": self.participant.vars['treatment_mt']
        }

class ComprehensionCheck3(Page):
    form_model = 'player'
    form_fields = ['uq3']

    def vars_for_template(self):
        return {
            "mt": self.participant.vars['treatment_mt']
        }

class ComprehensionCheck4(Page):
    form_model = 'player'
    form_fields = ['uq4']

    def vars_for_template(self):
        return {
            "mt": self.participant.vars['treatment_mt']
        }

class ComprehensionCheck5(Page):
    form_model = 'player'
    form_fields = ['uq5']

    def vars_for_template(self):
        return {
            "mt": self.participant.vars['treatment_mt']
        }

class ComprehensionCheck6(Page):
    form_model = 'player'
    form_fields = ['uq6']

    def vars_for_template(self):
        return {
            "mt": self.participant.vars['treatment_mt']
        }

class ComprehensionCheck7(Page):
    form_model = 'player'
    form_fields = ['uq7']

    def vars_for_template(self):
        return {
            "mt": self.participant.vars['treatment_mt']
        }

class ComprehensionCheck1_results(Page):
    form_model = 'player'
    def vars_for_template(self):
        return {
            "uq1" : self.player.uq1,
            "mt": self.participant.vars['treatment_mt']
        }

class ComprehensionCheck2_results(Page):
    form_model = 'player'
    def vars_for_template(self):
        return {
            "uq2" : self.player.uq2,
            "mt": self.participant.vars['treatment_mt']
        }

class ComprehensionCheck3_results(Page):
    form_model = 'player'
    def vars_for_template(self):
        return {
            "uq3" : self.player.uq3,
            "mt": self.participant.vars['treatment_mt']
        }

class ComprehensionCheck4_results(Page):
    form_model = 'player'
    def vars_for_template(self):
        return {
            "uq4" : self.player.uq4,
            "mt": self.participant.vars['treatment_mt']
        }

class ComprehensionCheck5_results(Page):
    form_model = 'player'
    def vars_for_template(self):
        return {
            "uq5" : self.player.uq5,
            "mt": self.participant.vars['treatment_mt']
        }

class ComprehensionCheck6_results(Page):
    form_model = 'player'
    def vars_for_template(self):
        return {
            "uq6" : self.player.uq6,
            "mt": self.participant.vars['treatment_mt']
        }

class ComprehensionCheck7_results(Page):
    form_model = 'player'
    def vars_for_template(self):
        return {
            "uq7" : self.player.uq7,
            "mt": self.participant.vars['treatment_mt']
        }

page_sequence = [GameInstructions, GameInstructionsImg, ComprehensionCheck1, ComprehensionCheck1_results, ComprehensionCheck2, ComprehensionCheck2_results, ComprehensionCheck3, ComprehensionCheck3_results, ComprehensionCheck4, ComprehensionCheck4_results, ComprehensionCheck5, ComprehensionCheck5_results, ComprehensionCheck6, ComprehensionCheck6_results, ComprehensionCheck7, ComprehensionCheck7_results]
