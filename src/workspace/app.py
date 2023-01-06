from fastapi import FastAPI
from .api import router


tags_metadata = [
    {
        'name': 'auth',
        'description': 'Авторизация и регистрация',
    },
    {
        'name': 'operations',
        'description': 'Работа с данными',
    },
    {
        'name': 'reports',
        'description': 'Импорт и экспорт отчетов',
    },
]

app = FastAPI(
    title='Finance Accounting',
    description='Applications created on FASTAPI frameworks to keep track of your finances',
    version='1.0',
    openapi_tags=tags_metadata,
)
app.include_router(router)
