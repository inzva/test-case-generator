from numba import njit


@njit
def is_prime(num: int) -> bool:
  assert num >= 0, "Given integer should not be negative"

  if num <= 1:
    return False

  for i in range(2, num + 1):
    if i * i > num:
      break
    if num % i == 0:
      return False

  return True


@njit
def prev_prime(n: int) -> int:
  assert n > 2, "Given integer must be strictly larger than 2"

  n -= 1
  while not is_prime(n):
    n -= 1

  return n


@njit
def next_prime(n: int) -> int:
  n += 1
  while not is_prime(n):
    n += 1

  return n
