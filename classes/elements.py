from enum import Enum
from typing import Dict, Tuple


class Element:
    """Элемент."""

    def __init__(self, name: str, *parents):
        self.name = name
        self.parents = sorted(parents)

    def __lt__(self, other):
        return self.name < other.name


class Elements(Enum):
    """Перечень игровых элементов."""

    water = Element('water')
    ground = Element('ground')
    air = Element('air')
    fire = Element('fire')

    steam = Element('steam', fire, water)


def get_dict_parents_elements() -> Dict[Tuple[str, str]: Element]:
    """Получить словарь элементов родителей."""
    parents_elements = {}
    for element in Elements:
        parents = element.value.parents
        if parents:
            parents_elements.update({tuple(parent.name for parent in parents): element})
    return parents_elements
