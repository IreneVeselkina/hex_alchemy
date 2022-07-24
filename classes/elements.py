from enum import Enum
from typing import Dict, Tuple, List


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

    @staticmethod
    def get_elements_by_names(names: List[str]) -> List[Element]:
        """Получить элементы по именам."""
        cards = []
        for name in names:
            cards.append(Elements.get_element_by_name(name))
        return cards

    @classmethod
    def get_element_by_name(cls, name: str) -> Element:
        """
        Получить элемент по имени.

        :param name: Имя элемента
        """
        element = cls.__getattribute__(cls, name)
        if not element:
            raise ValueError(f'Не найден элемент по имени {name}')
        return element.value


def get_dict_parents_elements() -> dict:
    """Получить словарь элементов родителей."""
    parents_elements = {}
    for element in Elements:
        parents = element.value.parents
        if parents:
            parents_elements.update({tuple(parent.name for parent in parents): element})
    return parents_elements
