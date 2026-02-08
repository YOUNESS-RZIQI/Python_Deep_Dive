"""
EliteCard.py - Elite card with both combat and magical capabilities
"""
from typing import Dict, List
from ex0.Card import Card, Rarity
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """
    Elite card that combines Card, Combatable, and Magical interfaces.
    These are powerful cards with both physical combat and magical abilities.
    """

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: Rarity,
        attack_power: int,
        defense_power: int,
        magic_power: int
    ) -> None:
        """
        Initialize an elite card with combat and magic stats.

        Args:
            name: The name of the elite card
            cost: The mana cost to play this card
            rarity: The rarity tier of the card (Rarity enum)
            attack_power: Physical attack power
            defense_power: Defense capability
            magic_power: Magical power level

        Raises:
            ValueError: If any power stat is not a positive integer
        """
        super().__init__(name, cost, rarity)

        # Validate all power stats are positive integers
        if not isinstance(attack_power, int) or attack_power <= 0:
            raise ValueError("Attack power must be a positive integer")
        if not isinstance(defense_power, int) or defense_power <= 0:
            raise ValueError("Defense power must be a positive integer")
        if not isinstance(magic_power, int) or magic_power <= 0:
            raise ValueError("Magic power must be a positive integer")

        self.attack_power = attack_power
        self.defense_power = defense_power
        self.magic_power = magic_power
        self.current_mana = 0

    def play(self, game_state: Dict) -> Dict:
        """
        Play this elite card by deploying it with all its capabilities.

        Args:
            game_state: Current state of the game

        Returns:
            A dictionary containing the result of playing the elite card
        """
        # Use game_state information if available
        card_name = game_state.get('card_name', self.name)
        available_mana = game_state.get('available_mana', 0)

        return {
            'card_played': card_name,
            'mana_used': self.cost,
            'effect': 'Elite warrior deployed with combat and magic abilities',
            'mana_remaining': (available_mana - self.cost
                               if available_mana >= self.cost else 0)
        }

    def attack(self, target) -> Dict:
        """
        Attack a target using physical combat.

        Args:
            target: The target to attack

        Returns:
            A dictionary containing the attack result
        """
        target_name = target if isinstance(target, str) else getattr(target,
                                                                     'name',
                                                                     'Unknown')

        return {
            'attacker': self.name,
            'target': target_name,
            'damage': self.attack_power,
            'combat_type': 'melee'
        }

    def defend(self, incoming_damage: int) -> Dict:
        """
        Defend against incoming damage.

        Args:
            incoming_damage: Amount of damage being dealt

        Returns:
            A dictionary containing the defense result
        """
        damage_blocked = min(self.defense_power, incoming_damage)
        damage_taken = max(0, incoming_damage - self.defense_power)

        return {
            'defender': self.name,
            'damage_taken': damage_taken,
            'damage_blocked': damage_blocked,
            'still_alive': True  # Elite cards are tough!
        }

    def get_combat_stats(self) -> Dict:
        """
        Get the combat statistics of this elite card.

        Returns:
            A dictionary containing combat-related statistics
        """
        return {
            'name': self.name,
            'attack_power': self.attack_power,
            'defense_power': self.defense_power,
            'combat_ready': True
        }

    def cast_spell(self, spell_name: str, targets: List) -> Dict:
        """
        Cast a magical spell on the given targets.

        Args:
            spell_name: Name of the spell to cast
            targets: List of targets for the spell

        Returns:
            A dictionary containing the spell cast result
        """
        mana_cost = len(spell_name) // 2  # Simple mana cost calculation

        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': [str(t) for t in targets],
            'mana_used': mana_cost
        }

    def channel_mana(self, amount: int) -> Dict:
        """
        Channel mana to increase magical reserves.

        Args:
            amount: Amount of mana to channel

        Returns:
            A dictionary containing the channeling result
        """
        self.current_mana += amount

        return {
            'channeled': amount,
            'total_mana': self.current_mana
        }

    def get_magic_stats(self) -> Dict:
        """
        Get the magical statistics of this elite card.

        Returns:
            A dictionary containing magic-related statistics
        """
        return {
            'name': self.name,
            'magic_power': self.magic_power,
            'current_mana': self.current_mana,
            'spell_ready': self.current_mana >= 1
        }

    def get_card_info(self) -> Dict:
        """
        Get comprehensive information about this elite card.

        Returns:
            A dictionary containing all card information
        """
        info = super().get_card_info()
        info['attack_power'] = self.attack_power
        info['defense_power'] = self.defense_power
        info['magic_power'] = self.magic_power
        return info
