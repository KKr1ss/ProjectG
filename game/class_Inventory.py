class Inventory:
    money = 0

    def add_money(self, moneyToAdd):
        self.money += moneyToAdd
    
    def subtract_money(self, moneyToSubtract):
        if(self.money - moneyToSubtract < 0):
            return False
        self.money -= moneyToSubtract
        return True
    # label moneyPlus:
    #     $ Inventory.add_money(2000)
    #     "+ 2000$"
    #     jump nav_boysCollege_mcRoom 

    # label moneyMinus:
    #     if Inventory.subtract_money(1500):
    #         "-1500$"
    #     else:
    #         "Nincs péz"
    #     jump nav_boysCollege_mcRoom 

class Inventory_Item:
    id = 0
    item_name = ""
    item_image = ""