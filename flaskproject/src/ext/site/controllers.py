from src.ext.db.models import Items


def get_all_active_stores():
    """Get all stores"""


def get_items():
    itens = Items.query.filter_by(available='1').all()
    return itens
