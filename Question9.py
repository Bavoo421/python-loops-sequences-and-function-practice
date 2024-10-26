def has_pair_with_sum(lst, target_sum):
    seen = set()
    for num in lst:
        if target_sum - num in seen:
            return True
        seen.add(num)
    return False

print(has_pair_with_sum([1, 2, 3, 4], 8))
