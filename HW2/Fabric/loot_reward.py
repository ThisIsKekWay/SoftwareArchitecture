import zope
import random
from i_game_item import IGameItem


class LootReward:
    zope.interface.implementer(IGameItem)
    loot = ['sword', 'shield', 'potion']

    def open(self):
        print(f'You got a {random.choice(self.loot)} from a loot chest')

