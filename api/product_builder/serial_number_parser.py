from collections.abc import Iterator, Iterable
from collections import OrderedDict


DEFAULT_PATTERN_KEY = OrderedDict([
    ('product_model', 1),
    ('model_year', 1),
    ('month_built', 1),
    ('year_built', 2),
    ('factory', 1),
    ('version', 1),
    ('unique_id', 12),
])

class SerialNumberParser(Iterable):
    """The concrete implementation of Parser for serial number patterns
    that match those in the examples given in the assignment. It stores
    two iterables, and is composed of an iterator. As iterables, these
    classes do not handle validation of inputs, they simply iterate and
    return.
    """

    def __init__(self, serial_number, pattern_key=DEFAULT_PATTERN_KEY):
        self.pattern_key = pattern_key
        self.serial_number = serial_number

    def __iter__(self):
        """
        Returns the iterator ready to slice and label the serial number into
        its constituent parts.

        Returns:
            An iterator of the serial number broken apart by the length and
            order information inside the pattern_key

        Example:

        from product_builder.pattern_parser import SerialNumberParser

        parsed = {}
        serial_parser = SerialNumberParser(pattern_key, serial_number)
        for result in parsed_serial:
            parsed[result[0]] = result[1]

        return parsed
        """
        return SerialNumberIterator(self.serial_number, self.pattern_key)


class SerialNumberIterator(Iterator):
    """Iterates over both the given serial number and the pattern_key ordered dict
    to extract each part of the serial number into a labeled dictionary.

    Attributes:
        serial_number (str): The serial number to be iterated.
        pattern_key (OrderedDict): The ordered labels for each meaningful
            piece of data inside the serial number, and the length of each.

    """
    def __init__(self, serial_number, pattern_key):
        self.serial_number = serial_number
        self.pattern_key_as_list = list(pattern_key.items())
        self.serial_position = 0
        self.key_position = 0

    def __next__(self):
        """Returns the next item in the serial_number sequence, based on the associated key
        and value in the pattern_key attr. This must maintain two pointers,
        and exits when the serial number is exhausted.

        Returns:
            A key, value tuple of the pattern_key key and the serial value
        """
        try:
            key = self.pattern_key_as_list[self.key_position][0]
            digits_to_extract = self.pattern_key_as_list[self.key_position][1]

            value = self.serial_number[
                self.serial_position: self.serial_position + digits_to_extract]

            self.serial_position += digits_to_extract
            self.key_position += 1
        except IndexError:
            raise StopIteration()

        return (key, value)
