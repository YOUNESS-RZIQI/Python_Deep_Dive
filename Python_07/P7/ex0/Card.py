"""
Card.py - Abstract Base Class for all DataDeck cards
"""
from abc import ABC, abstractmethod
from typing import Dict
from enum import Enum


class Rarity(Enum):
    """Enumeration for card rarity levels."""
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"


class Card(ABC):
    """
    Abstract base class representing a universal card blueprint.
    All cards in DataDeck must inherit from this class and implement
    the required abstract methods.
    """

    def __init__(self, name: str, cost: int, rarity: Rarity) -> None:
        """
        Initialize a card with basic attributes.

        Args:
            name: The name of the card
            cost: The mana cost to play this card
            rarity: The rarity tier of the card (Rarity enum)
        """
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: Dict) -> Dict:
        """
        Abstract method that defines how a card is played.
        Must be implemented by all concrete card classes.

        Args:
            game_state: Current state of the game

        Returns:
            A Dictionary containing the result of playing the card
        """
        pass

    def get_card_info(self) -> Dict:
        """
        Get comprehensive information about this card.

        Returns:
            A Dictionary containing all card information
        """
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity.value,
            "type": self.__class__.__name__.replace("Card", "")
        }

    def is_playable(self, available_mana: int) -> bool:
        """
        Check if this card can be played with the available mana.

        Args:
            available_mana: The amount of mana currently available

        Returns:
            True if the card can be played, False otherwise
        """
        return available_mana >= self.cost
