"""
main.py - Demonstration of the Ability System
"""
from ex0.Card import Rarity
from ex2.EliteCard import EliteCard


def main():
    """
    Demonstrate the ability system with multiple interfaces.
    """
    print("=== DataDeck Ability System ===\n")

    # Create an elite card
    arcane_warrior = EliteCard(
        "Arcane Warrior",
        6,
        Rarity.LEGENDARY,
        5,
        3,
        8
    )

    # Show that EliteCard implements multiple interfaces
    print("EliteCard capabilities:")

    # Get methods from each interface
    card_methods = ['play', 'get_card_info', 'is_playable']
    combatable_methods = ['attack', 'defend', 'get_combat_stats']
    magical_methods = ['cast_spell', 'channel_mana', 'get_magic_stats']

    print(f"- Card: {card_methods}")
    print(f"- Combatable: {combatable_methods}")
    print(f"- Magical: {magical_methods}\n")

    # Play the card
    game_state = {
        'card_name': 'Arcane Warrior',
        'available_mana': 10
    }
    print(f"Playing {arcane_warrior.name} (Elite Card):")
    play_result = arcane_warrior.play(game_state)
    print(f"Play result: {play_result}\n")

    # Combat phase
    print("Combat phase:")
    attack_result = arcane_warrior.attack("Enemy")
    crit_status = " CRITICAL HIT!" if attack_result.get('critical_hit') else ""
    print(f"Attack result: {attack_result}{crit_status}")

    defend_result = arcane_warrior.defend(5)
    dodge_status = " DODGED!" if defend_result.get('dodged') else ""
    print(f"Defense result: {defend_result}{dodge_status}\n")

    # Magic phase
    print("Magic phase:")
    spell_result = arcane_warrior.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    print(f"Spell cast: {spell_result}")
    print("  (Note: Spell power varies randomly: "
          f"{spell_result['spell_power']})")

    mana_result = arcane_warrior.channel_mana(3)
    print(f"Mana channel: {mana_result}\n")

    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
