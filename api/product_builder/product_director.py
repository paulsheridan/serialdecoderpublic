class ProductDirector:
    """ The director class, and the entry point into this builder pattern
    for creating a model from a serial_key object.
    """

    def __init__(self, builder):
        self._builder = builder

    def create_product_from_key(self, serial_key):
        """ Builds a model dictionary from a serial key. Orchestrates its builder
        class to add all the individual attributes of a single product together.

        Args:
            serial_key: - A dict of decoded serial number data and associated field names

        Returns:
            A dict containing the complete data values for each code and their associated field names
        """
        self._builder.set_product_model(serial_key['product_model'])
        self._builder.set_model_year(serial_key['model_year'])
        self._builder.set_production_month(serial_key['month_built'])
        self._builder.set_production_year(serial_key['year_built'])
        self._builder.set_factory(serial_key['factory'])
        self._builder.set_version(serial_key['version'])
        self._builder.set_unique_id(serial_key['unique_id'])
        return self._builder.get_product()
