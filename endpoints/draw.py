import os
from typing import Mapping
from werkzeug import Request, Response
from werkzeug.utils import send_from_directory
from dify_plugin import Endpoint


class DrawEndpoint(Endpoint):
    def _invoke(self, r: Request, values: Mapping, settings: Mapping) -> Response:
        """
        Invokes the endpoint with the given request.
        """
        directory = os.path.join(os.path.dirname(__file__), "static")

        return send_from_directory(directory, "index.html", r.environ)
