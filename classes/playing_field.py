from typing import List, Tuple

from classes.elements import Element, get_dict_parents_elements


class Cell:
    """Ячейка игрового поля."""

    def __init__(self, s: int, q: int, r: int):
        self.s, self.q, self.r = s, q, r
        self.filling = False
        self.element = None

    def set_element(self, element: Element):
        """Установить элемент для ячейки."""
        if not self.filling:
            self.filling = True
            self.element = element
        else:
            raise ValueError('Игровая ячейка уже заполнена!')


class PlayingField:
    """Игровое поле."""

    # Координаты соседних клеток
    _NEIGHBOUR_COORDS = [
        (1, 0, -1),
        (1, -1, 0),
        (0, -1, 1),
        (-1, 0, 1),
        (-1, 1, 0),
        (0, 1, -1)
    ]

    def __init__(self, size: int):
        self.size = size
        self.cells = {}
        self._generate_cells()
        self.parents_elements = get_dict_parents_elements()
        self.count_empty_cells = len(self.cells)

    def _generate_cells(self):
        """Сгенерировать поле."""
        for s in range(-self.size, self.size + 1):
            for q in range(-self.size, self.size + 1):
                for r in range(-self.size, self.size + 1):
                    if q + r + s == 0:
                        self.cells.update({(s, q, r): Cell(s, q, r)})

    def get_cell(self, *coords: int) -> Cell:
        """Получить ячейку поля по координатам."""
        return self.cells[coords]

    def set_cell(self, element: Element, *coords: int) -> List[Element]:
        """
        Установить элемент ячейке поля.

        :param element: Элемент
        :param coords: Координаты
        :return: Новые элементы, полученные в результате комбинаций с соседними ячейками
        """
        cell = self.get_cell(*coords)
        cell.set_element(element)
        self.count_empty_cells -= 1
        return self.give_new_elements(cell)

    def give_new_elements(self, cell: Cell) -> List[Element]:
        """
        Получить новые элементы по соседним ячейкам.

        :param cell: Новая ячейка
        """
        new_elements = []
        for s, q, r in self._NEIGHBOUR_COORDS:
            # ToDO добавить проверку на конец поля
            element = self.get_element(cell, self.get_cell(cell.s + s, cell.q + q, cell.r + r))
            if element:
                new_elements.append(element)
        return new_elements

    def get_element(self, cell: Cell, cell_neighbour: Cell) -> Element | None:
        """
        Получить элемент в результате комбинации 2х ячеек, если он есть.

        :param cell: Новая ячейка.
        :param cell_neighbour: Ячейка сосед
        """
        if cell_neighbour.filling:
            return self.parents_elements.get(tuple(sorted([cell_neighbour.element, cell.element])))
        return None
