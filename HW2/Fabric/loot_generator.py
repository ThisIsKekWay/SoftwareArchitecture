from item_fabric import ItemFabric
from loot_reward import LootReward


class LootGenerator(ItemFabric):
    def create_item(self):
        return LootReward()
