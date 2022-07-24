import json
from uuid import uuid4
from typing import Optional, List

from classes.elements import Elements, Element
from classes.deck import Deck, get_default, get_default_card_names


class Player:
    """Игрок."""

    def __init__(self, uuid: Optional[uuid4] = None):
        self.uuid = uuid or str(uuid4())
        self._load_info_player()

    def _load_info_player(self):
        """Загрузить информацию о пользователе."""
        with open('players.json', 'r') as players_file:
            users_info = json.load(players_file)

        user_info = users_info.get(self.uuid)
        if user_info:
            self.lvl = user_info.get('lvl', 0)

            self.open_cards = []
            for open_card in user_info.get('open_cards', get_default_card_names):
                self.open_cards.append(Elements.get_element_by_name(open_card))

            self.card_decks = {}
            for name, elements in user_info.get('card_decks', {}).items():
                self.card_decks.update({name: Deck(name, elements)})
        else:
            self.lvl = 0
            self.open_cards, self.card_decks = get_default()

    def add_deck(self, deck: Deck):
        """Добавить колоду."""
        self.card_decks.update({deck.name: deck})

    def get_deck(self, name: str) -> Deck:
        """
        Получить колоду.

        :param name: Имя колоды
        """
        deck = self.card_decks.get(name)
        if not deck:
            raise ValueError(f'Не найдена колода {name}')
        return deck

    def update_open_cards(self, new_elements: List[Element]):
        """
        Обновить список открытых кард.

        :param new_elements: Список новых элементов
        """
        new_elements_names = {element.name for element in new_elements}
        open_cards_names = {element.name for element in self.open_cards}

        new_open_cards_names = new_elements_names - open_cards_names
        if new_open_cards_names:
            for new_open_card_name in new_open_cards_names:
                self.open_cards.append(Elements.get_element_by_name(new_open_card_name))

    def save_changes(self):
        """Сохранить изменения."""
        with open('players.json', 'r') as players_file:
            users_info = json.load(players_file)
            users_info.update({
                self.uuid: {
                    'lvl': self.lvl,
                    'open_cards': [element.name for element in self.open_cards],
                    'card_decks': {name: deck.cards_names for name, deck in self.card_decks.items()}
                }
            })
        with open('players.json', 'w') as players_file:
            json.dump(users_info, players_file)
