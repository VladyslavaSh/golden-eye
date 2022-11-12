# golden_eye

### Web service that monitors and collects current exchange rates from open APIs.

### Website link: https://guarded-shore-08598.herokuapp.com/

### Technologies used:

- Language: Python
- Framework: Flask
- Database: SQLite
- ORM: Peewee
- Libraries: requests, peewee, Flask, unittest, traceback, importlib
- Frontend: Jinja2
- WSGI: Gunicorn
- Testing: Pytest
- Deployment: Heroku


### External APIs:

- The Ukrainian State Bank PrivatBank: <a href="https://api.privatbank.ua/#p24/exchange" target="_blank">https://api.privatbank.ua/#p24/exchange</a>
- Monobank Universal Bank: <a href="https://api.monobank.ua/docs/" target="_blank">https://api.monobank.ua/docs/</a>


### Files:

- `modules.py` <br/>
The creation of models (database tables) and initialisation of the database.
- `config.py` <br/>
Parameters for logger configuration, database file path and other settings.
- `tests.py` <br/>
Module with tests.
- `privat_api.py` <br/>
Gets data about the rate to be changed from the database. Sends a request to the api of Privatbank to get the desired rate from the response. Updates the updated field data and the rate value received via api.
- `monobank_api.py` <br/>
Gets data about the rate to be changed from the database. Sends a request to the Monobank API, get the desired exchange rate from the JSON response. Updates the data in the 'updated' field and the course value received from the API.
- `coin_api.py` <br/>
Gets data about the rate to be changed from the database. Sends a request to the Coin API, and gets the desired exchange rate from the JSON response. Updates the data in the 'updated' field and the course value received from the API.
- `app.py ` <br/>
Module in which the creation of the Flask application is carried out.
- `runserver.py` <br/>
Module in which the application is launched on the test local server.
- `views.py ` <br/>
Module, which describes the functions and their corresponding application URLs.
- `controllers.py ` <br/>
Module with functions or classes that describe the main logic of work models.
- `utils.py ` <br/>
Module with utility functions that are used from various modules.
- `__init__.py` <br/>
Contains the common configuration for all APIs: logging data, update_rate and send_request functions.
