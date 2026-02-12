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
        from_lowest = sorted(hand, key=lambda card: card.cost)
        

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