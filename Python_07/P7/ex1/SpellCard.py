from typing import Dict, List
from ex0.Card import Card, CardType
from ex0.CreatureCard import CreatureCard
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
        rarity: str,
        effect_type: str
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
        if not isinstance(effect_type, str):
            raise TypeError("effect_type must be of type (str)")
        self.effect_type = effect_type
        self.is_in_battelfield = False

    def play(self, game_state: Dict) -> Dict:
        """
        Play this spell card by casting it.

        Args:
            game_state: Current state of the game

        Returns:
            A Dictionary containing the result of casting the spell
        """
        if self.name in game_state["battlefield"]:
            raise ValueError(f"{self.name} is alredy in battlefield")
        if not isinstance(game_state, Dict):
            raise TypeError("gama_state must be Dict type.")

        if not self.is_playable(game_state["mana"]):
            raise ValueError("Error:  No Enough Mana")

        game_state["mana"] -= self.cost
        game_state["battlefield"] += [self.name]
        self.is_in_battelfield = True

        effect_descriptions = {
            EffectType.DAMAGE.value: f"Deal {self.cost} damage to target",
            EffectType.HEAL.value: f"Heal {self.cost * 2} health",
            EffectType.BUFF.value: f"Grant +{self.cost}/+{self.cost} buff",
            EffectType.DEBUFF.value: f"Apply -{self.cost}/-{self.cost} debuff"
        }

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effect_descriptions.get(
                self.effect_type, "Unknown effect")
        }

    def resolve_effect(self, targets: List[CreatureCard]) -> Dict:
        """
        Resolve the spell"s effect on the given targets.

        Args:
            targets: List of targets affected by the spell

        Returns:
            A Dictionary containing the resolution result
        """
        if not self.is_in_battelfield:
            raise ValueError("you can not do resolve_effect "
                             "before playing the card ??")
        for target in targets:
            if not target.is_in_battelfield:
                raise ValueError("you can not do resolve_effect "
                                 "on target not in battelfield ??")
            if self == target:
                raise ValueError("! you Can Not Attack Your Self  !")

        if self.effect_type == "":
            raise ValueError("Error: ! Effect alredy Consumed !")

        result = {
            "spell": self.name,
            "effect_type": self.effect_type,
            "targets": [target for target in targets],
            "consumed": True
        }
        self.effect_type = ""
        return result

    def get_card_info(self) -> Dict:
        """
        Get comprehensive information about this spell card.

        Returns:
            A Dictionary containing all card information
        """
        info = super().get_card_info()
        info["type"] = CardType.SPELL.value
        info["effect_type"] = self.effect_type
        return info
