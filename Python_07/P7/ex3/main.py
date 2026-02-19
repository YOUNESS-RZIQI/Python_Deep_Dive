from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine
import sys
import traceback
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex0.Card import Rarity


def main():
    """
    Demonstrate the game engine with Abstract Factory and Strategy patterns.
    """

    try:
        print("=== DataDeck Game Engine ===\n")
        factory = FantasyCardFactory()
        strategy = AggressiveStrategy()

        print("Configuring Fantasy Card Game...")
        print(f"Factory: {factory.__class__.__name__}")
        print(f"Strategy: {strategy.get_strategy_name()}")

        supported_types = factory.get_supported_types()
        print(f"Available types: {supported_types}\n")

        engine = GameEngine()
        engine.how_mush_to_creat = 3
        engine.configure_engine(factory, strategy)
        engine.strategy.mana = 20

        print("Simulating aggressive turn...")
        turn_result = engine.simulate_turn()

        print(f"Hand: [{turn_result['hand']}]")
        print("\nTurn execution:")
        print(f"Strategy: {turn_result['strategy']}")
        print(f"Actions: {turn_result['actions']}\n")

        print("Game Report:")
        status = engine.get_engine_status()
        print(f"{status}\n")

        print("Abstract Factory + Strategy Pattern: Maximum"
              " flexibility achieved!")

    except Exception:
        print()
        sys.stderr.write("\033[31m")
        traceback.print_exc()
        print()


if __name__ == "__main__":
    main()
