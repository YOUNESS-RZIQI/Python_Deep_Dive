"""
TournamentPlatform.py - Platform for managing tournament cards and matches
"""
from typing import Dict, List, Optional
import random
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    """
    Platform management system for organizing tournaments.
    Handles card registration, match creation, and leaderboard management.
    """

    def __init__(self) -> None:
        """Initialize the tournament platform."""
        self.registered_cards: Dict[str, TournamentCard] = {}
        self.matches_played: int = 0
        self.match_history: List[Dict] = []

    def register_card(self, card: TournamentCard) -> str:
        """
        Register a card for tournament play.

        Args:
            card: The tournament card to register

        Returns:
            A unique ID for the registered card
        """
        # Generate unique ID
        card_id = f"{card.name.lower().replace(' ', '_')}_{len(self.registered_cards) + 1:03d}"
        
        self.registered_cards[card_id] = card
        
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> Dict:
        """
        Create and simulate a match between two cards.

        Args:
            card1_id: ID of the first card
            card2_id: ID of the second card

        Returns:
            A dictionary containing the match result

        Raises:
            ValueError: If either card ID is not found
        """
        if card1_id not in self.registered_cards:
            raise ValueError(f"Card ID {card1_id} not found")
        if card2_id not in self.registered_cards:
            raise ValueError(f"Card ID {card2_id} not found")

        card1 = self.registered_cards[card1_id]
        card2 = self.registered_cards[card2_id]

        # Simulate match - simple combat based on attack/defense
        card1_score = card1.attack_power + card1.defense_power
        card2_score = card2.attack_power + card2.defense_power

        # Add some randomness to the match
        card1_score += random.randint(-2, 2)
        card2_score += random.randint(-2, 2)

        # Determine winner
        if card1_score > card2_score:
            winner_id = card1_id
            loser_id = card2_id
            winner = card1
            loser = card2
        else:
            winner_id = card2_id
            loser_id = card1_id
            winner = card2
            loser = card1

        # Calculate rating changes (simplified ELO)
        winner_old_rating = winner.calculate_rating()
        loser_old_rating = loser.calculate_rating()

        # Update wins/losses
        winner.update_wins(1)
        loser.update_losses(1)

        # Calculate new ratings
        winner_new_rating = winner.calculate_rating()
        loser_new_rating = loser.calculate_rating()

        # Record match
        match_result = {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner_new_rating,
            "loser_rating": loser_new_rating,
            "rating_change_winner": winner_new_rating - winner_old_rating,
            "rating_change_loser": loser_new_rating - loser_old_rating
        }

        self.matches_played += 1
        self.match_history.append(match_result)

        return match_result

    def get_leaderboard(self) -> List[Dict]:
        """
        Get the tournament leaderboard sorted by rating.

        Returns:
            A list of dictionaries containing leaderboard entries
        """
        leaderboard = []

        for card_id, card in self.registered_cards.items():
            leaderboard.append({
                "rank": 0,  # Will be set after sorting
                "card_id": card_id,
                "name": card.name,
                "rating": card.calculate_rating(),
                "record": f"{card.wins}-{card.losses}",
                "wins": card.wins,
                "losses": card.losses
            })

        # Sort by rating (highest first)
        leaderboard.sort(key=lambda x: x["rating"], reverse=True)

        # Assign ranks
        for i, entry in enumerate(leaderboard):
            entry["rank"] = i + 1

        return leaderboard

    def generate_tournament_report(self) -> Dict:
        """
        Generate a comprehensive tournament report.

        Returns:
            A dictionary containing tournament statistics
        """
        if not self.registered_cards:
            return {
                "total_cards": 0,
                "matches_played": 0,
                "avg_rating": 0,
                "platform_status": "inactive"
            }

        total_rating = sum(
            card.calculate_rating() 
            for card in self.registered_cards.values()
        )
        avg_rating = total_rating // len(self.registered_cards)

        return {
            "total_cards": len(self.registered_cards),
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active" if self.matches_played > 0 else "ready"
        }

    def get_card_by_id(self, card_id: str) -> Optional[TournamentCard]:
        """
        Get a card by its ID.

        Args:
            card_id: The card's unique ID

        Returns:
            The tournament card, or None if not found
        """
        return self.registered_cards.get(card_id)
