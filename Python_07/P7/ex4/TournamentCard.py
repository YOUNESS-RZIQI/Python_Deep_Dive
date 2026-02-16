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

        # Tournament stats
        self.wins = 0
        self.losses = 0
        self.base_rating = 1200  # Starting ELO-style rating

    def play(self, game_state: Dict) -> Dict:
        """
        Play this tournament card.

        Args:
            game_state: Current state of the game

        Returns:
            A dictionary containing the result of playing the card
        """
        card_name = game_state.get("card_name", self.name)
        available_mana = game_state.get("available_mana", 0)

        return {
            "card_played": card_name,
            "mana_used": self.cost,
            "effect": "Tournament warrior ready for battle",
            "mana_remaining": (available_mana - self.cost
                               if available_mana >= self.cost else 0)
        }

    def attack(self, target) -> Dict:
        """
        Attack a target in tournament combat.

        Args:
            target: The target to attack

        Returns:
            A dictionary containing the attack result
        """
        target_name = target if isinstance(target, str) else getattr(
            target, "name", "Unknown"
        )

        # Random critical hit chance
        is_critical = random.random() < 0.2
        damage = self.attack_power
        if is_critical:
            damage = int(self.attack_power * 1.5)

        return {
            "attacker": self.name,
            "target": target_name,
            "damage": damage,
            "critical_hit": is_critical
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
