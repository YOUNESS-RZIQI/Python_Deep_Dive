"""
SpellCard.py - Concrete implementation of a spell card
"""
from typing import Dict, List
from ex0.Card import Card, Rarity
from enum import Enum


class EffectType(Enum):
    """Enumeration for spell effect types."""
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class SpellCard(Card):
    """
    Concrete implementation of a spell card.
    Spells are instant magical effects that are consumed when played.
    """

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: Rarity,
        effect_type: EffectType
    ) -> None:
        """
        Initialize a spell card with an effect type.

        Args:
            name: The name of the spell
            cost: The mana cost to cast this spell
            rarity: The rarity tier of the card (Rarity enum)
            effect_type: The type of effect (EffectType enum)
        """
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: Dict) -> Dict:
        """
        Play this spell card by casting it.

        Args:
            game_state: Current state of the game

        Returns:
            A Dictionary containing the result of casting the spell
        """
        effect_descriptions = {
            EffectType.DAMAGE.value: f"Deal {self.cost} damage to target",
            EffectType.HEAL.value: f"Heal {self.cost * 2} health",
            EffectType.BUFF.value: f"Grant +{self.cost}/+{self.cost} buff",
            EffectType.DEBUFF.value: f"Apply -{self.cost}/-{self.cost} debuff"
        }

        return {
            'card_played': game_state['name'],
            'mana_used': game_state['cost'],
            'effect': effect_descriptions.get(
                game_state['effect_type'],
                "Unknown effect"
            )
        }

    def resolve_effect(self, targets: List) -> Dict:
        """
        Resolve the spell's effect on the given targets.

        Args:
            targets: List of targets affected by the spell

        Returns:
            A Dictionary containing the resolution result
        """
        return {
            'spell': self.name,
            'effect_type': self.effect_type.value,
            'targets': [str(target) for target in targets],
            'resolved': True,
            'consumed': True  # Spells are one-time use
        }

    def get_card_info(self) -> Dict:
        """
        Get comprehensive information about this spell card.

        Returns:
            A Dictionary containing all card information
        """
        info = super().get_card_info()
        info['effect_type'] = self.effect_type.value
        return info
