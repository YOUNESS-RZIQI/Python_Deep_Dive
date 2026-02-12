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
        self.cards = {"creatures": [], "spells": [], "artifacts": []}

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
        creatures_list = [
            "Dragon",
            "Ice Phoenix",
            "Shadow Wolf",
            "Thunder Giant",
            "Crystal Golem",
            "Forest Elf",
            "Sea Serpent",
            "Stone Troll",
            "Golden",
            "Dark Vampire",
        ]

        creature = CreatureCard(
            name=random.choice(creatures_list),
            cost=random.randint(1, 9),
            rarity=random.choice(list(Rarity)),
            attack=random.randint(1, 9),
            health=random.randint(1, 9),
        )

        if isinstance(name_or_power, str):
            creature.name = name_or_power
        elif isinstance(name_or_power, int):
            creature.attack = name_or_power

        self.cards["creatures"].append(creature.name.lower())
        return creature

    def create_spell(
        self,
        name_or_power: Optional[Union[str, int]] = None
    ) -> Card:
        """
        Create a fantasy spell card.

        Args:
            name_or_power: Either a spell name (str) or spell cost (int)

        Returns:
            A spell card
        """
        spell_names = [
            "Fireball",
            "Ice Lance",
            "Thunder Strike",
            "Healing Wave",
            "Stone Shield",
            "Shadow Curse",
            "Wind Gust",
            "Lightning",
            "Poison Cloud",
            "Arcane Blast"
        ]

        spell = SpellCard(
            name=random.choice(spell_names),
            cost=random.randint(1, 9),
            rarity=random.choice(list(Rarity)),
            effect_type=random.choice(list(EffectType))
        )

        if isinstance(name_or_power, str):
            spell.name = name_or_power
        elif isinstance(name_or_power, int):
            spell.cost = name_or_power

        self.cards["spells"].append(spell.name.lower())
        return spell

    def create_artifact(
        self,
        name_or_power: Optional[Union[str, int]] = None
    ) -> Card:
        """
        Create a fantasy artifact card.

        Args:
            name_or_power: Either an artifact name (str) or durability (int)

        Returns:
            An artifact card
        """
        artifact_names = [
            "Amulet of Strength",
            "Ring of Invisibility",
            "Crystal Orb",
            "Sword of Eternity",
            "Shield of Ages",
            "Cloak of Shadows",
            "Gauntlet of Power",
            "Helmet of Wisdom",
            "Boots of Swiftness",
            "Staff of Flames",
            "Mana_ring"
        ]

        artifact_effects = [
            "Increase attack of all creatures by 1",
            "Gain extra mana each turn",
            "Draw an extra card each turn",
            "Reduce damage taken by 2",
            "Double your attack once per turn",
            "Heal 1 health per turn",
            "Negate enemy spell once",
            "Extra defense to all creatures",
            "Discard enemy card randomly",
            "Increase spell damage by 2"
        ]

        artifact = ArtifactCard(
            name=random.choice(artifact_names),
            cost=random.randint(1, 9),
            rarity=random.choice(list(Rarity)),
            durability=random.randint(1, 5),
            effect=random.choice(artifact_effects)
        )

        if isinstance(name_or_power, str):
            artifact.name = name_or_power
        elif isinstance(name_or_power, int):
            artifact.durability = max(1, name_or_power)

        self.cards["artifacts"].append(artifact.name.lower())
        return artifact

    def create_themed_deck(self, size: int) -> Dict:
        """
        Create a fantasy-themed deck.

        Args:
            size: Number of cards in the deck

        Returns:
            A dictionary containing deck information of created Cards.
        """
        deck_cards: list[Card] = []

        creatures_count = size // 2
        spells_count = size // 2
        artifacts_count = size - creatures_count - spells_count

        for _ in range(creatures_count):
            deck_cards.append(self.create_creature())

        for _ in range(spells_count):
            deck_cards.append(self.create_spell())

        for _ in range(artifacts_count):
            deck_cards.append(self.create_artifact())

        return {"deck": deck_cards}

    def get_supported_types(self) -> Dict:
        """
        Get the types of cards this factory can create.

        Returns:
            A dictionary of supported card types
        """
        return {
            'creatures': "'Fire Dragon', 'Goblin Warrior' ...",
            'spells': "'Fireball', 'Ice Lance' ...",
            'artifacts': "'Amulet of Strength', 'Ring of Invisibility' ..."
        }
