"""authentik lib converter utilities"""
from typing import Any, Callable, Dict, T, Type

import cattr

class DictConverter(cattr.GenConverter):
    """ Converts from a dictionary to a given type """
    def __init__(self):
        super().__init__()

        # By default, cattr raises an error if it sees a type that does not
        # have a matching handler. Register a passthrough handler as the fallback
        # if nothing else matches to handle cases where a simple passthrough is needed
        dispatch_pair = (lambda _: True, self._passthrough_handler_or_error, False)
        self._structure_func._function_dispatch._handler_pairs.insert(-1, dispatch_pair)

    def _passthrough_handler_or_error(self, obj: Any, cl: Type[T]) -> T:
        if isinstance(obj, cl):
            return obj
        
        self._structure_error(obj, cl)

DICT_CONVERTER = DictConverter()

def from_dict(cl: Type[T], data: Dict) -> T:
    return DICT_CONVERTER.structure(data, cl)