# Task-Manager

### PL

Jeżeli chcesz otworzyć aplikację na serwerze lokalnym:

1. Pobranie potrzebnych bibliotek
> *pip install -r requirements.txt*
3. Uwtorzenie pliku .env w głównym folderze aplikacji i wygenerowanie SECRET_KEY przy użyciu biblioteki *secrets*
> import secrets
> 
> *token_hex(16)*
4. Utworzenie bazy danych:  
> *python*
>> *from app import db*
>> 
>> *db.create()*
