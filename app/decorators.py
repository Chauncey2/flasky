from functools import wraps
from flask import abort
from flask_login import current_user
from .models import Permission

"""
permission 这个装饰器妙就妙在接收了一个参数，返回一个装饰器，当传入参数的时候
也就相当于是一种函数引用，这个直接调用装饰器没有区别
"""


def permission_required(permission):
    def decorate(f):
        @wraps(f)
        def decorate_func(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)

        return decorate_func

    return decorate


def admin_required(f):
    return permission_required(Permission.ADMIN)(f)
