def numbers_with_max_number_of_divisors(limit: int) -> list[int]:
  """Given an upper bound `limit`, finds all positive integers not exceeding `limit` and having the maximum number of divisors."""

  assert 1 <= limit <= 10**12, (
    "`limit` must be within [1, 10**12], or else, update the primes list below accordingly."
  )

  # List of smallest primes (numbers to be found won't be divisible by a greater prime).
  p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

  # Keeps the record of the maximum number of divisors found so far.
  max_number_of_divisors = 0

  # The numbers to be found will be stored in this.
  target_numbers: list[int] = []

  # The recursive function for finding the numbers. This does all the work.
  def helper(num: int, p_i: int, cnt: int) -> None:
    nonlocal target_numbers, max_number_of_divisors, limit
    if cnt > max_number_of_divisors:
      max_number_of_divisors = cnt
      target_numbers = [num]
    elif cnt == max_number_of_divisors:
      target_numbers.append(num)
    if p_i == len(p):
      return
    pw = 1
    while num * p[p_i] ** pw <= limit:
      helper(num * p[p_i] ** pw, p_i + 1, cnt * (pw + 1))
      pw += 1

  helper(1, 0, 1)

  return target_numbers
