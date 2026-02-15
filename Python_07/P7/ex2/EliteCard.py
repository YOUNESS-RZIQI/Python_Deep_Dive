from typing import Dict, List
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """
    Elite card that combines Card, Combatable, and Magical interfaces.
    These are powerful cards with both physical combat and magical abilities.
    """

    mana = 0

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int,
        defense_power: int,
    ) -> None:
        """
        Initialize an elite card with combat and magic stats.

        Args:
            name: The name of the elite card
            cost: The mana cost to play this card
            rarity: The rarity tier of the card (Rarity enum)
            attack_power: Physical attack power
            defense_power: Defense capability

        Raises:
            ValueError: If any power stat is not a positive integer
        """
        super().__init__(name, cost, rarity)

        if not isinstance(attack_power, int) or attack_power <= 0:
            raise ValueError("Attack power must be a positive integer")
        if not isinstance(defense_power, int) or defense_power <= 0:
            raise ValueError("Defense power must be a positive integer")

        self.attack_power = attack_power
        self.defense_power = defense_power
        self.is_in_battelfield = False

    def play(self, game_state: Dict) -> Dict:
        """
        Play this elite card by deploying it with all its capabilities.

        Args:
            game_state: Current state of the game

        Returns:
            A dictionary containing the result of playing the elite card
        """
        if self.name in game_state["battlefield"]:
            raise ValueError(f"{self.name} is alredy in battlefield")
        if not isinstance(game_state, Dict):
            raise ValueError("gama_state must be Dict type.")
        if not self.is_playable(game_state["mana"]):
            return {"Error:": "No enoughf mana"}
        game_state["mana"] -= self.cost
        self.mana -= self.cost
        game_state["battlefield"] += [self.name]
        self.is_in_battelfield = True

        return {
            "card_played": self.name,
            "mana_used": self.cost,
        }

    def attack(self, target: CreatureCard) -> Dict:
        """
        Attack a target using physical combat.
        Has a chance for critical hits with bonus damage.

        Args:
            target: The target to attack

        Returns:
            A dictionary containing the attack result
        """
        if not self.is_in_battelfield or not target.is_in_battelfield:
            raise ValueError("You can not attack wiht no Card "
                             "in the battelfield")

        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self.attack_power,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> Dict:
        """
        Defend against incoming damage.
        Has a chance to dodge and take no damage.

        Args:
            incoming_damage: Amount of damage being dealt

        Returns:
            A dictionary containing the defense result
        """
        if not self.is_in_battelfield:
            raise ValueError("You can not defend wiht no Creature "
                             "in the battelfield")

        damage_blocked = min(incoming_damage, self.defense_power)
        new_defese_power = self.defense_power - incoming_damage
        self.defense_power = new_defese_power if new_defese_power >= 0 else 0
        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "damage_blocked": damage_blocked,
            "still_alive": self.defense_power > incoming_damage
        }

    def get_combat_stats(self) -> Dict:
        """
        Get the combat statistics of this elite card.

        Returns:
            A dictionary containing combat-related statistics
        """
        return {
            "name": self.name,
            "attack_power": self.attack_power,
            "defense_power": self.defense_power,
        }

    def cast_spell(self, spell_name: str, targets: List["EliteCard"]) -> Dict:
        """
        Cast a magical spell on the given targets.

        Args:
            spell_name: Name of the spell to cast
            targets: List of targets for the spell

        Returns:
            A dictionary containing the spell cast result
        """
        if not self.is_in_battelfield:
            raise ValueError("You can not cast_spell wiht no Creature "
                             "in the battelfield")
        for tar in targets:
            if not tar.is_in_battelfield:
                raise ValueError("You can not cast_spell wiht no Creature "
                                 "in the battelfield")

        if not isinstance(spell_name, str) or not isinstance(targets, List):
            raise ValueError("spell_name must be (str) and "
                             "targets must be (List)")
        base_mana = len(targets) * 2

        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": [t.name for t in targets],
            "mana_used": base_mana,
        }

    def channel_mana(self, amount: int) -> Dict:
        """
        Channel mana to increase magical reserves.

        Args:
            amount: Amount of mana to channel

        Returns:
            A dictionary containing the channeling result
        """
        self.mana += amount

        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> Dict:
        """
        Get the magical statistics of this elite card.

        Returns:
            A dictionary containing magic-related statistics
        """
        return {self.name: "Not emplimented yet, there is no info about it ?"}
        ...

    def get_card_info(self) -> Dict:
        """
        Get comprehensive information about this elite card.

        Returns:
            A dictionary containing all card information
        """
        info = super().get_card_info()
        info["attack_power"] = self.attack_power
        info["defense_power"] = self.defense_power
        return info
