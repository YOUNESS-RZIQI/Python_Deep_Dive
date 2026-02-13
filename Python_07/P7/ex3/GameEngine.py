from typing import Dict, Optional
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
import random


class GameEngine:
    """
    Game engine that orchestrates card creation and gameplay.
    Combines Abstract Factory and Strategy patterns.
    """

    def __init__(self) -> None:
        """Initialize the game engine."""
        self.factory: Optional[CardFactory] = None
        self.strategy: Optional[GameStrategy] = None
        self.turns_simulated: int = 0
        self.total_damage: int = 0
        self.cards_created: int = 0

    def configure_engine(
        self,
        factory: CardFactory,
        strategy: GameStrategy
    ) -> None:
        """
        Configure the game engine with a factory and strategy.

        Args:
            factory: Card factory to use for creating cards
            strategy: Game strategy to use for gameplay
        """
        self.factory: FantasyCardFactory = factory
        self.strategy: AggressiveStrategy = strategy
        self.cards_created = 0
        self.turns_simulated = 0

    def simulate_turn(self) -> Dict:
        """
        Simulate a game turn using the configured factory and strategy.

        Returns:
            A dictionary containing the turn simulation result

        Raises:
            ValueError: If engine is not configured
        """
        if not self.factory or not self.strategy:
            raise ValueError("Engine must be configured before simulating"
                             "turns")

        hand = self.factory.create_themed_deck(5)["deck"]

        self.cards_created += len(hand)

        battlefield = []

        self.strategy.mana = random.randint(4, 9)
        turn_result = self.strategy.execute_turn(hand, battlefield)
        self.turns_simulated += 1
        self.total_damage += turn_result["damage_dealt"]

        return {
            "actions": turn_result,
            "strategy": self.strategy.get_strategy_name(),
            "hand": [(card.name + f"({card.cost})") for card in hand]
        }

    def get_engine_status(self) -> Dict:
        """
        Get the current status of the game engine.

        Returns:
            A dictionary containing engine status information
        """
        return {
            'turns_simulated': self.turns_simulated,
            'strategy_used': self.strategy.get_strategy_name(),
            'total_damage': self.total_damage,
            'cards_created': self.cards_created
        }
