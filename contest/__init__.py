from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'contest'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 2
    ENDOWMENT = Currency(10)
    COST_PER_TICKET = Currency(0.50)
    PRIZE = Currency(8)


class Subsession(BaseSubsession):
    is_paid = models.BooleanField()

    def setup_round(self):
        self.is_paid = True
        for group in self.get_groups():
            group.setup_round()
class Group(BaseGroup):
    prize = models.CurrencyField()

    def setup_round(self):
        self.prize = C.PRIZE



class Player(BasePlayer):
    endowment = models.CurrencyField()
    cost_per_ticket = models.CurrencyField()
    tickets_purchased = models.IntegerField()
    def setup_round(self):
        self.endowment = C.ENDOWMENT
        self.cost_per_ticket = C.COST_PER_TICKET
# PAGES

class SetupRound(WaitPage):
    wait_for_all_groups = True
    @staticmethod
    def after_all_players_arrive(subsession):
        subsession.setup_round()


class Intro(Page):
    pass


class Decisions(Page):
    pass

class DecisionWaitPage(WaitPage):
    pass

class Results(Page):
    pass


class EndBlock(Page):
    pass


page_sequence = [
    SetupRound,
    Intro,
    Decisions,
    DecisionWaitPage,
    Results,
    EndBlock,
]
