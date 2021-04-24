from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
from ..models import Permission

"""
蓝图，路由、上下文管理器
"""


@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
