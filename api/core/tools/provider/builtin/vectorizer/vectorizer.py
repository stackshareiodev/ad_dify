from core.tools.provider.builtin_tool_provider import BuiltinToolProviderController
from core.tools.errors import ToolProviderCredentialValidationError

from core.tools.provider.builtin.vectorizer.tools.vectorizer import VectorizerTool

from typing import Any, Dict

class VectorizerProvider(BuiltinToolProviderController):
    def _validate_credentials(self, credentials: Dict[str, Any]) -> None:
        try:
            VectorizerTool().fork_tool_runtime(
                meta={
                    "credentials": credentials,
                }
            ).invoke(
                user_id='',
                tool_parameters={
                    "mode": "test",
                    "image_id": "__test_123"
                },
            )
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))