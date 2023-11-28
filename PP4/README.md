# 👩‍💻 Django Project

Цей проект - Django веб-додаток, який реалізує прості API та веб-сторінки.

## 🚀 Встановлення

1. **Склонуйте репозиторій:**

   ```bash
   git clone https://github.com/RTE610/PP-4.git
   cd PP-4
   ```
    
2. **Створіть та активуйте віртуальне середовище:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # для Linux або MacOS, або .\venv\Scripts\activate для Windows
   ```

3. **Встановіть залежності:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Застосуйте міграції:**

   ```bash
   python manage.py migrate
   ```

5. **Запустіть сервер розробки:**

   ```bash
   python manage.py runserver
   ```

6. **Відкрийте [http://127.0.0.1:8000/](http://127.0.0.1:8000/) у вашому веб-браузері.**

## 🌐 API

### Hello World Endpoint

- **URL:** `api/v1/hello-world14`
- **Метод:** GET
- **Параметри шляху:**
  - `variant_number` (ціле число) - номер варіанту
- **Відповідь:**
  - Текстова відповідь з "Hello World!14" та HTTP статусом 200.

## 🤝 Внесок

Пропозиції чи виправлення? Створіть pull request або відкрийте issue.

## 📄 Ліцензія

Проект розповсюджується під ліцензією [MIT](LICENSE).

## 🔗 URL Configuration

URL-конфігурація для проекту PP4 в `main/urls.py`:

```python
from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('', views.test),
    path('api/v1/hello-world14/', views.Task),
]
```

Не забудьте додати цей шлях до основного файлу конфігурації URL (`urls.py`):

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'))
]
```

Замініть `RTE610/PP-4` на свій URL репозиторію GitHub.