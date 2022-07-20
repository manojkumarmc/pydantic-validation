from typing_extensions import TypedDict
from pydantic import validate_arguments, ValidationError, StrictInt, BaseModel, StrictStr, HttpUrl, stricturl
from pprint import pprint as pp

class Constants(TypedDict):
    name: str
    age: int


class CDict(BaseModel):
    c: Constants

ca = CDict(c={'name':'Manoj', 'age': 10})

print(ca)
print(ca.c['name'])


@validate_arguments
def sample(a: StrictInt, b: int)  -> int:
    return a + b

try:
    print(sample(1.9,2))
except ValidationError as ve:
    print(ve)

@validate_arguments
def repeat(s: str, count: int, *, separator: bytes = b'') -> bytes:
    b = s.encode()
    return separator.join(b for _ in range(count))


a = repeat('hello', 3.0)
print(a)
#> b'hellohellohello'

b = repeat('x', '4', separator=' ')
print(b)
#> b'x x x x'

#try:
#    c = repeat('hello', 'wrong')
#except ValidationError as exc:
#    print(exc)

# This will not work
#class DType(TypedDict, BaseModel):
#    name: StrictStr
#    age: StrictInt
#
#
#dt = DType(name="Hellp", age=10)
#print(dt)


class UrlManager(BaseModel):
    url: HttpUrl


u = UrlManager(url="httpx://ww.google.co.in")
pp(u)
