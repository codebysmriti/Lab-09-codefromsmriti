# Problem-solving practice (LeetCode / ICPC style).


def two_sum(nums, target):
    # Outline:
    #   Find two numbers that add up to the target.
    #   Example: nums = [3, 2, 4], target = 6.
    #   The numbers 2 and 4 add up to 6, at indices [1, 2].
    #   Use a dictionary to remember numbers already visited.
    #   Calculate the needed number for each element.
    #   If the needed number exists, return both indices.

    seen = {}

    for i, num in enumerate(nums):
        needed = target - num

        if needed in seen:
            return [seen[needed], i]

        seen[num] = i


def max_profit(prices):
    # Outline:
    #   Find the maximum profit by buying first and selling later.
    #   If the list is empty, return 0.
    #   Track the lowest price seen so far.
    #   Calculate possible profit for each price.
    #   Keep track of the highest profit.

    if not prices:
        return 0

    lowest = prices[0]
    best_profit = 0

    for price in prices:
        if price < lowest:
            lowest = price

        profit = price - lowest

        if profit > best_profit:
            best_profit = profit

    return best_profit


def max_subarray(nums):
    # Outline:
    #   Find the largest sum of any continuous group of numbers.
    #   Example: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4].
    #   The best group is [4, -1, 2, 1], with a sum of 6.
    #   Track the current subarray sum and largest sum.
    #   Decide whether to add the next number or start a new group.
    #   Update the largest sum whenever a bigger sum is found.

    current_sum = nums[0]
    best_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        best_sum = max(best_sum, current_sum)

    return best_sum


def is_balanced(s):
    # Outline:
    #   Check whether all brackets are correctly matched.
    #   Example: "{[]}" is balanced because brackets close
    #   in the correct order.
    #   Use a list as a stack to remember opening brackets.
    #   Push opening brackets onto the stack.
    #   Check each closing bracket against the last opening bracket.
    #   Return False if they do not match.
    #   Return True if the stack is empty at the end.

    stack = []

    matching = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in s:
        if char in "([{":
            stack.append(char)

        elif char in ")]}":
            if not stack:
                return False

            if stack.pop() != matching[char]:
                return False

    return len(stack) == 0


def main():
    # Test two_sum
    print(two_sum([2, 7, 11, 15], 9))
    print(two_sum([3, 2, 4], 6))

    # Test max_profit
    print(max_profit([7, 1, 5, 3, 6, 4]))
    print(max_profit([7, 6, 4, 3, 1]))
    print(max_profit([]))

    # Test max_subarray
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(max_subarray([5, 4, -1, 7, 8]))

    # Test is_balanced
    print(is_balanced("()[]{}"))
    print(is_balanced("{[]}"))
    print(is_balanced("([)]"))


if __name__ == "__main__":
    main()