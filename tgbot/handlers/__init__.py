from .admin import admin_router
from .start import start_router
from .vacancies import vacancies_router
from .company import company_router
from .employments import employment_router

routers_list = [
    admin_router,
    start_router,
    company_router,
    vacancies_router,
    employment_router
]

__all__ = [
    'routers_list',
]
