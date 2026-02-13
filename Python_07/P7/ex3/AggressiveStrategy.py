from typing import Dict, List
from ex3.GameStrategy import GameStrategy
from ex0.CreatureCard import CreatureCard


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

        cards_played = []
        mana_used = 0
        damage_dealt = 0
        game_state = {"mana": self.mana, "battlefield": battlefield}
        for card in hand_from_lowest:
            if game_state["mana"] >= card.cost:
                cards_played += [card.name]
                card.play(game_state)
                mana_used += card.cost
                if "CreatureCard" in card.__class__.__name__:
                    damage_dealt += card.attack

        self.mana = game_state["mana"]
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
