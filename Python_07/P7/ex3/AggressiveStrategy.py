from typing import Dict, List
from ex3.GameStrategy import GameStrategy


# • Prioritizes attacking and dealing damage
# • Plays low-cost creatures first for board presence
# • Targets enemy creatures and player directly
# • Returns comprehensive turn execution results


class AggressiveStrategy(GameStrategy):
    """
    Aggressive strategy that prioritizes dealing damage.
    Plays low-cost cards first and attacks aggressively.
    """

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
        from_lowest = []
        for elment in hand
        # cards_played = []
        # mana_used = 0
        # targets_attacked = []
        # damage_dealt = 0

        # # Sort hand by cost (low to high) for aggressive play
        # sorted_hand = sorted(hand, key=lambda c: c.cost)

        # # Available mana for this turn (simplified)
        # available_mana = 10

        # # Play as many low-cost cards as possible
        # for card in sorted_hand:
        #     if mana_used + card.cost <= available_mana:
        #         cards_played.append(card.name)
        #         mana_used += card.cost

        #         # Aggressive strategy: calculate damage
        #         if hasattr(card, 'attack'):
        #             damage_dealt += card.attack
        #         elif hasattr(card, 'effect_type'):
        #             # Spell damage based on cost
        #             damage_dealt += card.cost

        # # Aggressive strategy attacks player directly
        # if damage_dealt > 0:
        #     targets_attacked.append("Enemy Player")

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

    def prioritize_targets(self, available_targets: List) -> List:
        """
        Prioritize targets aggressively.
        Prioritizes enemy player, then weakest creatures.

        Args:
            available_targets: List of available targets

        Returns:
            A list of targets in priority order
        """
        # Aggressive strategy: prioritize direct damage to player
        prioritized = []

        # Player is highest priority
        player_targets = [t for t in available_targets if 'player' in str(t).lower()]
        prioritized.extend(player_targets)

        # Then low-health creatures (if they have health attribute)
        creature_targets = [t for t in available_targets if t not in player_targets]
        creature_targets.sort(key=lambda t: getattr(t, 'health', 999))
        prioritized.extend(creature_targets)

        return prioritized