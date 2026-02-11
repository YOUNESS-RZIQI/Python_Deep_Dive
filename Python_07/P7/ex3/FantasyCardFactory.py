from typing import Dict, Optional, Union
import random
from ex0.Card import Card, Rarity
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard, EffectType
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


# • Creates fantasy-themed creatures (Dragons, Goblins, etc.)
# • Creates elemental spells (Fire, Ice, Lightning)
# • Creates magical artifacts (Rings, Staffs, Crystals)
# • Supports extensible card type registration


class FantasyCardFactory(CardFactory):
    """
    Factory for creating fantasy-themed cards.
    Creates dragons, goblins, elemental spells, and magical artifacts.
    """

    def __init__(self) -> None:
        """Initialize the fantasy card factory with card templates."""
        self.cards = []

    def create_creature(
        self,
        name_or_power: Optional[Union[str, int]] = None
    ) -> Card:
        """
        Create a fantasy creature card.

        Args:
            name_or_power: Either a creature type name or power level

        Returns:
            A creature card
        """
        creature = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY, 7, 6)
        if isinstance(name_or_power, str):
            creature.name = name_or_power
        elif isinstance(name_or_power, int):
            creature.attack = name_or_power

        self.cards += [creature]

    def create_spell(
        self,
        name_or_power: Optional[Union[str, int]] = None
    ) -> Card:
        """
        Create a fantasy spell card.

        Args:
            name_or_power: Either a spell name or power level

        Returns:
            A spell card
        """
        spell = SpellCard("Fire Dragon", 5, Rarity.LEGENDARY, 7, 6)
        if isinstance(name_or_power, str):
            spell.name = name_or_power
        elif isinstance(name_or_power, int):
            spell.attack = name_or_power

        # return SpellCard(
        #     name,
        #     template['cost'],
        #     template['rarity'],
        #     template['effect_type']
        # )

    def create_artifact(
        self,
        name_or_power: Optional[Union[str, int]] = None
    ) -> Card:
        """
        Create a fantasy artifact card.

        Args:
            name_or_power: Either an artifact name or power level

        Returns:
            An artifact card
        """
        if isinstance(name_or_power, str):
            # Create by name
            template_key = name_or_power.lower()
            if template_key in self.artifact_templates:
                template = self.artifact_templates[template_key]
                name = name_or_power.replace('_', ' ').title()
            else:
                # Default to mana ring
                template = self.artifact_templates['mana_ring']
                name = 'Mana Ring'
        elif isinstance(name_or_power, int):
            # Create by power level
            if name_or_power >= 3:
                template = self.artifact_templates['staff']
                name = 'Staff'
            else:
                template = self.artifact_templates['mana_ring']
                name = 'Mana Ring'
        else:
            # Random artifact
            template_key = random.choice(list(self.artifact_templates.keys()))
            template = self.artifact_templates[template_key]
            name = template_key.replace('_', ' ').title()

        return ArtifactCard(
            name,
            template['cost'],
            template['rarity'],
            template['durability'],
            template['effect']
        )

    def create_themed_deck(self, size: int) -> Dict:
        """
        Create a fantasy-themed deck.

        Args:
            size: Number of cards in the deck

        Returns:
            A dictionary containing deck information
        """
        deck_cards = []

        # Create a balanced deck
        creatures_count = size // 2
        spells_count = size // 3
        artifacts_count = size - creatures_count - spells_count

        for _ in range(creatures_count):
            deck_cards.append(self.create_creature())

        for _ in range(spells_count):
            deck_cards.append(self.create_spell())

        for _ in range(artifacts_count):
            deck_cards.append(self.create_artifact())

        return {
            'theme': 'Fantasy',
            'cards': deck_cards,
            'size': len(deck_cards),
            'composition': {
                'creatures': creatures_count,
                'spells': spells_count,
                'artifacts': artifacts_count
            }
        }

    def get_supported_types(self) -> Dict:
        """
        Get the types of cards this factory can create.

        Returns:
            A dictionary of supported card types
        """
        return {
            'creatures': list(self.creature_templates.keys()),
            'spells': list(self.spell_templates.keys()),
            'artifacts': list(self.artifact_templates.keys())
        }