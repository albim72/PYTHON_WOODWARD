from pydantic import Field
from pydantic.dataclasses import dataclass
import dataclasses
from typing import List,Optional

#dekorator pochodzący z biblioteki pydantic
@dataclass
class User:
    id:int
    name:str = "Jan Kowalski"
    friends:List[int]=dataclasses.field(default_factory=lambda : [0])
    age:Optional[int]=dataclasses.field(default=None,metadata=dict(title="wiek użytkownika",description="nie kłam!"))
    height:Optional[int] = Field(None,title="wzrost w cm",ge=50,le=270)

user = User(id='33')
print(user)
usr1 = User(55,"Olga Kot",[2,],56,177)
print(usr1)

usr2 = User(7,"Leon Nowik",[12,],37,270)
print(usr2)

l1 = (45,)
print(type(l1))
