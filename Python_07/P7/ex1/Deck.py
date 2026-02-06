"""
Deck.py - Deck management system for DataDeck
"""
from typing import Dict, Optional
import random
from ex0.Card import Card


class Deck:
    """
    Deck management class that can handle any card type.
    Demonstrates polymorphism by treating all cards through the Card interface.
    """

    def __init__(self) -> None:
        """Initialize an empty deck."""
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        """
        Add a card to the deck.

        Args:
            card: Any card that inherits from the Card base class
        """
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """
        Remove a card from the deck by name.

        Args:
            card_name: The name of the card to remove

        Returns:
            True if card was found and removed, False otherwise
        """
        for i, card in enumerate(self.cards):
            if card.name == card_name:
                self.cards.pop(i)
                return True
        return False

    def shuffle(self) -> None:
        """
        Shuffle the deck randomly.
        """
        random.shuffle(self.cards)

    def draw_card(self) -> Optional[Card]:
        """
        Draw a card from the top of the deck.

        Returns:
            The drawn card, or None if the deck is empty
        """
        if self.cards:
            return self.cards.pop(0)
        return None

    def get_deck_stats(self) -> Dict:
        """
        Get statistics about the deck composition.

        Returns:
            A Dictionary containing deck statistics
        """
        if not self.cards:
            return {
                'total_cards': 0,
                'creatures': 0,
                'spells': 0,
                'artifacts': 0,
                'avg_cost': 0.0
            }

        # Count card types by examining the class name
        card_types = {
            'creatures': 0,
            'spells': 0,
            'artifacts': 0
        }

        total_cost = 0

        for card in self.cards:
            card_type = card.__class__.__name__.replace('Card', '').lower()
            # Map card type names to stats keys
            if 'creature' in card_type:
                card_types['creatures'] += 1
            elif 'spell' in card_type:
                card_types['spells'] += 1
            elif 'artifact' in card_type:
                card_types['artifacts'] += 1
            total_cost += card.cost

        avg_cost = total_cost / len(self.cards) if self.cards else 0.0

        return {
            'total_cards': len(self.cards),
            'creatures': card_types['creatures'],
            'spells': card_types['spells'],
            'artifacts': card_types['artifacts'],
            'avg_cost': round(avg_cost, 1)
        }