from ex0.Card import Rarity
from ex2.EliteCard import EliteCard
import traceback
import sys
import random


def main():
    """
    Demonstrate the ability system with multiple interfaces.
    """
    print("=== DataDeck Ability System ===\n")

    try:
        arcane_warrior = EliteCard(
            "Arcane Warrior",
            6,
            Rarity.LEGENDARY,
            5,
            5,
        )

        print("EliteCard capabilities:")

        card_methods = ['play', 'get_card_info', 'is_playable']
        combatable_methods = ['attack', 'defend', 'get_combat_stats']
        magical_methods = ['cast_spell', 'channel_mana', 'get_magic_stats']

        print(f"- Card: {card_methods}")
        print(f"- Combatable: {combatable_methods}")
        print(f"- Magical: {magical_methods}\n")

        print("\nPlaying Arcane Warrior (Elite Card):\n")

        print("Combat phase:")
        attack_result = arcane_warrior.attack("Enemy")
        print(f"Attack result: {attack_result}")

        defend_result = arcane_warrior.defend(random.randint(1, 8))
        print(f"Defense result: {defend_result}\n")

        print("Magic phase:")
        spell_result = arcane_warrior.cast_spell("Fireball", ["Enemy1",
                                                              "Enemy2"])
        print(f"Spell cast: {spell_result}")

        arcane_warrior.channel_mana(4)
        mana_result = arcane_warrior.channel_mana(3)
        print(f"Mana channel: {mana_result}\n")

        print("Multiple interface implementation successful!")
    except Exception:
        print()
        sys.stderr.write("\033[31m")
        traceback.print_exc()
        print()


if __name__ == "__main__":
    main()
