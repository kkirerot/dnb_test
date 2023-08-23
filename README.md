The is an backend application where the goal is to submit a loan application with basic authentication

You will need python version 3.10.6 and pip installed

THe installations can be found here:
https://www.python.org/downloads/windows/

after cloning the repository you can open a command window, and navigate to the folder where the manager file is.

After that run the command:

pip install -r requirements.txt

py mange.py migrate

Then create a super user
python manage.py createsuperuser

Then rund the command:
py manage.py runserver

Then the application should be running


Then you can navigate to localhost:8000/api/create/ for testing of creating an loan_application

If you want to se all the applications you can go localhost:8000/api/list/ to view the applications (must be a staff user)


To run the tests you go to the command window and run the command:
py manage.py test applications/loan_application