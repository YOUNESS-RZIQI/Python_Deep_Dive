"""
Magical.py - Abstract interface for magical abilities
"""
from abc import ABC, abstractmethod
from typing import Dict, List


class Magical(ABC):
    """
    Abstract interface for cards with magical capabilities.
    Cards implementing this interface can cast spells, channel mana,
    and track magic stats.
    """

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: List) -> Dict:
        """
        Cast a spell on the given targets.

        Args:
            spell_name: Name of the spell to cast
            targets: List of targets for the spell

        Returns:
            A dictionary containing the spell cast result
        """
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> Dict:
        """
        Channel mana to increase magical power.

        Args:
            amount: Amount of mana to channel

        Returns:
            A dictionary containing the channeling result
        """
        pass

    @abstractmethod
    def get_magic_stats(self) -> Dict:
        """
        Get the magical statistics of this card.

        Returns:
            A dictionary containing magic-related statistics
        """
        pass
