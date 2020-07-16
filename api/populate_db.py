from model_proxy.lookup_tables import (
    product_model,
    model_year,
    month_built,
    factory,
)
from model_proxy.model_proxy import SQLAlchemyModelProxy


def populate_from_tables():
    tables = {
        'product_model': product_model,
        'model_year': model_year,
        'month_built': month_built,
        'factory': factory,
    }

    for key, value in tables.items():
        model_proxy = SQLAlchemyModelProxy.from_model_name(key)
        for table_key, table_value in value.items():
            try:
                model_proxy.create(
                    {
                        'code': table_key,
                        'name': table_value
                    }
                )
            except ValueError:
                pass
