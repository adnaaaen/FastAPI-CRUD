from pydantic import BaseModel


class Appi(BaseModel):
    name: str
    author: str | None
    department: str
    price: float | int


new = Appi(name="Data Science", author="Adnan", department="Computer Science", price=999)

new_appi = Appi(
    name="Computer Network", author="rishana", department="Computer Network", price=1999
)

# for key, value in dict(new).items():
#     print(f"{key} : {value}")

for key, value in new_appi.dict).items():
    setattr(new, key, value)
    print(f"{key} : {getattr(new, key)}")
print(f"author : {new.author}")
print(f"name : {new.name}")

