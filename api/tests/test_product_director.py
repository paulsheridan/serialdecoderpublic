import pytest

from product_builder.serial_number_parser import SerialNumberParser
from product_builder.product_director import ProductDirector
from product_builder.product_builder import SerializedProductBuilder
from model_proxy.model_proxy import NativeDataProxy

test_data = [
    ('RB719F1000001', {
        'product_model': 'RadRover',
        'model_year': '2019',
        'month_built': 'July',
        'year_built': '2019',
        'factory': 'FactoryF',
        'version': '1',
        'unique_id': '000001'
        }
    ),
    ('HB918V1435684', {
        'product_model': 'RadRhino',
        'model_year': '2019',
        'month_built': 'September',
        'year_built': '2018',
        'factory': 'FactoryV',
        'version': '1',
        'unique_id': '435684'
        }
    ),
    ('SA520F3123456', {
        'product_model': 'RadCity Stepthru',
        'model_year': '2018',
        'month_built': 'May',
        'year_built': '2020',
        'factory': 'FactoryF',
        'version': '3',
        'unique_id': '123456'
        }
    ),
]

class TestProductDirector:
    @pytest.mark.parametrize('serial, expected', test_data)
    def test_parsed_serial_passed_to_product_director_returns_good_product(self, serial, expected):
        parsed = {}
        serial_parser = SerialNumberParser(serial)
        for result in serial_parser:
            parsed[result[0]] = result[1]
        builder = ProductDirector(SerializedProductBuilder(NativeDataProxy))
        product = builder.create_product_from_key(parsed)
        assert product == expected
