from .activate_card_command import ActivateCardCommand
from .activate_system_command import ActivateSystemCommand
from .select_strategy_command import SelectStrategyCommand

COMMANDS = {
    'select_strategy': SelectStrategyCommand,
    'activate_system': ActivateSystemCommand,
    'activate_card': ActivateCardCommand,
}
