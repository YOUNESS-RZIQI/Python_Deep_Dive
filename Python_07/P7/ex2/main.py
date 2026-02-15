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
            Rarity.LEGENDARY.value,
            5,
            5,
        )

        enemy = EliteCard(
            "Enemy",
            1,
            Rarity.COMMON.value,
            3,
            3,
        )

        enemy1 = EliteCard(
            "Enemy1",
            1,
            Rarity.COMMON.value,
            3,
            3,
        )

        enemy2 = EliteCard(
            "Enemy2",
            1,
            Rarity.COMMON.value,
            3,
            3,
        )

        print("EliteCard capabilities:")

        card_methods = ['play', 'get_card_info', 'is_playable']
        combatable_methods = ['attack', 'defend', 'get_combat_stats']
        magical_methods = ['cast_spell', 'channel_mana', 'get_magic_stats']

        print(f"- Card: {card_methods}")
        print(f"- Combatable: {combatable_methods}")
        print(f"- Magical: {magical_methods}\n")

        print("\nPlaying Arcane Warrior (Elite Card):\n")
        arcane_warrior.mana = 10
        mana = arcane_warrior.mana
        game_state = {"mana": mana, "battlefield": []}
        # arcane_warrior.mana = game_state["mana"]
        arcane_warrior.play(game_state)
        enemy.play(game_state)
        print(f"\n{game_state['battlefield']}\n")
        print("Combat phase:")
        attack_result = arcane_warrior.attack(enemy)
        print(f"Attack result: {attack_result}")

        defend_result = arcane_warrior.defend(random.randint(1, 8))
        print(f"Defense result: {defend_result}\n")

        print("Magic phase:")
        enemy1.play(game_state)
        enemy2.play(game_state)
        spell_result = arcane_warrior.cast_spell("Fireball", [enemy1,
                                                              enemy2])
        print(f"Spell cast: {spell_result}")

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
