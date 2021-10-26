from datetime import date, datetime
from decimal import Decimal


def serialize_json(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    elif isinstance(obj, Decimal):
        return int(obj)

    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")
