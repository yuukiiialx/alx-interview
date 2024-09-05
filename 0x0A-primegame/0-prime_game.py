def isWinner(x, nums):
    def compute_grundy_numbers(max_n):
        grundies = [0] * (max_n + 1)
        primes = []
        
        is_prime = [True] * (max_n + 1)
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, max_n + 1):
            if is_prime[i]:
                primes.append(i)
                for multiple in range(i * i, max_n + 1, i):
                    is_prime[multiple] = False
        
        for n in range(2, max_n + 1):
            reachable = set()
            for prime in primes:
                if prime > n:
                    break
                for multiple in range(prime, n + 1, prime):
                    reachable.add(grundies[n - multiple])
            mex = 0
            while mex in reachable:
                mex += 1
            grundies[n] = mex
        
        return grundies
    
    max_n = max(nums)
    grundies = compute_grundy_numbers(max_n)
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        if grundies[n] != 0:
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
