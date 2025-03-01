
CUSTOMER_SCHEMA = [
    {
        "name": "customer_id",
        "type": "int",
        "required": True
    },
    {
        "name": "first_name",
        "type": "string",
        "required": True
    },
    {
        "name": "last_name",
        "type": "string",
        "required": True
    },
    {
        "name": "gender",
        "type": "enum",
        "values": ["M", "F", "U"],
        "required": True
    },
    {
        "name": "email",
        "type": "string",
        "required": True
    },
    {
        "name": "membership_status",
        "type": "enum",
        "values": ["active", "inactive"],
        "required": True
    },
    {
        "name": "address",
        "type": "string",
    },
    {
        "name": "phone_number",
        "type": "string",
        "required": False
    },
    {
        "name": "date_of_birth",
        "type": "date",
        "format": "%Y-%m-%d",
        "required": True
    },
    {
        "name": "job",
        "type": "string",
    },
    {
        "name": "company",
        "type": "string",
    },
    {
        "name": "city",
        "type": "string",
    },
    {
        "name": "state",
        "type": "string",
    },
    {
        "name": "country",
        "type": "string",
    },
    {
        "name": "language",
        "type": "enum",
        "values": ["en-US", "es-ES", "fr-FR"],
        "required": True
    }
]

SALES_SCHEMA = [
    {
        'name': 'sale_id',
        'type': 'int',
        'required': True
    },
    {
        "name": "customer_id",
        "type": "int",
        "required": True
    },
    {
        "name": "product_id",
        "type": "string",
        "required": True
    },
    {
        "name": "quantity",
        "type": "int",
        "required": True
    },
    {
        "name": "price_per_unit",
        "type": "float",
        "required": True
    },
    {
        "name": "total_price",
        "type": "float",
        "required": True
    },
    {
        "name": "sale_date",
        "type": "date",
        "format": "%Y-%m-%d",
        "required": True
    }
]

PRODUCT_SCHEMA = [
    {
        "name": "name",
        "type": "string",
        "required": True
    },
    {
        "name": "product_id",
        "type": "string",
        "required": True
    },
    {
        "name": "price",
        "type": "float",
        "required": True
    },
    {
        "name": "description",
        "type": "string",
    },
    {
        "name": "creation_date",
        "type": "date",
        "format": "%Y-%m-%d",
        "required": True
    }
]

SCHEMAS = {
    "customer": CUSTOMER_SCHEMA,
    "sales": SALES_SCHEMA,
    "product": PRODUCT_SCHEMA
}
