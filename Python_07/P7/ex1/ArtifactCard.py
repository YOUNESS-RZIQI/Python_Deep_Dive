from typing import Dict
from ex0.Card import Card


class ArtifactCard(Card):
    """
    Concrete implementation of an artifact card.
    Artifacts are permanent game modifiers that remain in play.
    """

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
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
            Exception: If durability is not a positive integer
        """
        super().__init__(name, cost, rarity)

        if not isinstance(durability, int) or durability <= 0:
            raise Exception("Durability must be a positive integer")
        if not isinstance(effect, str):
            raise TypeError("in ArtifactCard Calss in __init__ the effect"
                            " should be of type (str)")
        self.durability = durability
        self.effect = effect
        self.is_in_battelfield = False

    def play(self, game_state: Dict) -> Dict:
        """
        Play this artifact card by deploying it to the battlefield.

        Args:
            game_state: Current state of the game

        Returns:
            A Dictionary containing the result of playing the artifact
        """
        if self.name in game_state["battlefield"]:
            raise ValueError(f"{self.name} is alredy in battlefield")
        if not isinstance(game_state, Dict):
            raise TypeError("gama_state must be Dict type.")

        if not self.is_playable(game_state["mana"]):
            return {"error": "No Enough Mana"}
        game_state["mana"] -= self.cost
        game_state["battlefield"] += [self.name]
        self.is_in_battelfield = True
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f'Permanent: {self.effect}'
        }

    def activate_ability(self) -> Dict:
        """
        Activate the artifact"s ongoing ability.

        Returns:
            A Dictionary containing the activation result
        """
        if not self.is_in_battelfield:
            raise ValueError("you can not activete ability of not ArtifactCard"
                             " in the battalefield")
        return {
            "artifact": self.name,
            "ability": self.effect,
            "durability": self.durability,
            "active": self.durability > 0
        }

    def get_card_info(self) -> Dict:
        """
        Get comprehensive information about this artifact card.

        Returns:
            A Dictionary containing all card information
        """
        info = super().get_card_info()
        info["durability"] = self.durability
        info["effect"] = self.effect
        return info
