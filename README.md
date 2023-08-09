# AER - Automated Facial Recognizer
The functionality of Automated Facial Recognizer web application is to use a facial emotion recognition model to analyze selected frames and classify the emotions of all detected faces. It includes an additional image mode, so the user can test the simpler version. In both cases, a pre-trained machine learning model is used. The application by default uses DAN model, but it can easily be changed to a different one.  
The web application is dedicated to being used by scholars to help in their research, as well as people having problems with emotion identification, psychologists, marketers, and generally people interested in FER technology. As only visuals are processed by the model, uploaded video clips do not have to include audio. Though the results are not always completely accurate, up to eight emotions can be recognized in the media.
The application is a part of my thesis "Automated tool for facial emotion recognition in video".

---

### Technologies and tools used:
- Django
- React
- Celery
- RabbitMQ
- Selenium (Chrome Webdriver with Python)

---

## Installation instruction:
### Backend:
1.	Install a virtual environment:
```
pip install virtualenv
```
2.	Create a virtual environment (venv is the name of virtual environment that is being created and replaced by user with any valid value):
```
virtualenv venv
```
3.	Activate a virtual environment:
```
source venv/bin/activate
```
4.	Install all necessary modules and packages:
```
pip install -r reguirements.txt
```
5.	(Optional) Deactivate a virtual environment:
```
deactivate
```

### Frontend:
1.	Install all defined dependencies for React:
```
npm install
```
---

## Run instruction:
Once the installation was successful, the application can be started by running script run_application.sh available in main folder of the whole app.
To run the application manually:  
1.	Start frontend React.js server  
Current directory: */aer_web/frontend
```
npm start
``` 
2.	Migrate mock data  
Current directory: */aer_web/backend
```
python manage.py migrate
```
3.	Start Django server  
Current directory: */aer_web/backend
```
python manage.py runserver
```
4.	Celery worker can be initialized manually using the following command:  
For UNIX OS:
```
celery -A backend.celery worker –loglevel=ingo -P
```
For Windows OS (with prerequisite of gevent pack being installed on the machine):  
```
celery -A backend.celery worker –loglevel=ingo -P gevent
```
After successful start (either manually or by using the batch script), the application should be available in the browser at the address localhost:5000.

---

### Future works
Future works include the improvement of the frontend’s automatic unit tests. Currently, they cover only the most basic functionalities, thus not all of the code’s lines are covered. Moreover, the SQlite database could be upgraded to something more efficient, e.g., PostgreSQL. The currently implemented database is best for web applications with low to moderate traffic, but if it were high, it could negatively influence the performance of the application.






