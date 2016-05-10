__author__ = 'zhengyiwang'
def coinChange( coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    dp = [0 for i in range(amount + 1)]
    for i in range(1,amount + 1):
        mini = 9999999999
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] > -1:
                mini = min(mini, dp[i - coin])
        if mini == 9999999999:
            mini = -1
        else:
            mini += 1
        dp[i] = mini

    return dp[amount]



print coinChange([370,417,408,156,143,434,168,83,177,280,117],9953)
