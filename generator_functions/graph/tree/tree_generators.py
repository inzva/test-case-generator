import random

from generator_types.graph import EdgeList


def gen_tree(n: int, parent_dist: int = 10**9, root: int = 1) -> EdgeList:
  assert 1 <= n, "There must be at least 1 node"
  assert 0 <= parent_dist, "`parent_dist` must be positive"
  assert 1 <= root <= n, "The root's number must be within [1, n]"

  nodes = list(range(1, n + 1))
  nodes.remove(root)
  random.shuffle(nodes)
  nodes.insert(0, root)

  edges: EdgeList = []
  for node_index, node in enumerate(nodes):
    # Ignore the root
    if not node_index:
      continue
    parent_index = random.choice(range(max(0, node_index - parent_dist), node_index))
    parent = nodes[parent_index]
    u, v = node, parent
    if random.randint(0, 1):
      u, v = v, u
    edges.append((u, v))

  random.shuffle(edges)

  return edges


def gen_chain_tree(n: int, root: int = 1) -> EdgeList:
  """Generates a tree rooted at node `1`, where each non-leaf node has exactly 1 child."""

  return gen_tree(n, 1, root)


def gen_blossom_tree(n: int, root: int = 1) -> EdgeList:
  """Generates a tree rooted at node `1`, where each node except the root is a leaf node."""

  assert 1 <= n, "There must be at least 1 node"
  assert 1 <= root <= n, "The root's number must be within [1, n]"

  nodes = list(range(1, n + 1))
  nodes.remove(root)
  random.shuffle(nodes)
  edges: EdgeList = []
  for node in nodes:
    u, v = node, root
    if random.randint(0, 1):
      u, v = v, u
    edges.append((u, v))
  return edges
