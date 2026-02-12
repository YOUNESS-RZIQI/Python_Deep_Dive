from typing import Dict, List
from ex3.GameStrategy import GameStrategy
from ex0.CreatureCard import CreatureCard


# • Prioritizes attacking and dealing damage
# • Plays low-cost creatures first for board presence
# • Targets enemy creatures and player directly
# • Returns comprehensive turn execution results


class AggressiveStrategy(GameStrategy):
    """
    Aggressive strategy that prioritizes dealing damage.
    Plays low-cost cards first and attacks aggressively.
    """

    def __init__(self):
        self.mana = 0

    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        """
        Execute an aggressive turn.
        Plays low-cost cards first and attacks all targets.

        Args:
            hand: List of cards in hand
            battlefield: List of cards on the battlefield

        Returns:
            A dictionary containing the turn execution result
        """

        hand_from_lowest: List = sorted(hand, key=lambda card: card.cost)
        del hand_from_lowest[-1]

        cards_played = []
        mana_used = 0
        damage_dealt = 0
        for card in hand_from_lowest:
            if self.mana >= card.cost:
                self.mana -= card.cost
                mana_used += card.cost
                battlefield += [card.name]
                cards_played += [card.name]
                if hasattr("attack", card):
                    damage_dealt += card.attack

        targets_attacked = "Enemy Player"
        return {
            'cards_played': cards_played,
            'mana_used': mana_used,
            'targets_attacked': targets_attacked,
            'damage_dealt': damage_dealt
        }

    def get_strategy_name(self) -> str:
        """
        Get the name of this strategy.

        Returns:
            The strategy name
        """
        return "AggressiveStrategy"

    def prioritize_targets(self,
                           available_targets: List[CreatureCard]) -> List:
        """
        Prioritize targets aggressively.

        Args:
            available_targets: List of available targets

        Returns:
            A list of targets in priority order
        """

        prioritized: List = sorted(available_targets,
                                   key=lambda card: card.health)

        return prioritized
