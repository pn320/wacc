import logging

import structlog

__version__ = "0.0.1a1"

structlog.configure(wrapper_class=structlog.make_filtering_bound_logger(logging.DEBUG))
