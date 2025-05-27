"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""
class LowFuelError(Exception):
    def __str__(self):
        return f"LowFuelError"
    
class NotEnoughFuel(Exception):
    def __str__(self):
        return f"LowFuelError"
    
class CargoOverload(Exception):
    def __str__(self):
        return f"LowFuelError"