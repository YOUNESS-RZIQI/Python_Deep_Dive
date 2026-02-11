"""
main.py - Demonstration of the Card Foundation
"""
from ex0.Card import Rarity
from ex0.CreatureCard import CreatureCard
import sys
import traceback


def main():
    """
    Demonstrate the abstract base class design and concrete implementation.
    """
    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    try:

        fire_dragon = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY, 7, 5)

        goblin_warrior = CreatureCard("Goblin Warrior", 2, Rarity.COMMON, 2, 2)

        print("CreatureCard Info:")
        print(fire_dragon.get_card_info())
        print()

        available_mana = 6
        print(f"Playing Fire Dragon with {available_mana} mana available:")
        print(f"Playable: {fire_dragon.is_playable(available_mana)}")

        game_state = {"mana": 7, "battlefield": []}
        goblin_warrior.play(game_state)
        play_result = fire_dragon.play(game_state)
        print(f"Play result: {play_result}")
        print()


        print(game_state["battlefield"])
        # print("Fire Dragon attacks Goblin Warrior:")
        # attack_result = fire_dragon.attack_target(goblin_warrior)
        # print(f"Attack result: {attack_result}")
        # print()

        # insufficient_mana = 3
        # print(f"Testing insufficient mana ({insufficient_mana} available):")
        # print(f"Playable: {fire_dragon.is_playable(insufficient_mana)}")
        # print()

        # print("Abstract pattern successfully demonstrated!")
    except Exception:
        print()
        sys.stderr.write("\033[31m")
        traceback.print_exc()
        print()

    finally:
        sys.stderr.write("\033[0m")
        sys.stderr.flush()


if __name__ == "__main__":
    main()
