from functools import partial
import inspect

def typed_property(field, val_type):
    field_name = '_'+field
    def gets(self):
        return getattr(self, field_name)
    def sets(self, value):
        if not isinstance(value, val_type):
            raise ValueError("Must provide a %s" % val_type)
        setattr(self, field_name, value)
    return property(gets, sets)

Integer = partial(typed_property, val_type=int)
String = partial(typed_property, val_type=str)
Float = partial(typed_property, val_type=float)

