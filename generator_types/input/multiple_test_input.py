from dataclasses import dataclass

from generator_types.input.input import Input


@dataclass
class MultipleTestInput:
  t: int
  inputs: list[Input]
