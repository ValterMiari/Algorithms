from functools import wraps


def trace(func):

    # cache func name, which will be used for trace print
    func_name = func.__name__
    # define the separator, which will indicate current recursion level (repeated N times)
    separator = '|  '

    # current recursion depth
    trace.recursion_depth = 0

    @wraps(func)
    def traced_func(*args, **kwargs):

        # repeat separator N times (where N is recursion depth)
        # `map(str, args)` prepares the iterable with str representation of positional arguments
        # `", ".join(map(str, args))` will generate comma-separated list of positional arguments
        # `"x"*5` will print `"xxxxx"` - so we can use multiplication operator to repeat separator
        print(f'{separator * trace.recursion_depth}|-- {func_name}({", ".join(map(str, args))})')
        # we're diving in
        trace.recursion_depth += 1
        result = func(*args, **kwargs)
        # going out of that level of recursion
        trace.recursion_depth -= 1
        # result is printed on the next level
        print(f'{separator * (trace.recursion_depth + 1)}|-- return {result}')

        return result

    return traced_func

def opt(values):
    i = len(values)
    if i <= 0:
        return 0
    elif i == 1:
        return values[0]
    else:
        return max(opt(values[:i-1]), opt(values[:i-2]) + values[i-1])

def optimal_opt(values):
    # results store all subcomputations (memoization)
    # initial value of result is zero at index 0
    results = {0:0}
    for i in range(len(values)):
        if i == 0:
            results.update({i+1:values[i]})
        else:
            results.update({i+1:max(results.get(i), results.get(i-1) + values[i])})
    return results

days1 = range(1, 6)
v1 = [1,10,1,1,10,1]
v2 = [1, 20, 20]
v3 = [1, 2, 1, 3, 1, 4, 32, 100, 100, 1]
opt = trace(opt)
#print(values[:5])
#print(opt(v1))
steps = optimal_opt(v1)
print(steps)

