import random

from generator_types.graph import EdgeList, WeightedEdgeList


def make_graph_weighted(
  edges: EdgeList, lower_bound: int, upper_bound: int
) -> WeightedEdgeList:
  """Makes the graph weighted by assigning random weights to the edges."""

  return [(u, v, random.randint(lower_bound, upper_bound)) for u, v in edges]
