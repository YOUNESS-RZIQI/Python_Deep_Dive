from abc import ABC, abstractmethod
from typing import Dict, List


class GameStrategy(ABC):
    """
    Abstract interface for game strategies.
    Defines how cards should be played and targets should be prioritized.
    """

    @abstractmethod
    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        """
        Execute a turn based on this strategy.

        Args:
            hand: List of cards in hand
            battlefield: List of cards on the battlefield

        Returns:
            A dictionary containing the turn execution result
        """
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """
        Get the name of this strategy.

        Returns:
            The strategy name
        """
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: List) -> List:
        """
        Prioritize targets based on this strategy.

        Args:
            available_targets: List of available targets

        Returns:
            A list of targets in priority order
        """
        pass
