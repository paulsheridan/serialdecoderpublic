import pytest

from model_proxy.model_proxy import NativeDataProxy, SQLAlchemyModelProxy
from model_proxy.errors import ResourceNotFoundError, TableNotFoundError
from model_proxy.lookup_tables import (
    product_model,
    model_year,
    month_built,
    factory,
)

class TestModelProxy:
    def test_native_data_proxy_reads_from_lookup_tables(self):
        model_proxy = NativeDataProxy.from_model_name('product_model')
        value = model_proxy.read('R')
        assert value == 'RadRover'

    @pytest.mark.parametrize('table_name, table', [('product_model', product_model), ('model_year', model_year), ('month_built', month_built), ('factory', factory)])
    def test_native_data_proxy_inits_with_correct_dict_type_lookup_table(self, table_name, table):
        model_proxy = NativeDataProxy.from_model_name(table_name)
        assert isinstance(model_proxy.lookup_table, dict)
        assert model_proxy.lookup_table == table

    def test_native_data_proxy_raises_tablenotfound_bad_table_name(self):
        with pytest.raises(TableNotFoundError):
            NativeDataProxy.from_model_name('bad_name')

    def test_native_data_raises_resourcenotfounderror_with_bad_key(self):
        model_proxy = NativeDataProxy.from_model_name('product_model')
        with pytest.raises(ResourceNotFoundError):
            model_proxy.read('X')
