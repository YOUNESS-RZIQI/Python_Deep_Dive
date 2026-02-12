"""
main.py - Demonstration of the Deck Builder
"""
from ex0.Card import Rarity
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard, EffectType
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
import sys
import traceback


def main():
    """
    Demonstrate the deck builder system with polymorphism.
    """
    print("=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...\n")

    deck = Deck()

    try:
        fire_dragon = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY, 7, 5)
        lightning_bolt = SpellCard("Lightning Bolt", 3, Rarity.COMMON,
                                   EffectType.DAMAGE)
        mana_crystal = ArtifactCard("Mana Crystal", 2, Rarity.UNCOMMON, 5,
                                    "+1 mana per turn")

        deck.add_card(lightning_bolt)
        deck.add_card(mana_crystal)
        deck.add_card(fire_dragon)

        stats = deck.get_deck_stats()
        print(f"Deck stats: {stats}\n")

        deck.shuffle()

        print("Drawing and playing cards:\n")

        game_state = {"mana": 10, "battlefield": []}
        for no_matter in range(len(deck.cards)):
            card = deck.draw_card()
            if card:
                card_type = card.__class__.__name__.replace("Card", "")
                print(f"Drew: {card.name} ({card_type})")
                play_result = card.play(game_state)
                print(f"Play result: {play_result}\n")

    except Exception:
        print()
        sys.stderr.write("\033[31m")
        traceback.print_exc()
        print()

    print("Polymorphism in action: Same interface, different card "
          "behaviors!")


if __name__ == "__main__":
    main()
