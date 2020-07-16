from graphene import (
    ObjectType,
    String,
    List,
    Schema,
    Field,
    Mutation,
    Boolean)

from flask_jwt_extended import (
    jwt_required,
    create_access_token,
    create_refresh_token,
)
from google_auth import google_user_from_token

from product_builder.serial_number_parser import SerialNumberParser
from product_builder.product_director import ProductDirector
from product_builder.product_builder import SerializedProductBuilder
from model_proxy.model_proxy import SQLAlchemyModelProxy


class ProductCode(ObjectType):
    code = String()
    name = String()

class Product(ObjectType):
    serial = String()
    product_model = String()
    model_year = String()
    month_built = String()
    year_built = String()
    factory = String()
    version = String()
    unique_id = String()

class Query(ObjectType):
    products_from_serials = List(Product, serials=List(String))
    product_codes = List(ProductCode, table=String())

    @jwt_required
    def resolve_products_from_serials(parent, info, serials):
        """ Consumes a list of serial numbers, composes the parser, then the
        product builder, returns all products as dicts with meaningful keys and data
        """

        products = []
        for serial in serials:
            parsed = {}
            serial_parser = SerialNumberParser(serial)
            for result in serial_parser:
                parsed[result[0]] = result[1]
            builder = ProductDirector(SerializedProductBuilder(SQLAlchemyModelProxy))
            product = builder.create_product_from_key(parsed)
            product['serial'] = serial
            products.append(product)
        return products

    @jwt_required
    def resolve_product_codes(parent, info, table):
        """ Fetches all product codes from the database for display in the model admin
        page.
        """

        model_proxy = SQLAlchemyModelProxy.from_model_name(table)
        product_codes = model_proxy.read()
        return product_codes

class CreateProductCode(Mutation):
    class Arguments:
        table = String()
        name = String()
        code = String()

    product_code = Field(ProductCode)

    @jwt_required
    def mutate(root, info, table, name, code):
        """ Adds a single new model instance to the database
        """

        model_proxy = SQLAlchemyModelProxy.from_model_name(table)
        product_code = model_proxy.create(
            {
                'code': code,
                'name': name
            }
        )
        return CreateProductCode(product_code=product_code)

class Token(ObjectType):
    access_token = String()
    refresh_token = String()

class TokenAuth(Mutation):
    class Arguments:
        id_token = String(required=True)

    token = Field(Token)

    def mutate(root, info, id_token):
        """ Creates JWT token from google user data received from the front end.
        """

        token = google_user_from_token(id_token)
        access_token = create_access_token(identity=token)
        refresh_token = create_refresh_token(identity=token)
        token['access_token'] = access_token
        token['refresh_token'] = refresh_token
        return TokenAuth(token=token)

class Mutation(ObjectType):
    token_auth = TokenAuth.Field()
    create_product_code = CreateProductCode.Field()

schema = Schema(query=Query, mutation=Mutation)
