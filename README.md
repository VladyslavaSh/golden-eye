# golden_eye

### Web service that monitors and collects current exchange rates from open APIs

### Technologies used:

- Language: Python
- Framework: Flask
- Database: SQLite
- ORM: Peewee
- Libraries: requests, peewee, Flask, requests
- Frontend: Jinja2
- WSGI: Gunicorn
- Testing: Pytest
- Deployment: Heroku


### External APIs:

- The Ukrainian State Bank PrivatBank: <a href="https://api.privatbank.ua/#p24/exchange" target="_blank">https://api.privatbank.ua/#p24/exchange</a>
- Monobank Universal Bank: <a href="https://api.monobank.ua/docs/" target="_blank">https://api.monobank.ua/docs/</a>

### Database’s structure:


### Files:

- `modules.py` <br/>
The creation of models (database tables) and initialisation of the database.
- `config.py` <br/>
Parameters for logger configuration, database file path and other settings.
- `tests.py`
- `privat_api.py` <br/>
Gets data about the rate to be changed from the database. Sends a request to the api of Privatbank to get the desired rate from the response. Updates the updated field data and the rate value received via api.
- `monobank_api.py` <br/>
Gets data about the rate to be changed from the database. Sends a request to the Monobank API, get the desired exchange rate from the JSON response. Updates the data in the 'updated' field and the course value received from the API.

