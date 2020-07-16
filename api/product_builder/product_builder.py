import abc

from model_proxy.errors import ResourceNotFoundError


class ProductBuilder(abc.ABC):

    """
    The Decoder interface specifies the methods necessary to decode
    the individual codes that make up one Serial Number.
    """

    @abc.abstractmethod
    def set_product_model(self, model):
        pass

    @abc.abstractmethod
    def set_model_year(self, model_year):
        pass

    @abc.abstractmethod
    def set_production_month(self, month_built):
        pass

    @abc.abstractmethod
    def set_production_year(self, year_built):
        pass

    @abc.abstractmethod
    def set_factory(self, factory):
        pass

    @abc.abstractmethod
    def set_version(self, version):
        pass

    @abc.abstractmethod
    def set_unique_id(self, unique_id):
        pass


class SerializedProductBuilder(ProductBuilder):
    """ A concrete implementation of the builder class, it
    contains all the necessary functionality to decode the
    individual product attributes and returns a dict comprised
    of field names and associated codes
    """

    def __init__(self, db_proxy_class):
        self.product = {}
        self.db_proxy_class = db_proxy_class

    def _query_model_proxy(self, database_model_name, code):
        try:
            model_proxy = self.db_proxy_class.from_model_name(database_model_name)

            queried = model_proxy.read(code)
            return queried.name
        except ResourceNotFoundError:
            return 'Unknown'

    def set_product_model(self, model):
        model_name = self._query_model_proxy('product_model', model)
        self.product['product_model'] = model_name

    def set_model_year(self, model_year):
        model_year = self._query_model_proxy('model_year', model_year)
        self.product['model_year'] = model_year

    def set_production_month(self, month_built):
        month_built = self._query_model_proxy('month_built', month_built)
        self.product['month_built'] = month_built

    def set_production_year(self, year_built):
        self.product['year_built'] = '20' + year_built

    def set_factory(self, factory):
        factory = self._query_model_proxy('factory', factory)
        self.product['factory'] = factory

    def set_version(self, version):
        self.product['version'] = version

    def set_unique_id(self, unique_id):
        self.product['unique_id'] = unique_id

    def get_product(self):
        return self.product
