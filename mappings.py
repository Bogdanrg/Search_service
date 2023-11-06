phones_mapping = {
    "mappings":
        {
            "properties":
                {
                    "name": {
                        "type": "text"
                    },
                    "price": {
                        "type": "double"
                    },
                    "onMarket": {
                        "type": "boolean"
                    },
                    "description": {
                        "type": "text"
                    }
                }
        }
}

food_mapping = {
    "mappings":
        {
            "properties":
                {
                    "name": {
                        "type": "text"
                    },
                    "calories": {
                        "type": "double"
                    },
                    "description": {
                        "type": "text"
                    }
                }
        }
}
