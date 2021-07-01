
from .models import *
import csv

class Post_ManipCheck(Page):
    form_model = 'player'
    form_fields = ['pmc_pna1', 'pmc_pna2']

class Debriefing(Page):
    form_model = 'player'
    form_fields = ['debriefing1', 'debriefing2', 'debriefing3',
                   'debriefing7', 'debriefing8', 'debriefing9', 'debriefing10', 'debriefing11', 'debriefing12',
                   'debriefing13', 'debriefing14']

    def before_next_page(self):
        if self.player.debriefing13 == 4:
            self.participant.vars["ac_items"] += 1

class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'occupation', 'money_available']

class PayOut(Page):
    form_model = 'player'
    form_fields = ['first_name', 'last_name', 'IBAN']

    def vars_for_template(self):
        return {
            'payout' : self.participant.payoff_plus_participation_fee(),
        }

    def before_next_page(self):
        productName_r1 = ["NONE", "Mars", "Snickers"]
        productName_r2 = ["NONE", "Airwaves Cool Cassis", "Airwaves Menthol & Eucalyptus"]
        productName_r3 = ["NONE", "Corny Nuss Karamell", "Corny Erdnuss Volmilch"]
        productName_r4 = ["NONE", "Romerquell Blaubeere", "Romerquell Marille"]

        print(self.participant.vars["purchases"])
        print(self.participant.vars["ac_decisions"])
        print(self.participant.vars["dc_result"])
        print(self.participant.vars["ac_items"])

        purchases = self.participant.vars["purchases"]
        ac_decisions = self.participant.vars["ac_decisions"]
        ac_items = self.participant.vars["ac_items"]
        dc_result = self.participant.vars["dc_result"]

        productR1 = productName_r1[purchases[0]]
        productR2 = productName_r2[purchases[1]]
        productR3 = productName_r3[purchases[2]]
        productR4 = productName_r4[purchases[3]]

        with open('payouts.csv', mode='a+') as results_file:
            payout = self.participant.payoff_plus_participation_fee()
            IBAN = self.player.IBAN
            first_name = self.player.first_name
            last_name = self.player.last_name
            results_writer = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            results_writer.writerow([payout, productR1, productR2, productR3, productR4, first_name, last_name, IBAN, ac_decisions, ac_items, dc_result])
            print("Results stored!")

        self.player.IBAN = "-" # hier werden die Daten aus der oTree DB durch "-" ersetzt
        self.player.first_name = "-" # hier werden die Daten aus der oTree DB durch "-" ersetzt
        self.player.last_name = "-" # hier werden die Daten aus der oTree DB durch "-" ersetzt


class ThankYou(Page):
    form_model = 'player'

page_sequence = [Post_ManipCheck, Debriefing, Demographics, PayOut, ThankYou]
