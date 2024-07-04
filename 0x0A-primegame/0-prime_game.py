#!/usr/bin/python3
"""
This module contains a function to determine the winner
of a prime game session.

The prime game is played with `x` rounds and a list of numbers `nums`.
In each round, a number `n` is selected from `nums`.
The goal is to determine if the number of prime numbers
less than or equal to `n` is even or odd. If it's even, Ben wins the round.
If it's odd, Maria wins the round.
The player with the most wins at the end of `x` rounds
is declared the overall winner.

The function `isWinner(x, nums)` takes in the number of rounds `x`
and the list of numbers `nums`
and returns the name of the winner (either 'Maria' or 'Ben')
or None if there is no winner.

Example usage:
    x = 3
    nums = [1, 2, 3]
    winner = isWinner(x, nums)
    print(winner)  # Output: 'Maria'
"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.

    Args:
        x (int): The number of rounds in the prime game.
        nums (list): A list of numbers to be used in each round.

    Returns:
        str or None: The name of the winner ('Maria' or 'Ben')
        or None if there is no winner.

    """
    if x < 1 or not nums:
        return None
    marias_wins, bens_wins = 0, 0
    # generate primes with a limit of the maximum number in nums
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    # filter the number of primes less than n in nums for each round
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
