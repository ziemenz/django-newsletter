try:
    from django.utils.version import get_version
except ImportError:
    from .get_version import get_version

VERSION = (0, 6, 0, 'alpha', 0)

__version__ = get_version(VERSION)
