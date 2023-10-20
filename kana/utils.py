# # https://stackoverflow.com/questions/128573/using-property-on-classmethods, Retrieved October, 2023.
# from functools import cached_property

from const import IterSymbol

# obj = IterSymbol('', True, False)

# for f in dir(obj):
#     print('before getattr', obj, f)
#     getattr(obj, f)
#     print('after getattr', obj, f)


class A:
    a = 1
    b = 2
    c = 3
    d = 4

    def f(self):
        return [getattr(self, v) for v in get_obj_varnames_with_specified_type(self, var_type=int)]


def get_obj_varnames_with_specified_type(obj: object, var_type):
    # print([f for f in dir(obj) if isinstance(getattr(obj, f), var_type)])
    return [f for f in dir(obj) if isinstance(getattr(obj, f), var_type)]


dict_what = A().f()
print(dict_what)

# class classproperty(cached_property):
#     def __get__(self, owner_self, owner_cls):
#         return self.fget(owner_cls)


# class C(object):

#     @classproperty
#     def x(cls):
#         return 1


# assert C.x == 1
# assert C().x == 1

# # https://stackoverflow.com/questions/62129639/cached-property-and-classmethod-doesnt-work-together-django, Retrieved October, 2023


# # class cached_classproperty(classproperty):
# #     def __init__(self, method=None):
# #         print("method: ", method)
# #         self.fget = method

# #     def get_result_field_name(self):
# #         return self.fget.__name__ + "_property_result" if self.fget else None

# #     def __get__(self, instance, cls=None):
# #         result_field_name = self.get_result_field_name()

# #         if hasattr(cls, result_field_name):
# #             return getattr(cls, result_field_name)

# #         if not cls or not result_field_name:
# #             return self.fget(cls)

# #         setattr(cls, result_field_name, self.fget(cls))
# #         return getattr(cls, result_field_name)

# #     def getter(self, method):
# #         self.fget = method
# #         return self
