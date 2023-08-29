from .employment import employment_router
from .start import start_router
from .vacancies import vacanties_router

routers_list = [
    start_router,
    employment_router,
    vacanties_router,
]

__all__ = [
    'routers_list',
]
