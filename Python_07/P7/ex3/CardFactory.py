from abc import ABC, abstractmethod
from typing import Dict, Optional, Union
from ex0.Card import Card


class CardFactory(ABC):
    """
    Abstract factory interface for creating themed cards.
    Defines methods for creating different card types and themed decks.
    """

    def create_creature(
        self,
        name_or_power: Optional[Union[str, int]] = None
    ) -> Card:
        """
        Create a creature card.

        Args:
            name_or_power: Either a specific name or power level

        Returns:
            A creature card
        """
        pass

    create_creature = abstractmethod(create_creature)

    def create_spell(
        self,
        name_or_power: Optional[Union[str, int]] = None
    ) -> Card:
        """
        Create a spell card.

        Args:
            name_or_power: Either a specific name or power level

        Returns:
            A spell card
        """
        pass

    create_spell = abstractmethod(create_spell)

    def create_artifact(
        self,
        name_or_power: Optional[Union[str, int]] = None
    ) -> Card:
        """
        Create an artifact card.

        Args:
            name_or_power: Either a specific name or power level

        Returns:
            An artifact card
        """
        pass

    create_artifact = abstractmethod(create_artifact)

    def create_themed_deck(self, size: int) -> Dict:
        """
        Create a themed deck with the specified number of cards.

        Args:
            size: Number of cards in the deck

        Returns:
            A dictionary containing deck information
        """
        pass

    create_themed_deck = abstractmethod(create_themed_deck)

    def get_supported_types(self) -> Dict:
        """
        Get the types of cards this factory can create.

        Returns:
            A dictionary of supported card types
        """
        pass

    get_supported_types = abstractmethod(get_supported_types)
