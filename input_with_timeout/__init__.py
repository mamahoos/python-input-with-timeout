"""
## Input with Timeout

The 'input-with-timeout' module provides a cross-platform method to capture user input with a timeout feature.
This is particularly useful for creating command-line interfaces where the program needs to proceed if the user does not provide input within a certain time frame.

### Features

- Customizable `timeout` for user input.
- Cross-platform support (currently only Windows is supported).
- Easy integration with existing Python projects.

This module is part of the 'python-input-with-timeout' project by mamahoos, available at:
https://github.com/mamahoos/python-input-with-timeout

For any inquiries or contributions, you can reach out via:
- Telegram: https://t.me/mamahoos
- Email: m4m4hoos@gmail.com
- Github: https://github.com/mamahoos
"""

from .main import input_with_timeout
from .__version__ import (
    __title__       ,
    __description__ ,
    __version__     ,
    __version_info__,
    __author__      ,
    __author_email__,
    __url__         ,
    __copyright__   ,
    __license__     ,
    __keywords__    ,
    __platforms__   ,
    __classifiers__ ,
)
