import zope

from i_game_item import IGameItem


class GemReward:
    zope.interface.implementer(IGameItem)

    def open(self):
        print("Open a gem chest")
