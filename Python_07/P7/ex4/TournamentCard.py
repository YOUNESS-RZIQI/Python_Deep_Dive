from typing import Dict
import random
from ex0.Card import Card, Rarity
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """Rankable
    Tournament card that combines Card, Combatable, and Rankable interfaces.
    These cards can participate in ranked tournaments and track their performance.
    """

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: Rarity,
        attack_power: int,
        defense_power: int
    ) -> None:
        """
        Initialize a tournament card.

        Args:
            name: The name of the card
            cost: The mana cost to play this card
            rarity: The rarity tier of the card (Rarity enum)
            attack_power: Attack power for combat
            defense_power: Defense capability

        Raises:
            ValueError: If attack_power or defense_power are not positive
        """
        super().__init__(name, cost, rarity)

        if not isinstance(attack_power, int) or attack_power <= 0:
            raise ValueError("Attack power must be a positive integer")
        if not isinstance(defense_power, int) or defense_power <= 0:
            raise ValueError("Defense power must be a positive integer")

        self.attack_power = attack_power
        self.defense_power = defense_power
        self.is_in_battelfield = False

        self.wins = 0
        self.losses = 0
        self.base_rating = 1200

    def play(self, game_state: Dict) -> Dict:
        """
        Play this tournament card.

        Args:
            game_state: Current state of the game

        Returns:
            A dictionary containing the result of playing the card
        """
        if not isinstance(game_state, Dict):
            raise TypeError("game satate must be of type (Dict)")

        if self.name in game_state["battlefield"]:
            raise ValueError(f"{self.name} is alredy in battlefield")

        if not self.is_playable(game_state["mana"]):
            return {"error": "No Enough Mana"}

        game_state["mana"] -= self.cost
        game_state["battlefield"] += [self.name]
        self.is_in_battelfield = True
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournament warrior ready for battle"}

    def attack(self, target: "TournamentCard") -> Dict:
        """
        Attack a target in tournament combat.

        Args:
            target: The target to attack

        Returns:
            A dictionary containing the attack result
        """
        if self == target:
            raise ValueError("! you Can Not Attack Your Self ? !")

        if not self.is_in_battelfield or not target.is_in_battelfield:
            raise ValueError("You can not attack wiht no Creature "
                             "in the battelfield")
        if target.defense_power <= 0:
            return {"error": "The target has No defense_power (alredy death)"}

        combat_resolved = self.attack_power >= target.defense_power
        target.defense_power -= min(target.defense_power, self.attack_power)
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack_power,
            "combat_resolved": combat_resolved
        }

    def calculate_rating(self) -> int:
        """
        Calculate tournament rating based on wins, losses, and base stats.
        Uses a simplified ELO-style calculation.

        Returns:
            The calculated rating
        """
        # Base rating + win bonus - loss penalty + power bonus
        win_bonus = self.wins * 16
        loss_penalty = self.losses * 16
        power_bonus = (self.attack_power + self.defense_power) * 2

        rating = self.base_rating + win_bonus - loss_penalty + power_bonus
        return max(0, rating)  # Rating can't be negative

    def get_tournament_stats(self) -> Dict:
        """
        Get comprehensive tournament statistics.

        Returns:
            A dictionary containing all tournament-related stats
        """
        return {
            "name": self.name,
            "rating": self.calculate_rating(),
            "record": f"{self.wins}-{self.losses}",
            "attack_power": self.attack_power,
            "defense_power": self.defense_power,
            "total_matches": self.wins + self.losses
        }

    # not manchend to be implemented.

    def defend(self, incoming_damage: int) -> Dict:
        """
        Defend against incoming damage in tournament.

        Args:
            incoming_damage: Amount of damage being dealt

        Returns:
            A dictionary containing the defense result
        """
        damage_blocked = min(self.defense_power, incoming_damage)
        damage_taken = max(0, incoming_damage - self.defense_power)

        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": damage_blocked,
            "still_alive": damage_taken < self.defense_power
        }

    def get_combat_stats(self) -> Dict:
        """
        Get combat statistics.

        Returns:
            A dictionary containing combat stats
        """
        return {
            "name": self.name,
            "attack_power": self.attack_power,
            "defense_power": self.defense_power,
            "combat_ready": True
        }

    def update_wins(self, wins: int) -> None:
        """
        Update the number of wins.

        Args:
            wins: Number of wins to add
        """
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        """
        Update the number of losses.

        Args:
            losses: Number of losses to add
        """
        self.losses += losses

    def get_rank_info(self) -> Dict:
        """
        Get ranking information.

        Returns:
            A dictionary containing ranking details
        """
        return {
            "name": self.name,
            "rating": self.calculate_rating(),
            "wins": self.wins,
            "losses": self.losses,
            "win_rate": (self.wins / (self.wins + self.losses) * 100 
                        if (self.wins + self.losses) > 0 else 0.0)
        }

    def get_card_info(self) -> Dict:
        """
        Get comprehensive card information.

        Returns:
            A dictionary containing all card information
        """
        info = super().get_card_info()
        info["attack_power"] = self.attack_power
        info["defense_power"] = self.defense_power
        info["rating"] = self.calculate_rating()
        info["record"] = f"{self.wins}-{self.losses}"
        return info
