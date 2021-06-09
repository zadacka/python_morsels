from collections import UserDict
from typing import Optional, Mapping


class PermaDict_Alex(UserDict):
    """ Needed a hint on what class to derive from ... tied myself in knots with 'dict' because it kept
        setting the 'self.silent' as self ... which was a dict key. My dirty work around to use
        an external map {object_id: silent boolean} didn't work either, though I'm not sure why, because the super()
        call definitely did *not* seem to get the silent arg passed through...

        *facepalm*  - becuase I was doing __new__ not __init__! Oh, stupid, stupid, stupid.
        """

    def __init__(self, *args, silent=False, **kwargs):
        self.silent = silent
        super().__init__(*args, **kwargs)

    def __maybe_set_item__(self, key, value, force):
        if key not in self.data.keys() or force:
            self.data[key] = value
        else:
            if self.silent:
                pass
            else:
                raise KeyError(f"Key {key} already in this PermaDict!")

    def __setitem__(self, key, value):
        self.__maybe_set_item__(key, value, force=False)

    def update(self, E=None, force=False, **F):
        if hasattr(E, 'keys'):
            for k in E.keys():
                self.__maybe_set_item__(k, E[k], force=force)
        elif E is not None:
            for k, v in E:
                self.__maybe_set_item__(k, v, force=force)

        for k, v in F.items():
            self.__maybe_set_item__(k, v, force=force)

    def force_set(self, k, v):
        self.__maybe_set_item__(k, v, force=True)


class PermaDict(UserDict):
    def __init__(self, *args, silent=False, **kwargs):
        self.silent = silent
        super().__init__(*args, **kwargs)

    def force_set(self, key, value):
        return super().__setitem__(key, value)

    def update(self, *args, force=False, **kwargs):
        if force:
            # we know that UserDict has a self.data where the actual data lives, so we can do:
            return self.data.update(*args, **kwargs)
        else:
            # if not forcing, then we will try the UserDict's update() ... which uses the PermaDict's __setitem__()
            # much more efficient than having to loop through stuff with __setitem__!
            return super().update(*args, **kwargs)

    def __setitem__(self, key, value):
        """ Interesting: __setitem__ NEVER is called to change the value of an existing key:value map"""
        if key not in self:
            return super().__setitem__(key, value)
        if not self.silent:
            raise KeyError(f"{key} already in dictionary")