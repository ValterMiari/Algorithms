
def opt_split(prices):
    prices.sort(reverse=True)
    opt = [tuple(prices[x:x+3]) for x in range(0, len(prices), 3)]
    return opt

def comparison(prices):
    tot = sum(prices)
    partition = opt_split(prices)
    opt_sol = skip_third(prices)
    output = f"Sum: {tot}\nOptimal solution: {opt_sol}\nParition: {partition}\nInput: {prices}"
    return output

def calc_partition(partition):
    tot = 0
    for i in range(len(partition)):
        for j in range(0, 1):
            tot += partition[i].index(j)
    return tot

def skip_third(arr):
    tot = 0
    for i in range(len(arr)):
       if ((i+1) % 3 != 0): 
            tot += arr[i]
    return tot

p = [10, 30, 399, 9090, 89348, 90, 218, 89, 8932, 8933, 93, 89322, 89343, 8992, 899, 2888]
test = [1,2,3,4,5,6,7,8,9,10,11,12]
p1 = []
print(comparison(test))

