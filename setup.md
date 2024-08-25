This is a setup script, you just copy and paste.
But before that, ensure you're using venv and have node and docker installed.

Edit database configuration in the .env file

# Pre-installation script

After running the script, please edit the .env file to configure your database.

```bash
python -m pip install virtualenv
git clone https://github.com/DrowningToast/django-setup-script.git
cd django-setup-script
copy .env.example .env
code .
cd ..
mkdir django
cd django
```

# Run for start project setup

```bash
py -m venv myvenv
myvenv\Scripts\activate.bat

python -m pip install django
python -m django --version

django-admin startproject PROJECT_NAME

python -m pip install psycopg2
python -m pip install psycopg2-binary

docker-compose -f ../django-setup-script/docker-compose.yml up -d --build

python -m pip install django-extensions ipython jupyter notebook
python -m pip install ipython==8.25.0 jupyter_server==2.14.1 jupyterlab==4.2.2 jupyterlab_server==2.27.2
python -m pip install notebook==6.5.7

git clone git@github.com:aaapwn/Server-Side-Web-Development.git
code .

```
