
from .models import *

class Intro(Page):
    form_model = 'player'

    def vars_for_template(self):
        return {
            "mt": self.participant.vars['treatment_mt']
        }

    def before_next_page(self):
        self.participant.vars["ac_items"] = 0
        self.participant.vars["ac_decisions"] = ""

page_sequence = [Intro]