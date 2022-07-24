from classes.deck import Deck
from classes.player import Player
from classes.playing_field import PlayingField


class Game:
    """Игра."""

    def __init__(self, player: Player, playing_field: PlayingField, deck: Deck):
        """
        Инициирование объекта игры.

        :param player: Игрок
        :param playing_field: Игровое поле
        """
        self.player = player
        self.playing_field = playing_field
        self.deck = deck
        self.cards = deck.cards.copy()

    def move(self, index_cards: int, *coords: int):
        """
        Сделать ход.

        :param index_cards: Индекс используемой карты
        :param coords: Координаты хода
        """
        element = self.cards.pop(index_cards)
        new_elements = self.playing_field.set_cell(element, *coords)
        if new_elements:
            self.player.update_open_cards(new_elements)
            self.cards.extend(new_elements)

        if not self.cards or not self.playing_field.count_empty_cells:
            self.finish()

    def finish(self):
        """Завершить игру."""
        self.player.save_changes()
