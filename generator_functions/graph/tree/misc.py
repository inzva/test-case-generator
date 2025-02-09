import random

from generator_functions.graph.tree.tree_generators import (
  gen_blossom_tree,
  gen_chain_tree,
  gen_tree,
)
from generator_types.graph import EdgeList


def gen_random_tree(n: int) -> EdgeList:
  """An exemplary random tree generator. Change the parameters however you want."""

  pick = random.random()
  if pick <= 0.2:
    return gen_chain_tree(n)
  elif pick <= 0.4:
    return gen_blossom_tree(n)
  elif pick <= 0.6:
    return gen_tree(n, 5)
  elif pick <= 0.7:
    return gen_tree(n, 10)
  elif pick <= 0.8:
    return gen_tree(n, 100)
  elif pick <= 0.9:
    return gen_tree(n, 1000)
  else:
    return gen_tree(n, n)
