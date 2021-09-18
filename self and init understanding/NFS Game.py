class Car(object):
    """
    blueprint for car
  """

    def __init__(self, model, color, company, speed_limit):
        self.color = color
        self.company = company
        self.speed_limit = speed_limit
        self.model = model

    @staticmethod
    def start():
        print("started")

    @staticmethod
    def stop(self):
        print("stopped")

    @staticmethod
    def accelerate(self):
        print("accelerating...")
        "accelerator functionality here"

    @staticmethod
    def change_gear(self, gear_type):
        print("gear changed")
        " gear related functionality here"


suzuki = Car("erotica", "black", "suzuki", 60)
audi = Car("A6", "red", "audi", 80)



