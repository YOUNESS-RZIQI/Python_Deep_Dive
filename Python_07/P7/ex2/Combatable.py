from abc import ABC, abstractmethod
from typing import Dict


class Combatable(ABC):
    """
    Abstract interface for cards with combat capabilities.
    Cards implementing this interface can attack, defend, and track
    combat stats.
    """

    def attack(self, target) -> Dict:
        """
        Attack a target with this card.

        Args:
            target: The target to attack

        Returns:
            A dictionary containing the attack result
        """
        pass

    attack = abstractmethod(attack)

    def defend(self, incoming_damage: int) -> Dict:
        """
        Defend against incoming damage.

        Args:
            incoming_damage: Amount of damage being dealt

        Returns:
            A dictionary containing the defense result
        """
        pass

    defend = abstractmethod(defend)

    def get_combat_stats(self) -> Dict:
        """
        Get the combat statistics of this card.

        Returns:
            A dictionary containing combat-related statistics
        """
        pass

    get_combat_stats = abstractmethod(get_combat_stats)
