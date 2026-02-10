"""
main.py - Demonstration of the Game Engine
"""
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main():
    """
    Demonstrate the game engine with Abstract Factory and Strategy patterns.
    """
    print("=== DataDeck Game Engine ===\n")

    # Create factory and strategy
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    print("Configuring Fantasy Card Game...")
    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")

    # Show available card types
    supported_types = factory.get_supported_types()
    print(f"Available types: {supported_types}\n")

    # Create and configure game engine
    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    # Simulate a turn
    print("Simulating aggressive turn...\n")
    turn_result = engine.simulate_turn()

    print(f"Hand: {turn_result['hand']}")
    print(f"\nTurn execution:")
    print(f"Strategy: {turn_result['strategy']}")
    print(f"Actions: {turn_result['actions']}\n")

    # Get engine report
    print("Game Report:")
    status = engine.get_engine_status()
    print(f"{status}\n")

    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()