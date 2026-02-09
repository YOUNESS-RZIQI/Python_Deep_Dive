from ex0.Card import Rarity
from ex2.EliteCard import EliteCard
import traceback
import sys


def main():
    """
    Demonstrate the ability system with multiple interfaces.
    """
    print("=== DataDeck Ability System ===\n")

    error_count = 0

    arcane_warrior = EliteCard(
        "Arcane Warrior",
        6,
        Rarity.LEGENDARY,
        5,
        5,
        8
    )

    print("EliteCard capabilities:")

    card_methods = ['play', 'get_card_info', 'is_playable']
    combatable_methods = ['attack', 'defend', 'get_combat_stats']
    magical_methods = ['cast_spell', 'channel_mana', 'get_magic_stats']

    print(f"- Card: {card_methods}")
    print(f"- Combatable: {combatable_methods}")
    print(f"- Magical: {magical_methods}\n")

    print("\nPlaying Arcane Warrior (Elite Card):\n")

    # Combat phase
    try:
        print("Combat phase:")
        attack_result = arcane_warrior.attack("Enemy")
        print(f"Attack result: {attack_result}")
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
        defend_result = arcane_warrior.defend(2)
        print(f"Defense result: {defend_result}\n")
    except Exception:
        print()
        sys.stderr.write("\033[31m")
        traceback.print_exc()
        print()
        error_count += 1
    finally:
        sys.stderr.write("\033[0m")
        sys.stderr.flush()

    # Magic phase:
    try:
        print("Magic phase:")
        spell_result = arcane_warrior.cast_spell("Fireball", ["Enemy1",
                                                              "Enemy2"])
        print(f"Spell cast: {spell_result}")

        arcane_warrior.channel_mana(4)
        mana_result = arcane_warrior.channel_mana(3)
        print(f"Mana channel: {mana_result}\n")
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
        print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
