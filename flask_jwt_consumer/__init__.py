name = "flask_jwt_consumer"

from importlib.metadata import version

try:
    __version__ = version(__name__)
except Exception:
    __version__ = "0.0.0"


from .flask_jwt_consumer import JWTConsumer
from .helpers import get_jwt_payload, get_jwt_raw
from .decorators import requires_jwt
from .errors import AuthError
