from typing import Mapping
import json
from werkzeug import Request, Response
from dify_plugin.entities.model.message import UserPromptMessage, SystemPromptMessage
from dify_plugin import Endpoint


MARKDOWN_SYSTEM_PROMPT = """
1. You need to generate a mindmap based on the user's prompt.
2. The mindmap should be in markdown format.
3. Only output the markdown content, no other text.

Example Response:
# Core Concept
## Sub Concept 1
## Sub Concept 2
"""

MERMAID_SYSTEM_PROMPT = """
1. You need to generate a mermaid diagram based on the user's prompt.
2. The mermaid diagram should be in mermaid format.
3. Only output the mermaid content, no other text.

Example Response:
flowchart TD
 A[Christmas] -->|Get money| B(Go shopping)
 B --> C{Let me think}
 C -->|One| D[Laptop]
 C -->|Two| E[iPhone]
 C -->|Three| F[Car]
"""

class LLMEndpoint(Endpoint):
    def _invoke(self, r: Request, values: Mapping, settings: Mapping) -> Response:
        """
        Invokes the endpoint with the given request.
        """
        model = settings.get("model")
        data = r.get_json()
        prompt = data.get("prompt")
        type = data.get("type")
        if type == "markdown":
            system_prompt = SystemPromptMessage(content=MARKDOWN_SYSTEM_PROMPT)
        else:
            system_prompt = SystemPromptMessage(content=MERMAID_SYSTEM_PROMPT)
        prompt_messages = [
            system_prompt,
            UserPromptMessage(content=prompt),
        ]
        response = self.session.model.llm.invoke(
                model_config=model,
                prompt_messages=prompt_messages,
                stream=False,
            )
        
        result = json.dumps({
            "result": response.message.content
        })

        return Response(result, status=200, content_type="application/json")
