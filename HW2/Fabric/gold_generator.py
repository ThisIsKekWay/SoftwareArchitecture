from item_fabric import ItemFabric
from gold_reward import GoldItem


class GoldGenerator(ItemFabric):
    def create_item(self):
        return GoldItem()
