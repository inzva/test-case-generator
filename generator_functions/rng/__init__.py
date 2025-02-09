import random


def randints(
  n: int, lower_bound: int, upper_bound: int, allow_repetition: bool = True
) -> list[int]:
  assert 0 <= n, "The number of integers to generate must be non-negative"
  assert lower_bound <= upper_bound, "Lower bound must not be greater than upper bound"

  if allow_repetition:
    assert upper_bound - lower_bound + 1 >= n, (
      "Unable to generate with allow_repetition=True, the range is smaller than the number of integers to generate"
    )

  return (random.choices if allow_repetition else random.sample)(
    range(lower_bound, upper_bound + 1), k=n
  )


def randints_with_target_sum(n: int, target_sum: int, lower_bound: int) -> list[int]:
  """Generate n integers with the sum of target_sum, where each integer is at least lower_bound."""

  assert 0 <= n, "The number of integers to generate must be non-negative"
  assert n * lower_bound <= target_sum, (
    "Unable to generate, the minimum possible sum is greater than the target sum"
  )

  # Generated numbers will be in the form of lower_bound + x_i, where 0 <= x_i.
  # Generate x_i's, then add lower_bound to all.
  # sum(x_i) == target_sum - n * lower_bound (normalized sum)
  normalized_sum = target_sum - n * lower_bound
  prefix_sums = [0] + sorted(randints(n - 1, 0, normalized_sum)) + [normalized_sum]
  ints = [prefix_sums[i + 1] - prefix_sums[i] + lower_bound for i in range(n)]

  assert sum(ints) == target_sum

  return ints
