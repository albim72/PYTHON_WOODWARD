class DynamicBehavior:
    def __init__(self):
        self.state = "initial"

    def change_behavior(self):
        #zmiana zachowania obiektu na podstawie zmiany stanu
        if self.state == "initial":
            self.state = "changed"
            self.execute = self.changed_behavior
        elif self.state == "changed":
            self.state = "final"
            self.execute = self.changed_behavior
        else:
            print("Obiekt zakończył działanie!")

    def initial_behavior(self):
        return "Zachowanie początkowe"

    def final_behavior(self):
        return "Zachowanie końcowe"

    def changed_behavior(self):
        return "Zachowanie zmienione"

    def execute(self):
        return self.initial_behavior()

obj = DynamicBehavior()
print(obj.execute())

obj.change_behavior()
print(obj.execute())

obj.change_behavior()
print(obj.execute())

obj.change_behavior()
