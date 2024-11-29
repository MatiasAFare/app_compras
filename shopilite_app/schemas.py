schema_producto = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": [
            "product_name",
            "price",
            "establishment_name",
            "brand",
            "datetime",
        ],
        "properties": {
            "productId": {
                "bsonType": "int",
                "description": "Must be an integer and it's not mandatory."
            },
            "product_name": {
                "bsonType": "string",
                "description": "Must be a string and it's mandatory."
            },
            "price": {
                "bsonType": "double",
                "description": "Must be a float and it's mandatory."
            },
            "establishment_name": {
                "bsonType": "string",
                "description": "Must be an string and it's mandatory."
            },
            "brand": {
                "bsonType": "string",
                "description": "Must be an string and it's mandatory."
            },
            "datetime": {
                "bsonType": "date",
                "description": "Must be a date and it's mandatory."
            },
            "comments": {
                "bsonType": "string",
                "description": "Must be an string and it's not mandatory."
            },
            "images":{
                "bsonType": "binData",
                "description": "Must be an image binary data (e.g. jpg, png) and it's not mandatory"
            }
        },
    }
}