from django.db import models
from django.utils.translation import gettext_lazy as _


class CardTrigger(models.TextChoices):
    START_OF_AGENDA_PHASE = 'start_of_agenda_phase', _('At the start of the agenda phase')
    AFTER_AGENDA_REVEALED = 'after_agenda_revealed', _('After an agenda is revealed')
    AFTER_SPEAKER_VOTE = 'after_speaker_vote', _('After the speaker votes on an agenda')
    START_OF_INVASION = 'start_of_invasion', _('At the start of an invasion')
    ELECTED_AS_AGENDA_OUTCOME = 'elected_as_agenda_outcome', _('When you are elected as the outcome of an agenda')
    AFTER_YOUR_SHIP_IS_DESTROYED_DURING_SPACE_COMBAT = 'after_your_ship_is_destroyed_during_space_combat', _('After 1 of your ships is destroyed during a space combat')
    ACTION = 'action', _('As an Action')
    AFTER_THEY_USE_SUSTAIN_DAMAGE = 'after_they_use_sustain_damage', _("After another player's ship uses Sustain Damage to cancel a hit produced by your units or abilities")
    START_OF_INVASION_IN_A_SYSTEM_THAT_CONTAINS_OPPOSING_PDS = 'start_of_invasion_in_a_system_that_contains_opposing_pds', _('At the start of an invasion in a system that contains 1 or more of your opponents\' PDS units')
    AFTER_YOU_VOTE = 'after_you_vote', _('After you cast votes on an outcome of an agenda')
    START_OR_END_OF_COMBAT_ROUND = 'start_or_end_of_combat_round', _('At the start or end of a combat round')
    AFTER_THEY_MOVE_SHIPS_DURING_TACTICAL_ACTION = 'after_they_move_ships_during_tactical_action', _('After another player moves ships into a system during a tactical action')
    START_OF_FIRST_ROUND_OF_SPACE_COMBAT = 'start_of_first_round_of_space_combat', _('At the start of the first round of a space combat')
    AFTER_YOUR_GROUND_FORCES_MADE_COMBAT_ROLLS_DURING_INVASION = 'after_your_ground_forces_made_combat_rolls_during_invasion', _('After your ground forces make combat rolls during a round of ground combat')
    AFTER_YOU_ACTIVATE_A_SYSTEM = 'after_you_activate_a_system', _('After you activate a system')
    AFTER_YOU_GAIN_CONTROL_OF_A_PLANET = 'after_you_gain_control_of_a_planet', _('When you gain control of a planet')
    AFTER_THEY_DECLARE_RETREAT_DURING_SPACE_COMBAT = 'after_they_declare_retreat_during_space_combat', _('After your opponent declares a retreat during a space combat')
    BEFORE_YOU_ASSIGN_HITS_DURING_SPACE_CANNON = 'before_you_assign_hits_during_space_cannon', _('Before you assign hits produced by another player\'s Space Cannon roll')
    START_OF_COMBAT_ROUND = 'start_of_combat_round', _('At the start of a combat round')
    AFTER_THEY_COMMIT_GROUND_FORCES = 'after_they_commit_ground_forces', _('After another player commits ground forces to land on a planet you control')
    WHEN_YOU_WOULD_RETURN_STRATEGY_CARDS_DURING_STATUS_PHASE = 'when_you_would_return_strategy_cards_during_status_phase', _('When you would return your strategy card(s) during the status phase')
    WHEN_THEY_CHOOSE_A_STRATEGY_CARD_DURING_STRATEGY_PHASE = 'when_they_choose_a_strategy_card_during_strategy_phase', _('When another player chooses a strategy card during the strategy phase')
    AFTER_THEY_GAIN_CONTROL_OF_YOUR_PLANET = 'after_they_gain_control_of_your_planet', _('After another player gains control of a planet you control')
    AFTER_THEY_PLAY_ACTION_CARD_EXCLUDING_SABOTAGE = 'after_they_play_action_card_excluding_sabotage', _('When another player plays an action card other than "Sabotage"')
    AFTER_YOU_WON_SPACE_COMBAT = 'after_you_won_space_combat', _('After you win a space combat')
    BEFORE_YOU_ASSIGN_HITS_TO_YOUR_SHIPS_DURING_SPACE_COMBAT = 'before_you_assign_hits_to_your_ships_during_space_combat', _('Before you assign hits to your ships during a space combat')
    START_OF_STRATEGY_PHASE = 'start_of_strategy_phase', _('At the start of the strategy phase')
    AFTER_YOU_ACTIVATE_A_SYSTEM_THAT_CONTAINS_YOUR_SHIPS = 'after_you_activate_a_system_that_contains_your_ships', _('After you activate a system that contains 1 or more of your ships')
    WHEN_AGENDA_REVEALED = 'when_agenda_revealed', _('When an agenda is revealed') # Veto special case
