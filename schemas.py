from pydantic import BaseModel


class PhoneModel(BaseModel):
    id: str
    name: str
    price: float
    onMarket: bool
    description: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": "1",
                "name": "Samsung",
                "price": 2000.5,
                "onMarket": "true",
                "description": "Vaflya"
            }
        }


class FoodModel(BaseModel):
    id: str
    name: str
    calories: float
    description: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": "1",
                "name": "Soup",
                "calories": 200.5,
                "description": "Yummy"
            }
        }
