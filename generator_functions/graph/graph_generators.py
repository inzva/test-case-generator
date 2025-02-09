import random

from generator_types.graph import EdgeList


def gen_graph(
  n: int,
  m: int,
  should_be_connected: bool = True,
  shuffle_nodes: bool = True,
  max_dist: int = 10**9,
) -> EdgeList:
  """Generates a graph with `n` nodes and `m` edges.

  Args:
      n (int): The number of nodes.
      m (int): The number of edges.
      should_be_connected (bool, optional): Whether the graph should be connected. Defaults to `True`.
      shuffle_nodes (bool, optional): Whether to shuffle the nodes. Defaults to `True`.
      max_dist (int, optional): The maximum distance between two nodes of an edge. Defaults to `10**9`.

  Returns:
      The list of edges.
  """

  assert 1 <= n, "There must be at least 1 node"
  assert 0 <= m, "The number of edges must be non-negative"
  if should_be_connected:
    assert m >= n - 1, (
      "The graph must be connected, so the number of edges must be at least `n - 1`"
    )

  max_dist = min(max_dist, n - 1)

  nodes = list(range(1, n + 1))

  if shuffle_nodes:
    random.shuffle(nodes)

  edges = []

  if should_be_connected:
    for i in range(n - 1):
      u, v = nodes[i], nodes[i + 1]
      if random.randint(0, 1):
        u, v = v, u
      edges.append((u, v))

  for _ in range(len(edges), m):
    dist = random.randint(1, max_dist)
    u = random.randint(1, n - dist)
    v = u + dist
    if random.randint(0, 1):
      u, v = v, u
    edges.append((u, v))

  random.shuffle(edges)

  return edges
