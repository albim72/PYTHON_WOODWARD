def state_manager(cls):
    class Wrapped(cls):
        def __init__(self,*args,**kwargs):
            self._state = "inactive" #stan początkowy
            super().__init__(*args,**kwargs)

        def activate(self):
            self._state = "active"

        def deactivate(self):
            self._state = "inactive"

        def get_state(self):
            return self._state

        def __getattribute__(self, name):
            value = super().__getattribute__(name)
            if name == 'run_fast' and self._state == "inactive":
                raise ValueError("Obiekt jest nieaktywny!")
            return value
    return Wrapped


@state_manager
class User:
    def __init__(self,name):
        self.name = name

    def run_fast(self):
        print(f"{self.name} biegnie bardzo szybko!!!")


#testujemy
user = User("Leokadia")
print(user.get_state())

user.activate()
print(user.get_state())

#sprawdzenie stanu
try:
    user.deactivate()
    user.run_fast()
    print(user.get_state())
except ValueError as e:
    print(e)
    
    
try:
    user.activate()
    user.run_fast()
    print(user.get_state())
except ValueError as e:
    print(e)
