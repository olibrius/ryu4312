# Copyright (C) 2013,2014,2015 Nippon Telegraph and Telephone Corporation.
# Copyright (C) 2013,2014,2015 YAMAMOTO Takashi <yamamoto at valinux co jp>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import functools
import types


def add_method(cls, method_name, method):
    """Add the method to the class dynamically.

    Handles both plain functions and functools.partial objects.
    functools.partial objects are not descriptors so they won't receive
    'self' automatically; we wrap them in a real function.
    """
    if isinstance(method, functools.partial):
        # Wrap the partial so it acts as a proper instance method.
        # The partial's underlying function expects (self, ...) so we
        # pass the instance as the first positional arg.
        _partial = method

        def _wrapper(self, _p=_partial):
            return _p(self)

        _wrapper.__name__ = method_name
        _wrapper.__qualname__ = "%s.%s" % (cls.__qualname__, method_name)
        setattr(cls, method_name, _wrapper)
    else:
        method.__name__ = method_name
        if not hasattr(method, "__qualname__"):
            method.__qualname__ = "%s.%s" % (cls.__qualname__, method_name)
        setattr(cls, method_name, method)
