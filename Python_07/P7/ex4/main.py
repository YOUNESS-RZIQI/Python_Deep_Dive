"""
main.py - Demonstration of the Tournament Platform
"""
from ex0.Card import Rarity
from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform
import sys
import traceback
import random


def main():
    """
    Demonstrate the tournament platform with ranking system.
    """
    try:
        print("=== DataDeck Tournament Platform ===\n")

        platform = TournamentPlatform()

        print("Registering Tournament Cards...\n")

        fire_dragon = TournamentCard(
            "Fire Dragon",
            5,
            Rarity.LEGENDARY.value,
            random.randint(1, 7),
            random.randint(1, 7)
        )

        ice_wizard = TournamentCard(
            "Ice Wizard",
            4,
            Rarity.EPIC.value,
            random.randint(1, 7),
            random.randint(1, 7)
        )

        dragon_id = platform.register_card(fire_dragon)
        wizard_id = platform.register_card(ice_wizard)

        print(f"{fire_dragon.name} (ID: {dragon_id}):")
        print("- Interfaces: "
              f"{platform.get_intrfaces()}")
        print(f"- Rating: {fire_dragon.calculate_rating()}")
        print(f"- Record: {fire_dragon.wins}-{fire_dragon.losses}\n")

        print(f"{ice_wizard.name} (ID: {wizard_id}):")
        print("- Interfaces: "
              f"{platform.get_intrfaces()}")
        print(f"- Rating: {ice_wizard.calculate_rating()}")
        print(f"- Record: {ice_wizard.wins}-{ice_wizard.losses}\n")

        print("Creating tournament match...\n")
        match_result = platform.create_match(dragon_id, wizard_id)
        print(f"Match result: {match_result}\n")

        print("Tournament Leaderboard:")
        leaderboard = platform.get_leaderboard()
        for dc in leaderboard:
            print(f"{dc['rank']}. {dc['name']} - "
                  f"Rating: {dc['rating']} ({dc['record']})")

        print()

        print("Platform Report:")
        report = platform.generate_tournament_report()
        print(f"{report}\n")

        print("=== Tournament Platform Successfully Deployed! ===")
        print("All abstract patterns working together harmoniously!")

    except Exception:
        print()
        sys.stderr.write("\033[31m")
        traceback.print_exc()
        print()


if __name__ == "__main__":
    main()
