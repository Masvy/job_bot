from .admin import admin_router
from .start import start_router
from .vacancies import vacanties_router
from .company import company_router

routers_list = [
    admin_router,
    start_router,
    company_router,
    vacanties_router,
]

__all__ = [
    'routers_list',
]
