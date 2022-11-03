* Virtual environment : `python3 -m venv venv`
* Run venv : `source venv/bin/activate`
* Install packages : `pip install -r requirements.txt`
* Run server :
    ```
    cd django_ml
    python manage.py runserver
    ```
* API endpoint for prediction -
    http://localhost:8000/api/predict
    <br>Sample JSON :
    ```
    {
        "age": 0.2,
        "menopause": 1.0,
        "tumor-size": 0.3,
        "inv-nodes": 0.666667,
        "node-caps": 1.0,
        "deg-malig": 0.5,
        "breast": 1.0,
        "breast-quad": 0.25,
        "irradiat": 1.0
    }
    ```