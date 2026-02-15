from abc import ABC, abstractmethod
from typing import Dict, List


class Magical(ABC):
    """
    Abstract interface for cards with magical capabilities.
    Cards implementing this interface can cast spells, channel mana,
    and track magic stats.
    """

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

    cast_spell = abstractmethod(cast_spell)

    def channel_mana(self, amount: int) -> Dict:
        """
        Channel mana to increase magical power.

        Args:
            amount: Amount of mana to channel

        Returns:
            A dictionary containing the channeling result
        """
        pass

    channel_mana = abstractmethod(channel_mana)

    def get_magic_stats(self) -> Dict:
        """
        Get the magical statistics of this card.

        Returns:
            A dictionary containing magic-related statistics
        """
        pass

    get_magic_stats = abstractmethod(get_magic_stats)
