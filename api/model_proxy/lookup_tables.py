"""This is an in-memory representation of the lookup table models that will
go in the database. One of the great things about sepparating concerns and
coding to interfaces, rather than implementations, is that in a case like this,
where I don't have time to set up a whole database, I can make a mockup of the necessary
data here, and use it until I get a database working. The interface for both will
be the same, so I don't have to care which I'm using! Additionally, when the database
is set up, I can use these data structures to fill it with information, rather than typiung
all of this out again!
"""

product_model = {
    'R': 'RadRover',
    'M': 'RadMini',
    'W': 'RadWagon',
    '6': 'RadCity 16',
    '9': 'RadCity 19',
    'S': 'RadCity Stepthru',
    'B': 'RadBurro',
    'H': 'RadRhino',
    'C': 'Large Cargo Box',
    'K': 'Small Cargo Box',
    'P': 'Pedicab',
    'F': 'Flatbed',
    'T': 'Truckbed',
    'N': 'Insulated Cargo Box',
    'Y': 'Runner',
}

model_year = {
    'A': '2018',
    'B': '2019',
    'C': '2020',
    'D': '2021',
    'E': '2022',
    'F': '2023',
    'G': '2024',
    'H': '2025',
    'I': '2026',
}

month_built = {
    '1': 'January',
    '2': 'February',
    '3': 'March',
    '4': 'April',
    '5': 'May',
    '6': 'June',
    '7': 'July',
    '8': 'August',
    '9': 'September',
    'O': 'October',
    'N': 'November',
    'D': 'December',
}

factory = {
    'F': 'FactoryF',
    'V': 'FactoryV',
}
