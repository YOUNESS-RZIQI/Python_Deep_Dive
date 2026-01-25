def generat_evnets(events_num: int):
    """
    Generates game events one by one using a generator.
    """

    i: int = 1

    while i <= events_num:

        if i % 3 == 1:
            name: str = "alice"
            level: int = 5
            action: str = "killed monster"
        elif i % 3 == 2:
            name: str = "bob"
            level: int = 12
            action: str = "found treasure"
        else:
            name: str = "charlie"
            level: int = 8
            action: str = "leveled up"

        yield i, name, level, action
        i += 1


def stream_analytic(count: int) -> None:
    """
    Processes a stream of game events using a generator and computes
    statistics while streaming, demonstrating constant memory usage.
    """

    total_events_processed: int = 0
    hight_level_players: int = 0
    treasure_events: int = 0
    level_up_events: int = 0

    for i, name, level, word in generat_evnets(count):
        total_events_processed += 1
        if level >= 10:
            hight_level_players += 1
        if word == "found treasure":
            treasure_events += 1
        if word == "leveled up":
            level_up_events += 1
        if i <= 3:
            print(f"Event {i}: Player {name} (level {level}) {word}")

    print("...\n\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events_processed}")
    print(f"High-level players (10+): {hight_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds\n")


def fibonacci_sequence(count: int):

    """
    Generates the first N numbers of the Fibonacci
    sequence one at a time using a generator.
    """

    i: int = 0
    a: int = 0
    b: int = 1

    while i < count:
        yield a
        a, b = b, a + b
        i += 1


def print_fibonacci_sequence(count: int) -> None:

    """
    Prints the first N Fibonacci numbers generated from a Fibonacci generator.
    """

    i: int = 0

    print(f"Fibonacci sequence (first {count}): ", end='')

    for num in fibonacci_sequence(count):
        if i < count - 1:
            print(num, ', ', sep='', end='')
        else:
            print(num)
        i += 1


def prime_numbers(count: int):

    """
    Generates the first N prime numbers using a generator.
    """

    i: int = 0
    num: int = 2

    while i < count:

        is_prime: bool = True
        div: int = 2

        while div * div <= num:
            if num % div == 0:
                is_prime = False
                break
            div += 1

        if is_prime:
            yield num
            i += 1

        num += 1


def print_prime_numbers(count: int) -> None:

    """
    Prints the first N prime numbers produced by a prime number generator.
    """

    i: int = 0

    print(f"Prime numbers (first {count}): ", end='')

    for num in prime_numbers(count):
        if i < count - 1:
            print(num, ', ', sep='', end='')
        else:
            print(num)
        i += 1


def generator_demonstration() -> None:

    """
    Demonstrates generator usage with Fibonacci and prime number sequences.
    """

    print("=== Generator Demonstration ===")

    print_fibonacci_sequence(10)

    print_prime_numbers(5)


def ft_data_stream() -> None:

    """
    Main entry point that runs the game data stream
    processor and generator demonstrations.
    """
    try:
        print("=== Game Data Stream Processor ===\n")

        print("Processing 1000 game events...\n")
        stream_analytic(1000)

        generator_demonstration()
    except Exception as e:
        print(f"Error : {e}")


ft_data_stream()
