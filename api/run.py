""" The main Flask application file that bootstraps and starts the app. """

import os

from flask_graphql import GraphQLView

from bootstrap import app_factory
from schema import schema


app = app_factory()

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True,
    )
)

if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG", False))
