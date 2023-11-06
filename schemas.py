from pydantic import BaseModel


class PhoneModel(BaseModel):
    name: str
    price: float
    onMarket: bool
    description: str

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Samsung",
                "price": 2000.5,
                "onMarket": "true",
                "description": "Vaflya"
            }
        }


class FoodModel(BaseModel):
    name: str
    calories: float
    description: str
