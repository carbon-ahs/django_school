## Backend part of school site. 

This project uses python 3.12
for prod 3.11.12 needed.
link: https://github.com/adang1345/PythonWindows/blob/master/3.11.12/python-3.11.12-amd64-full.exe
guide: https://youtu.be/h2w8oNw_W80?si=rodPqaHJL-NygxUq
## Run commands

```python
# 1. Create the virtual environment
py -m venv .venv

# 2. Activate the virtual environment
source .venv/Scripts/activate

# 3. Upgrade pip within the virtual environment
py -m pip install --upgrade pip

# 4. Install dependencies from requirements.txt
pip install -r requirements.txt

# 5. Run django server
py manage.py runserver

# 6. collect static file
python manage.py collectstatic

# 7 run command with waitress
waitress-serve --port=8000 django_project.wsgi:application
 
```

## Migration migrat

```
py manage.py makemigrations
py manage.py migrate
```
