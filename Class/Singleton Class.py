"""
Python is an Object oriented programming language
i.e everything in Python is an object. There are special kind
of methods in Python known as magic methods or dunder methods
(dunder here means “Double Underscores”). Dunder or magic methods
in Python are the methods having two prefix and suffix underscores
in the method name. These are commonly used for operator
overloading.
Few examples for magic methods are: __init__, __add__, __len__,
 __repr__ etc."""

import functools


def singleton(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if not wrapper.instance:
            wrapper.instance = cls(*args, **kwargs)
        return wrapper.instance
    wrapper.instance = None
    return wrapper


@singleton
class ONE:
    pass


first = ONE()
second = ONE()

print(first is second)
