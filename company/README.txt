This is a REST API for a simple CRM system that allows you to manage companies and their employees.

Create a virtual environment and activate it:

cd "NAME"
python3 -m venv venv
source venv/bin/activate
Install the dependencies:

pip install -r requirements.txt

Set up the database:

python manage.py migrate

Start the development server:

python manage.py runserver
The API will be available at http://127.0.0.1:8000/.

The API has the following endpoints:

/api/companies/: CRUD API to manage companies.
/api/employees/: CRUD API to manage employees.

You can use the built-in Django admin interface to manage the data. 
