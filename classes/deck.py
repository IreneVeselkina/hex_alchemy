from typing import List, Dict, Tuple

from classes.elements import Elements, Element


class Deck:
    """Колода."""

    def __init__(self, name: str, cards_names: List[str]):
        """
        Инициация колоды.

        :param name: Имя колоды
        :param cards_names: Список имен кард в колоде
        """
        self.name = name
        self.cards_names = cards_names
        self.cards = Elements.get_elements_by_names(cards_names)


def get_default_card_names() -> List[str]:
    """Список имен кард в колоде по умолчанию."""
    return ['water', 'ground', 'air', 'fire']


def get_default() -> Tuple[List[Element], Dict[str, Deck]]:
    """
    Получить данные по умолчанию.

    :return Список имен кард в колоде, данные о колодах
    """
    default_deck = Deck('default', get_default_card_names())
    return default_deck.cards, {'default': default_deck}
