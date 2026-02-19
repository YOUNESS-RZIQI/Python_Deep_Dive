"""
main.py - Demonstration of the Tournament Platform
"""
from ex0.Card import Rarity
from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    """
    Demonstrate the tournament platform with ranking system.
    """
    print("=== DataDeck Tournament Platform ===\n")

    # Create tournament platform
    platform = TournamentPlatform()

    # Create tournament cards
    print("Registering Tournament Cards...\n")

    fire_dragon = TournamentCard(
        "Fire Dragon",
        5,
        Rarity.LEGENDARY.value,
        7,
        5
    )

    ice_wizard = TournamentCard(
        "Ice Wizard",
        4,
        Rarity.EPIC.value,
        5,
        6
    )

    # Register cards
    dragon_id = platform.register_card(fire_dragon)
    wizard_id = platform.register_card(ice_wizard)

    # Show card interfaces
    print(f"{fire_dragon.name} (ID: {dragon_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {fire_dragon.calculate_rating()}")
    print(f"- Record: {fire_dragon.wins}-{fire_dragon.losses}\n")

    print(f"{ice_wizard.name} (ID: {wizard_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {ice_wizard.calculate_rating()}")
    print(f"- Record: {ice_wizard.wins}-{ice_wizard.losses}\n")

    # Create a match
    print("Creating tournament match...\n")
    match_result = platform.create_match(dragon_id, wizard_id)
    print(f"Match result: {match_result}\n")

    # Show leaderboard
    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for entry in leaderboard:
        print(f"{entry['rank']}. {entry['name']} - "
              f"Rating: {entry['rating']} ({entry['record']})")

    print()

    # Generate platform report
    print("Platform Report:")
    report = platform.generate_tournament_report()
    print(f"{report}\n")

    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
