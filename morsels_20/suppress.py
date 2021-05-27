from contextlib import contextmanager, ContextDecorator
from functools import wraps


class ExceptionInfo:
    # could also use types.SimpleNamespace for this
    exception = None
    traceback = None


@contextmanager
def suppress1(*exceptions):
    """ This approach uses Corey Schafer's neat contextmanager pattern"""
    info = ExceptionInfo()
    try:
        yield info
    except exceptions as e:
        info.exception = e
        info.traceback = e.__traceback__  # or  sys.exc_info in Python 2


class suppress(ContextDecorator):
    def __init__(self, *exception_types):
        self.exception_types = exception_types

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.exception = exc_val
        self.traceback = exc_tb
        return isinstance(exc_val, self.exception_types)


# from contextlib import suppress <- the easiest solution: use the standard library one!!

class suppress_1:
    """ doesn't work as a decorator though... """

    def __init__(self, *exceptions) -> None:
        self.exceptions = exceptions
        self.suppressed = ExceptionInfo()
        super().__init__()

    def __enter__(self):
        return self.suppressed

    def __exit__(self, exc_type, exc_val, exc_tb):
        if isinstance(exc_val, self.exceptions):
            # if exc_type and any(issubclass(exc_type, e) for e in self.exceptions):
            # note: isinstance is better than issubclass because it doesn't raise when given None, so we don't need the
            #  extra 'has an exception been raised' check
            # note2: both the 'isinstance' and 'issubclass' work with a single item OR with a tuple of types to check!!
            self.suppressed.exception = exc_val
            self.suppressed.traceback = exc_tb
            return True
        return False


class suppress_trey:
    """ Really nice: store the 'exception', 'traceback' attrubtes on self, return self!"""

    def __init__(self, *exception_types):
        self.exception_types = exception_types

    def __call__(self, function):
        """ Magic to make this a decorator """

        @wraps(function)
        def wrapper(*args, **kwargs):
            with self:
                return function(*args, **kwargs)

        return wrapper

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.exception = exc_val
        self.traceback = exc_tb
        return isinstance(exc_type, self.exception_types)
