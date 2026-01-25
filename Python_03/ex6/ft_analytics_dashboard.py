def list_comprehension_examples() -> None:

    print("=== List Comprehension Examples ===")

    lst = [["alice", 2300, 'active'],
           ['bob', 1800, 'active'],
           ['charlie', 2150, 'active'],
           ['diana', 2050, 'not active']]

    high_scorers = [data[0] for data in lst if data[1] > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    scores_doubled = [data[1] * 2 for data in lst]
    print(f"Scores doubled: {scores_doubled}")

    active_players = [data[0] for data in lst if data[2] == 'active']
    print(f"Active players: {active_players}\n")


def dict_comprehension_examples() -> None:

    print("=== Dict Comprehension Examples ===")

    dc = {'Player1': {'name': 'alice', 'score': 2300, 'achievements': 5},
          'Player2': {'name': 'bob', 'score': 1800, 'achievements': 3},
          'Player3': {'name': 'charlie', 'score': 2150, 'achievements': 7},
          'Player4': {'name': 'diana', 'score': 2050, 'achievements': 0}
          }

    score_categories = {'high': 3, 'medium': 2, 'low': 1}

    player_scores = {dc[key]['name']: dc[key]['score']
                     for key in dc if dc[key]['achievements'] > 0}

    achievement_counts = {dc[key]['name']: dc[key]['achievements']
                          for key in dc if dc[key]['achievements'] > 0}

    print(f"Player scores: {player_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {achievement_counts}\n")


def set_comprehension_examples() -> None:

    print("=== Set Comprehension Examples ===")

    unique_players = {'alice', 'bob', 'charlie', 'diana', 'diana', 'alice'}
    unique_achievements = {'first_kill', 'level_10', 'boss_slayer', 'level_10'}
    active_regions = {'north', 'east', 'central'}

    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Active regions: {active_regions}\n")


def combined_analysis() -> None:

    print("=== Combined Analysis ===")

    dc = {'Player1': {'name': 'bob', 'score': 1800, 'achievements': 3},
          'Player2': {'name': 'alice', 'score': 2300, 'achievements': 5},
          'Player4': {'name': 'charlie', 'score': 2150, 'achievements': 7},
          'Player5': {'name': 'diana', 'score': 2050, 'achievements': 0}
          }

    total_unique_achievements = 0
    unique_achievements = [dc[key]['achievements'] for key in dc]

    total_unique_achievements = sum(unique_achievements)

    average_score = 0
    total_score = 0
    all_scores = [dc[key]['score'] for key in dc]
    total_score = sum(all_scores)
    average_score = total_score / len(dc)

    sorted_keys = sorted(dc, key=lambda k: dc[k]['score'], reverse=True)

    print(f"Total players: {len(dc)}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print(f"Average score: {average_score}")

    print(f"Top performer: {dc[sorted_keys[0]]['name']}"
          f" ({dc[sorted_keys[0]]['score']} points, "
          f"{dc[sorted_keys[0]]['achievements']} achievements)")


def ft_analytics_dashboard() -> None:

    print("=== Game Analytics Dashboard ===\n")

    list_comprehension_examples()
    dict_comprehension_examples()
    set_comprehension_examples()
    combined_analysis()


ft_analytics_dashboard()
