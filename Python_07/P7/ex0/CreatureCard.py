"""
CreatureCard.py - Concrete implementation of a creature card
"""
from typing import Dict
from ex0.Card import Card, Rarity


class CreatureCard(Card):
    """
    Concrete implementation of a creature card.
    Creatures have attack and health values and can engage in combat.
    """

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: Rarity,
        attack: int,
        health: int
    ) -> None:
        """
        Initialize a creature card with combat stats.

        Args:
            name: The name of the creature
            cost: The mana cost to summon this creature
            rarity: The rarity tier of the card (Rarity enum)
            attack: The attack power of the creature
            health: The health points of the creature

        Raises:
            ValueError: If attack or health are not positive integers
        """
        super().__init__(name, cost, rarity)

        # Validate attack and health are positive integers
        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("Attack must be a positive integer")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("Health must be a positive integer")

        self.attack = attack
        self.health = health

    def play(self, game_state: Dict) -> Dict:
        """
        Play this creature card by summoning it to the battlefield.

        Args:
            game_state: Current state of the game

        Returns:
            A Dictionary containing the result of playing the creature
        """
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Creature summoned to battlefield'
        }

    def attack_target(self, target: 'CreatureCard') -> Dict:
        """
        Attack another creature or target.

        Args:
            target: The target creature to attack

        Returns:
            A Dictionary containing the combat result
        """
        return {
            'attacker': self.name,
            'target': target.name,
            'damage_dealt': self.attack,
            'combat_resolved': True
        }

    def get_card_info(self) -> Dict:
        """
        Get comprehensive information about this creature card.

        Returns:
            A Dictionary containing all card information including combat stats
        """
        info = super().get_card_info()
        info['attack'] = self.attack
        info['health'] = self.health
        return info
