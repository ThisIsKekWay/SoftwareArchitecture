# Реализация фабрик-паттерна.


from HW2.Fabric.gem_generator import GemGenerator
from HW2.Fabric.gold_generator import GoldGenerator
from HW2.Fabric.loot_generator import LootGenerator
import random

if __name__ == "__main__":
    gem = GemGenerator()
    gold = GoldGenerator()
    loot = LootGenerator()
    gens = [gem, gold, loot]

    for i in range(1, 20):
        chest = random.choice(gens).create_item()
        chest.open()
