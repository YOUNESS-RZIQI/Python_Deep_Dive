"""
ArtifactCard.py - Concrete implementation of an artifact card
"""
from typing import Dict
from ex0.Card import Card, Rarity


class ArtifactCard(Card):
    """
    Concrete implementation of an artifact card.
    Artifacts are permanent game modifiers that remain in play.
    """

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: Rarity,
        durability: int,
        effect: str
    ) -> None:
        """
        Initialize an artifact card with durability and effect.

        Args:
            name: The name of the artifact
            cost: The mana cost to play this artifact
            rarity: The rarity tier of the card (Rarity enum)
            durability: How many turns the artifact lasts
            effect: Description of the artifact's permanent ability

        Raises:
            ValueError: If durability is not a positive integer
        """
        super().__init__(name, cost, rarity)

        if not isinstance(durability, int) or durability <= 0:
            raise ValueError("Durability must be a positive integer")

        self.durability = durability
        self.effect = effect

    def play(self, game_state: Dict) -> Dict:
        """
        Play this artifact card by deploying it to the battlefield.

        Args:
            game_state: Current state of the game

        Returns:
            A Dictionary containing the result of playing the artifact
        """
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': f"Permanent: {self.effect}"
        }

    def activate_ability(self) -> Dict:
        """
        Activate the artifact's ongoing ability.

        Returns:
            A Dictionary containing the activation result
        """
        return {
            'artifact': self.name,
            'ability': self.effect,
            'durability_remaining': self.durability,
            'active': self.durability > 0
        }

    def get_card_info(self) -> Dict:
        """
        Get comprehensive information about this artifact card.

        Returns:
            A Dictionary containing all card information
        """
        info = super().get_card_info()
        info['durability'] = self.durability
        info['effect'] = self.effect
        return info
