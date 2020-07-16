"""
The Model Proxy abstracts the act of querying database lookup tables for serial
code information. This maintains proper dependency inversion, but also allows me
to use anything I want in place of the database, including simple in-memory models
for testing and prototyping. The proxy is very simple, since most of its functionaltiy
will be reading.
"""

import abc
from importlib import import_module
from psycopg2.errors import UniqueViolation

from models import db
from model_proxy.errors import ResourceNotFoundError, TableNotFoundError

class ModelProxy(abc.ABC):

    @abc.abstractmethod
    def create(self, data):
        pass

    @abc.abstractmethod
    def delete(self, model_id):
        pass

    @abc.abstractmethod
    def update(self, model_id, new_data):
        pass

    @abc.abstractmethod
    def read(self, serial_code):
        pass

    @abc.abstractclassmethod
    def from_model_name(cls, model_name):
        pass


class NativeDataProxy(ModelProxy):
    """ A concrete implementation of the ModelProxy API that wraps a dictionary for
        any application model"""

    def __init__(self, lookup_table):
        self.lookup_table = lookup_table

    def read(self, serial_code):
        """ Returns a string for an individual product attribute, such as model, month produced, etc.

        Args:
            serial_code: - The serial code of the field name to retrieve.

        Returns:
            A string meaningful string of the serial code given.
        """
        try:
            return self.lookup_table[serial_code]
        except KeyError:
            raise ResourceNotFoundError

    def create(self, data):
        return NotImplementedError

    def delete(self, model_id):
        return NotImplementedError

    def update(self, model_id, new_data):
        return NotImplementedError

    @classmethod
    def from_model_name(cls, model_name):
        """ An abstract factory that provides an instance of any of
        the lookup table dictionaries consuming a string
        version of the model class name
        """

        try:
            model_module = import_module('model_proxy.lookup_tables')
            lookup_table = getattr(model_module, model_name)

        except (IndexError, AttributeError):
            raise TableNotFoundError(
                '{} not found!'.format('model_proxy.lookup_tables.' + model_name))

        return cls(lookup_table)

class SQLAlchemyModelProxy(ModelProxy):
    def __init__(self, sqlalchemy_model):
        self.sqlalchemy_model = sqlalchemy_model

    def read(self, serial_code=None):
        """ Returns a string for an individual product attribute, such as model, month produced, etc.

        Args:
            serial_code: - The serial code of the field name to retrieve.

        Returns:
            A string meaningful string of the serial code given.
        """
        if serial_code is None:
            return self.sqlalchemy_model.query.all()
        value = self.sqlalchemy_model.query.filter_by(code=serial_code).first()
        if not value:
            raise ResourceNotFoundError
        return value

    def create(self, data):
        """ Creates an individual product attribute, such as model, month produced, etc in the database.

        Args:
            data: - The dict containing code and name variables to add

        Returns:
            The model instance added.
        """
        try:
            instance = self.sqlalchemy_model(**data)
            db.session.add(instance)
            db.session.commit()
            return instance
        except UniqueViolation:
            raise ValueError('That entry already exists in the database.')

    def delete(self, model_id):
        return NotImplementedError

    def update(self, model_id, new_data):
        return NotImplementedError

    @classmethod
    def from_model_name(cls, model_name):
        """An abstract factory that provides a SQLAlchemy model instance
         consuming a string version of the model class name
        """

        try:
            model_module = import_module('models')
            model_class_name = model_name.replace(
                '_', ' ').title().replace(' ', '')
            model_class = getattr(model_module, model_class_name)

        except (IndexError, ModuleNotFoundError):
            raise ImportError(
                '{} not found!'.format('models.' + model_name))

        return cls(model_class)
