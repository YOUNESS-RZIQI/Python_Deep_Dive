def achievement_hunter() -> None:

    """
    Achievement Hunter program demonstrating the use of a set.
    """

    try:
        alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
        bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
        charlie = {'level_10', 'treasure_hunter', 'boss_slayer',
                   'speed_demon', 'perfectionist'}

        print("=== Achievement Tracker System ===\n")
        print("Player alice achievements:", alice)
        print("Player bob achievements:", bob)
        print("Player charlie achievements:", charlie)

        print("\n=== Achievement Analytics ===")

        all_achievements = alice.union(bob, charlie)
        print("All unique achievements:", all_achievements)
        print("Total unique achievements:", len(all_achievements))

        common = alice.intersection(bob, charlie)
        print("\nCommon to all players:", common)

        only_alice_have = alice.difference(bob, charlie)
        only_bob_have = bob.difference(alice, charlie)
        only_charlie_have = charlie.difference(alice, bob)
        rare = only_alice_have.union(only_bob_have, only_charlie_have)
        print("Rare achievements (1 player):", rare)

        alice_bob_common = alice.intersection(bob)
        print("\nAlice vs Bob common:", alice_bob_common)

        alice_unique = alice.difference(bob)
        print("Alice unique:", alice_unique)

        bob_unique = bob.difference(alice)
        print("Bob unique:", bob_unique)
    except Exception as e:
        print("Error : ", e)


achievement_hunter()
