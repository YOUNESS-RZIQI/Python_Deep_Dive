import random
from ex0.Card import Card, Rarity
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard, EffectType
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory
from typing import Dict


class FantasyCardFactory(CardFactory):
    """
    Factory for creating fantasy-themed cards.
    Creates dragons, goblins, elemental spells, and magical artifacts.
    """

    def __init__(self) -> None:
        """Initialize the fantasy card factory with card templates."""
        self.data = {}

    def create_creature(
        self,
        name_or_power: str | int | None = None
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
            "Goblin",
        ]

        rar = random.choice(list(Rarity))

        creature = CreatureCard(
            name=random.choice(creatures_list),
            cost=random.randint(1, 9),
            rarity=rar.value,
            attack=random.randint(1, 9),
            health=random.randint(1, 9),
        )

        if isinstance(name_or_power, str):
            creature.name = name_or_power
        elif isinstance(name_or_power, int):
            creature.cost = name_or_power

        return creature

    def create_spell(
        self,
        name_or_power: str | int | None = None
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

        rar = random.choice(list(Rarity))
        eff = random.choice(list(EffectType))

        spell = SpellCard(
            name=random.choice(spell_names),
            cost=random.randint(1, 9),
            rarity=rar.value,
            effect_type=eff.value
        )

        if isinstance(name_or_power, str):
            spell.name = name_or_power
        elif isinstance(name_or_power, int):
            spell.cost = name_or_power

        return spell

    def create_artifact(
        self,
        name_or_power: str | int | None = None
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
            "Become invisible for one turn",
            "Draw an extra card each turn",
            "Double your attack once per turn",
            "Reduce damage taken by 2",
            "Negate enemy spell once",
            "Increase attack damage by 2",
            "Extra defense to all creatures",
            "Gain extra movement speed this turn",
            "Increase spell damage by 2",
            "Gain extra mana each turn"
        ]

        rar = random.choice(list(Rarity))

        num = random.randint(0, len(artifact_names) - 1)
        artifact = ArtifactCard(
            name=(artifact_names[num]),
            cost=random.randint(1, 9),
            rarity=rar.value,
            durability=random.randint(1, 5),
            effect=(artifact_effects[num])
        )

        if isinstance(name_or_power, str):
            artifact.name = name_or_power
        elif isinstance(name_or_power, int):
            artifact.durability = max(1, name_or_power)

        return artifact

    def create_themed_deck(self, size: int) -> Dict:
        """
        Create a fantasy-themed deck.

        Args:
            size: Number of cards in the deck

        Returns:
            A dictionary containing deck information of created Cards.
        """
        if size >= 32 or size < 0:
            raise ValueError("the Size must be : -1 < size < 32")
        deck_cards: list[Card] = []
        used_names = set()

        while len(deck_cards) < size:
            card = random.choice([
                self.create_creature,
                self.create_spell,
                self.create_artifact
            ])
            card = card()
            if card.name not in used_names:
                deck_cards.append(card)
                used_names.add(card.name)

        return {"deck": deck_cards}

    def get_supported_types(self) -> Dict:
        """
        Get the types of cards this factory can create.

        Returns:
            A dictionary of supported card types
        """
        return {
            "creatures": ["Fire Dragon", "Goblin Warrior"],
            "spells": ["Fireball"],
            "artifacts": ["mana_ring"]
        }

    def register_data_of_card_to_creat(self, card_id: str,
                                       class_reference: Card,
                                       constructor_data: tuple[str, ...]):
        if not isinstance(card_id, str):
            raise TypeError("card_id must be of type (str)")
        if not isinstance(class_reference, Card):
            raise TypeError("Class_reference must be of type (Card)")
        if not isinstance(constructor_data, tuple):
            raise TypeError("Card_type must be of type (tuple)")

        self.data.update({card_id: {"data": constructor_data,
                                    "clas": class_reference}})

    def creat_card(self, card_id: str):
        if not isinstance(card_id, str):
            raise TypeError("card_to_creat must be (str)")

        data = (item for item in self.data[card_id]["data"])
        clas = self.data[card_id]["clas"]
        obj = clas(data)
        return obj

