import pytest

from product_builder.product_builder import SerializedProductBuilder
from model_proxy.model_proxy import NativeDataProxy

ALL_MODELS = [
    ('R', 'RadRover'),
    ('M', 'RadMini'),
    ('W', 'RadWagon'),
    ('6', 'RadCity 16'),
    ('9', 'RadCity 19'),
    ('S', 'RadCity Stepthru'),
    ('B', 'RadBurro'),
    ('H', 'RadRhino'),
    ('C', 'Large Cargo Box'),
    ('K', 'Small Cargo Box'),
    ('P', 'Pedicab'),
    ('F', 'Flatbed'),
    ('T', 'Truckbed'),
    ('N', 'Insulated Cargo Box'),
    ('Y', 'Runner'),
]

ALL_MODEL_YEARS = [
    ('A', '2018'),
    ('B', '2019'),
    ('C', '2020'),
    ('D', '2021'),
    ('E', '2022'),
    ('F', '2023'),
    ('G', '2024'),
    ('H', '2025'),
    ('I', '2026'),
]

ALL_MONTHS_BUILT = [
    ('1', 'January'),
    ('2', 'February'),
    ('3', 'March'),
    ('4', 'April'),
    ('5', 'May'),
    ('6', 'June'),
    ('7', 'July'),
    ('8', 'August'),
    ('9', 'September'),
    ('O', 'October'),
    ('N', 'November'),
    ('D', 'December'),
]

ALL_FACTORY_CODES = [
    ('F', 'FactoryF'),
    ('V', 'FactoryV'),
]



class TestProductBuilder:
    @pytest.mark.parametrize('test_code, expected_result', ALL_MODELS)
    def test_product_builder_adds_model_name_correctly(self, test_code, expected_result):
        builder = SerializedProductBuilder(NativeDataProxy)
        builder.set_product_model(test_code)
        assert builder.product['product_model'] == expected_result

    @pytest.mark.parametrize('test_code, expected_result', ALL_MODEL_YEARS)
    def test_product_builder_adds_model_year_correctly(self, test_code, expected_result):
        builder = SerializedProductBuilder(NativeDataProxy)
        builder.set_model_year(test_code)
        assert builder.product['model_year'] == expected_result

    @pytest.mark.parametrize('test_code, expected_result', ALL_MONTHS_BUILT)
    def test_product_builder_adds_month_built_correctly(self, test_code, expected_result):
        builder = SerializedProductBuilder(NativeDataProxy)
        builder.set_production_month(test_code)
        assert builder.product['month_built'] == expected_result

    @pytest.mark.parametrize('test_code, expected_result', [('19', '2019'), ('20', '2020'), ('21', '2021'), ('22', '2022')])
    def test_product_builder_adds_production_year_correctly(self, test_code, expected_result):
        builder = SerializedProductBuilder(NativeDataProxy)
        builder.set_production_year(test_code)
        assert builder.product['year_built'] == expected_result

    @pytest.mark.parametrize('test_code, expected_result', ALL_FACTORY_CODES)
    def test_product_builder_adds_factory_correctly(self, test_code, expected_result):
        builder = SerializedProductBuilder(NativeDataProxy)
        builder.set_factory(test_code)
        assert builder.product['factory'] == expected_result

    @pytest.mark.parametrize('test_version', ['1', '2', '3', '4', '5', '6', '7'])
    def test_product_builder_sets_version_correctly(self, test_version):
        builder = SerializedProductBuilder(NativeDataProxy)
        builder.set_version(test_version)
        assert builder.product['version'] == test_version

    @pytest.mark.parametrize('test_unique_id', ['120349', '292048', '087253', '400066', '713295', '982646', '111117'])
    def test_product_builder_sets_version_correctly(self, test_unique_id):
        builder = SerializedProductBuilder(NativeDataProxy)
        builder.set_unique_id(test_unique_id)
        assert builder.product['unique_id'] == test_unique_id

    @pytest.mark.parametrize('query_models', ['product_model', 'model_year', 'month_built', 'factory'])
    @pytest.mark.parametrize('nonexistant_values', [';foewfh', 'idontexist', 'nineninenine'])
    def test_query_model_proxy_returns_unknown_if_entry_not_found(self, query_models, nonexistant_values):
        builder = SerializedProductBuilder(NativeDataProxy)
        test_result = builder._query_model_proxy(query_models, nonexistant_values)
        assert test_result == 'Unknown'
