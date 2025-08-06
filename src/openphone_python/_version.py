"""
Version information for openphone-python.
"""

__version__ = "0.1.1"
__version_info__ = tuple(int(i) for i in __version__.split(".") if i.isdigit())

# Version metadata
VERSION_MAJOR = __version_info__[0] if len(__version_info__) > 0 else 0
VERSION_MINOR = __version_info__[1] if len(__version_info__) > 1 else 0
VERSION_PATCH = __version_info__[2] if len(__version_info__) > 2 else 0

# API version compatibility
API_VERSION = "v1"
MINIMUM_API_VERSION = "v1"
