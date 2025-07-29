To deploy your **Django project using SQLite on cPanel**, you can **keep the same database** and follow the steps below. Make sure your cPanel hosting supports **Python apps** (e.g., through **Python Selector**, available in many shared hosting plans like Hostinger, A2Hosting, etc.).

---

## ✅ Steps to Deploy Django on cPanel with SQLite (No DB Change):

---

### ✅ 1. Prepare Files Locally

* Ensure your project is ready for production:

  ```bash
  python manage.py collectstatic
  ```
* Zip your entire project folder, including:

  * `manage.py`

  * `db.sqlite3`

  * `core/` (your app)

  * `django_project/` (project directory)

  * `static/`, `staticfiles/`, `media/`

  * All dependencies listed in `requirements.txt`

  > If you don't have `requirements.txt`, generate one:

  ```bash
  pip freeze > requirements.txt
  ```

---

### ✅ 2. Upload to cPanel

1. Log in to **cPanel**
2. Go to **File Manager**
3. Navigate to the directory where you want to host (e.g., `/home/username/` or `public_html/`)
4. Upload your zipped project and **extract** it.

---

### ✅ 3. Set up Python App in cPanel

1. Go to **Setup Python App** in cPanel

2. Click **Create Application**:

   * Choose Python version (e.g., 3.10+)
   * Application Root: where your project is extracted (e.g., `myapp`)
   * Application URL: like `/myapp`
   * WSGI file: later point it to `django_project/wsgi.py`

3. Click **Create**

---

### ✅ 4. Install Requirements

Once the app is created:

1. In the Python App screen, there is a **terminal command** to access the virtual environment. Run it via **Terminal** in cPanel:

   ```bash
   source /home/username/virtualenv/myapp/3.10/bin/activate
   pip install -r /home/username/myapp/requirements.txt
   ```

2. If `whitenoise` or other packages fail to install, try upgrading pip:

   ```bash
   pip install --upgrade pip setuptools wheel
   ```

---

### ✅ 5. Configure WSGI

Edit the `passenger_wsgi.py` file (usually auto-generated). Modify it like this:

```python
import sys
import os

sys.path.insert(0, "/home/username/myapp")  # full path to your Django project
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

> Replace `/home/username/myapp` and `django_project` accordingly.

---

### ✅ 6. File Permissions & Media

* Make sure `db.sqlite3`, `media/`, and `staticfiles/` are **writable** (CHMOD 755 or 775).
* If media files aren’t accessible, set up `.htaccess` or add routes in `urls.py`:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

### ✅ 7. Debug off (optional but recommended)

In `settings.py`:

```python
DEBUG = False
ALLOWED_HOSTS = ["yourdomain.com", "www.yourdomain.com"]
```

---

### ✅ 8. Restart the App

* In cPanel > **Setup Python App**, click **Restart**.

---

### ✅ 9. Test

* Visit the app from the browser using your domain or subdomain.
* Ensure everything loads: static files, media, forms, admin, etc.

---

## Notes:

* SQLite is fine for small or medium apps on cPanel. For production scaling, consider PostgreSQL/MySQL.
* `DEBUG=True` is okay during deployment but switch to `False` in production.
* You don’t need `gunicorn` or `nginx` in cPanel – **Passenger (mod\_wsgi)** handles that.

---

If you tell me:

* The **folder name you extracted to**
* Your **domain/subdomain name**
* Any **error messages** you're seeing

I can help tailor the exact WSGI and cPanel settings for you.
