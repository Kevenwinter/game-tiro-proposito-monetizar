# Definição de classes de armas
class Weapon:
    
   
def __init__(self, name, price):
        self.name = name
        self.price = price


        self.name = name
        self.price = price

        self.name = name
        self.price

        self.name = name
        self

        self.name = name
       

        self.name = name

        self.name =

        self.name

       
# Definição de classes de skins compradas com moedas reais
class Skin:
    
   
def __init__(self, name, price):
        self.name = name
        self.price = price


        self.name = name
        self.price =

        self.name = name
        self.price

        self.name = name
        self

        self.name = name
       

        self.name = name

        self.name =

        self.name

        self
class WeaponSkin(Skin):
    
   
def __init__(self, name, price, weapon_type):
        
       
super().__init__(name, price)
        self.weapon_type = weapon_type


        self.weapon_type

        self.weapon

        self

       
class OutfitSkin(Skin):
    
   
def __init__(self, name, price, outfit_type):
        
       
super().__init__(name, price)
        self.outfit_type = outfit_type


        self.outfit_type = outfit

        self.outfit_type =

        self.outfit_type

        self.out

        self
# Definição de armas e skins
weapons = {
    
weapons = {
   

weapons = {

weapons =

weapons
"Pistol": Weapon("Pistol", 20),
    
   
"Shotgun": Weapon("Shotgun", 50),
    
   
"Rifle": Weapon("Rifle", 80)
}

weapon_skins = {
    
}

weapon_skins = {
   

}

weapon_skins =

}

weapon_skins

}

weapon_s

}

weapon

}

"Default": WeaponSkin("Default", 0, "All"),
    
   
"Camu": WeaponSkin("Camo", 5, "All"),
    "Golden": WeaponSkin("Golden", 10, "All"),
    
   
"Red Drag": WeaponSkin("Red", 15, "All"),
    
   
"Pink Panter": WeaponSkin("Pink", 20, "All"),
    
   
"Blue dolphins hare": WeaponSkin("Blue", 150, "All")
}

outfit_skins = {
    
}

outfit_skins = {
   

}

outfit_skins =

}

outfit_skins

}

outfit

}

out

}

"Default": OutfitSkin("Default", 0, "All"),
    
   
"Camouflage": OutfitSkin("Camouflage", 5, "All"),
    
   
"Tactical": OutfitSkin("Tactical", 10, "All"),
    
   
"Stealth": OutfitSkin("Stealth", 15, "All"),
    
   
"Urban": OutfitSkin("Urban", 30, "All"),
    
   
"Desert": OutfitSkin("Desert", 40, "All")
}

# Definição de moedas
class Coin:
    
   
def __init__(self, name, is_real):
        self.name = name
        self.is_real = is_real

real_coin = Coin(
        self.name = name
        self.is_real = is_real

real_coin =

        self.name = name
        self.is_real = is_real

real_coin

        self.name = name
        self.is_real = is_real


        self.name = name
        self.is_real = is_real

        self.name = name
        self.is_real =

        self.name = name
        self.is_real

        self.name = name
        self.
        self.name = name
        self

        self.name = name
       

        self.name = name

        self.name =

        self.name

        self

       
"Real Coin", True)
virtual_coin = Coin(
virtual_coin = Coin

virtual_coin

virtual
"Virtual Coin", False)

# Definição de loja
class Shop:
    
   
def __init__(self, name, items):
        self.name = name
        self.items = items

    
        self.name = name
        self.items = items

   

        self.name = name
        self.items =

        self.name = name
        self.items

        self.name = name

        self.name =

        self

       
def list_items(self):
        
       
print(f"\nWelcome to {self.name}!\n")
        
       
for item in self.items:
            
           
if isinstance(item, Weapon):
                
               
print(f"{item.name} ({item.price} virtual coins) - Weapon")
            
           
elif isinstance(item, WeaponSkin):
                
               
print(f"{item.name} ({item.price} real coins) - Weapon skin for {item.weapon_type}")
            
           
elif isinstance(item, OutfitSkin):
                
               
print(f"{item.name} ({item.price} real coins) - Outfit skin for {item.outfit_type}")
            
           
else:
                
               
print(f"{item.name} ({item.price} {item.coin.name})")

    

   


def buy_item(self, item, coins):
        
       
if item in self.items:
            
           
if coins >= item.price:
                
               
print(f"You have bought {item.name}!")
                coins -= item.price
                
                coins -= item.price
               

                coins -= item.price

                coins -= item

                coins