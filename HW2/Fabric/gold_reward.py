import zope.interface

from i_game_item import IGameItem


class GoldItem:
    zope.interface.implementer(IGameItem)

    def open(self):
        print("Open a gold chest")
