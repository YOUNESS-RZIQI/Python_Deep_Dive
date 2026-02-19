from typing import Dict
from ex0.Card import Card, CardType


class CreatureCard(Card):
    """
    Concrete implementation of a creature card.
    Creatures have attack and health values and can engage in combat.
    """

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        """
        Initialize a creature card with combat stats.

        Args:
            name: The name of the creature
            cost: The mana cost to summon this creature
            rarity: The rarity tier of the card (Rarity enum)
            attack: The attack power of the creature
            health: The health points of the creature

        Raises:
            Exception: If attack or health are not positive integers
        """
        super().__init__(name, cost, rarity)

        if not isinstance(attack, int) or attack <= 0:
            raise Exception("Attack must be a positive integer")
        if not isinstance(health, int) or health <= 0:
            raise Exception("Health must be a positive integer")

        self.attack = attack
        self.health = health
        self.is_in_battelfield = False

    def play(self, game_state: Dict) -> Dict:
        """
        Play this creature card by summoning it to the battlefield.

        Args:
            game_state: Current state of the game

        Returns:
            A Dictionary containing the result of playing the creature
        """
        if self.name in game_state["battlefield"]:
            raise ValueError(f"{self.name} is alredy in battlefield")
        if not isinstance(game_state, Dict):
            raise TypeError("gama_state must be (Dict) type.")
        if not self.is_playable(game_state["mana"]):
            raise ValueError("Error:  No Enough Mana")
        game_state["mana"] -= self.cost
        game_state["battlefield"] += [self.name]
        self.is_in_battelfield = True
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target: "CreatureCard") -> Dict:
        """
        Attack another creature or target.

        Args:
            target: The target creature to attack

        Returns:
            A Dictionary containing the combat result
        """
        if self == target:
            raise ValueError("! you Can Not Attack Your Self ? !")
        if not isinstance(target, CreatureCard):
            raise TypeError("target must be of type (CreatureCard).")
        if not self.is_in_battelfield or not target.is_in_battelfield:
            raise ValueError("if you want to attack you need to be"
                             "in the battelfield.")
        if target.health <= 0:
            return {"error": "The target has No Health (alredy death)"}
        combat_resolved = self.attack >= target.health
        target.health -= min(target.health, self.attack)
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": combat_resolved
        }

    def get_card_info(self) -> Dict:
        """
        Get comprehensive information about this creature card.

        Returns:
            A Dictionary containing all card information including combat stats
        """
        info = super().get_card_info()
        info["type"] = CardType.CREATURE.value
        info["attack"] = self.attack
        info["health"] = self.health
        return info
