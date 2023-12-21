from flask import Blueprint

cliente = Blueprint('cliente',
                    __name__,
                    url_prefix="/cliente",
                    template_folder='templates')

from . import routes