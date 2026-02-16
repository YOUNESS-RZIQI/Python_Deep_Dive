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

    def calculate_rating(self) -> int:
        """
        Calculate the current rating of this entity.

        Returns:
            The calculated rating as an integer
        """
        pass

    calculate_rating = abstractmethod(calculate_rating)

    def update_wins(self, wins: int) -> None:
        """
        Update the number of wins.

        Args:
            wins: Number of wins to add
        """
        pass

    update_wins = abstractmethod(update_wins)

    def update_losses(self, losses: int) -> None:
        """
        Update the number of losses.

        Args:
            losses: Number of losses to add
        """
        pass

    update_losses = abstractmethod(update_losses)

    def get_rank_info(self) -> Dict:
        """
        Get ranking information.

        Returns:
            A dictionary containing ranking details
        """
        pass

    get_rank_info = abstractmethod(get_rank_info)
