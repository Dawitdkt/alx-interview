#!/usr/bin/python3
'''
some docmentation
'''


def isWinner(x, nums):
    '''
some docmentation
'''
    wins = {'Maria': 0, 'Ben': 0}
    for n in nums:
        primes = get_primes(n)
        player = 'Maria'
        while True:
            move = get_optimal_move(primes, player)
            if move is None:
                break
            primes = remove_multiples(primes, move)
            player = switch_player(player)
        winner = switch_player(player)
        wins[winner] += 1
    if wins['Maria'] > wins['Ben']:
        return 'Maria'
    elif wins['Maria'] < wins['Ben']:
        return 'Ben'
    else:
        return None


def get_primes(n):
    '''
some docmentation
'''
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(2, n + 1) if primes[i]]


def get_optimal_move(primes, player):
    '''
some docmentation
'''
    if primes == []:
        return None
    if player == 'Maria':
        # pick the smallest prime
        return primes[0]
    else:
        # pick a prime that leaves the fewest primes for Maria
        min_primes_left = len(primes) + 1
        optimal_move = None
        for p in primes:
            new_primes = remove_multiples(primes, p)
            if len(new_primes) < min_primes_left:
                min_primes_left = len(new_primes)
                optimal_move = p
        return optimal_move


def remove_multiples(primes, p):
    '''
some docmentation
'''
    return [n for n in primes if n % p != 0]


def switch_player(player):
    '''
some docmentation
'''
    return 'Ben' if player == 'Maria' else 'Maria'
