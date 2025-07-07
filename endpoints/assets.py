import os
from typing import Mapping
from werkzeug import Request, Response
from werkzeug.utils import send_from_directory
from dify_plugin import Endpoint


class AssetsEndpoint(Endpoint):
    def _invoke(self, r: Request, values: Mapping, settings: Mapping) -> Response:
        """
        Invokes the endpoint with the given request.
        """
        path = values.get("path")
        if not path:
            return Response("Not Found", status=404)
        directory = os.path.join(os.path.dirname(__file__), "static", "assets")
        return send_from_directory(directory, path, r.environ)
