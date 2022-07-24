from enum import Enum
from typing import Dict, Tuple


class Element:
    """Элемент."""

    def __init__(self, name: str, ru_name: str, *parents):
        self.name = name
        self.ru_name = ru_name
        self.parents = sorted(parents)

    def __lt__(self, other):
        return self.name < other.name


class Elements(Enum):
    """Перечень игровых элементов."""

    water = Element('water', 'вода')
    ground = Element('ground', 'земля')
    air = Element('air', 'воздух')
    fire = Element('fire', 'огонь')

    steam = Element('steam', 'пар', fire, water)
    energy = Element('energy', 'энергия', fire, air)
    dust = Element('dust', 'пыль', ground, air)
    lava = Element('lava', 'лава', ground, fire)
    swamp = Element('swamp', 'болото', ground, water)
    alcohol = Element('alcohol', 'алкоголь', fire, air)
    stone = Element('stone', 'камень', water, lava)
    sand = Element('sand', 'песок', stone, air)
    metal = Element('metal', 'металл', stone, fire)


def get_dict_parents_elements() -> Dict[Tuple[str, str]: Element]:
    """Получить словарь элементов родителей."""
    parents_elements = {}
    for element in Elements:
        parents = element.value.parents
        if parents:
            parents_elements.update({tuple(parent.name for parent in parents): element})
    return parents_elements
