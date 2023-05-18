# Task-Manager

### PL

Jeżeli chcesz otworzyć aplikację na serwerze lokalnym:

1. Wpisz w terminal - *pip install -r requirements.txt* - aby pobrać potrzebne biblioteki
2. Stwórz plik .env w głównym folderze aplikacji i wygeneruj SECRET_KEY przy użyciu biblioteki *secrets*
3. Stwórz bazę danych:  

* Otwórz konsolę pythona: *python*
* Pobierz utworzony wcześniej model bazy danych z app: *>>> from app import db*
* Utwórz bazę danych: *>>> db.create()*

### EN

If you want to open the application on the local server:

1. Open terminal and type - pip install -r requirements.txt - to download the needed libraries
2. Create .env file in the main folder and generate SECRET_KEY using *secrets* library
3. Create a database:

* Open the python console: *python*
* Get the database model you created earlier from app: *>>> from app import db*
* Create the database: *>>> db.create()* 
