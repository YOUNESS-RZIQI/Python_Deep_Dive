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

    error_count = 0
    try:
        fire_dragon = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY, 7, 5)
    except ValueError as e:
        print("Error:", e)
        return
    try:
        goblin_warrior = CreatureCard("Goblin Warrior", 2, Rarity.COMMON, 2, 2)
    except ValueError as e:
        print("Error:", e)
        return

    try:
        print("CreatureCard Info:")
        print(fire_dragon.get_card_info())
        print()
    except Exception:
        print()
        sys.stderr.write("\033[31m")
        traceback.print_exc()
        print()
        error_count += 1
    finally:
        sys.stderr.write("\033[0m")
        sys.stderr.flush()

    try:
        available_mana = 6
        print(f"Playing Fire Dragon with {available_mana} mana available:")
        print(f"Playable: {fire_dragon.is_playable(available_mana)}")
    except Exception:
        print()
        sys.stderr.write("\033[31m")
        traceback.print_exc()
        print()
        error_count += 1
    finally:
        sys.stderr.write("\033[0m")
        sys.stderr.flush()

    try:
        game_state = fire_dragon.ge_card_info()
        play_result = fire_dragon.play(game_state)
        print(f"Play result: {play_result}")
        print()
    except Exception:
        print()
        sys.stderr.write("\033[31m")
        traceback.print_exc()
        print()
        error_count += 1
    finally:
        sys.stderr.write("\033[0m")
        sys.stderr.flush()

    try:
        print("Fire Dragon attacks Goblin Warrior:")
        attack_result = fire_dragon.attack_target(goblin_warrior)
        print(f"Attack result: {attack_result}")
        print()
    except Exception:
        print()
        sys.stderr.write("\033[31m")
        traceback.print_exc()
        print()
        error_count += 1
    finally:
        sys.stderr.write("\033[0m")
        sys.stderr.flush()

    try:
        insufficient_mana = 3
        print(f"Testing insufficient mana ({insufficient_mana} available):")
        print(f"Playable: {fire_dragon.is_playable(insufficient_mana)}")
        print()
    except Exception:
        print()
        sys.stderr.write("\033[31m")
        traceback.print_exc()
        print()
        error_count += 1
    finally:
        sys.stderr.write("\033[0m")
        sys.stderr.flush()

    if error_count == 0:
        print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
