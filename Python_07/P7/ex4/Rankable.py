"""
Rankable.py - Abstract interface for ranking capabilities
"""
from abc import ABC, abstractmethod
from typing import Dict


class Rankable(ABC):
    """
    Abstract interface for entities that can be ranked.
    Provides methods for calculating ratings and tracking wins/losses.
    """

    @abstractmethod
    def calculate_rating(self) -> int:
        """
        Calculate the current rating of this entity.

        Returns:
            The calculated rating as an integer
        """
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """
        Update the number of wins.

        Args:
            wins: Number of wins to add
        """
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """
        Update the number of losses.

        Args:
            losses: Number of losses to add
        """
        pass

    @abstractmethod
    def get_rank_info(self) -> Dict:
        """
        Get ranking information.

        Returns:
            A dictionary containing ranking details
        """
        pass