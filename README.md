
# Technologies

* Python 3.8
* Django 3.0.10
* Django CMS 3.7.4

# Install

## Step 1: Create a virtual environment


```bash
python3 -m venv mysite-env
```

```bash
source mysite-env/bin/activate
```

## Step 2: Update pip

```bash
pip install --upgrade pip
```

```bash
cd mysite-demo
```

## Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

## Step 4: Migrate
```bash
python3 manage.py makemigrations mysite
```

```bash
python3 manage.py migrate mysite
```

## Step 5: Create Admin Login User CMS
```bash
python3 manage.py createsuperuser
```

## Step 6: Run CMS
```bash
python3 manage.py runserver
```