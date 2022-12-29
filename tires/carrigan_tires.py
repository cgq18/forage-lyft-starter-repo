from tires.tires import Tires



class CarriganTires(Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
        
    def needs_service(self):
        for tire in tire_wear:
            if tire >= 0.9:
                return true
        return false
