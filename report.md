# 1. Technologie

Aplikacja została napisana za pomocą języka *Python* i biblioteki *Flask*. Do utworzenia bazy danych skorzystano z biblioteki *SqlAlchemy* i technologii ORM. Skorzystano również z biblioteki *Pandas* oraz *Numpy*.
Do zabezpieczenia haseł wykorzystano bibliotekę *bcrypt* wraz z użyciem peppera. Frontent został wykonany samodzielnie przy użyciu narzędzi: *HTML*, *CSS*, *Bootstrap5*, *Alpine.js*, *Jinja2*, *SweetAlerts2*.

# 2. Struktura aplikacji

- task_manager
  - app
    - admin
    - auth
      - templates
        - auth
          - base.html
        - login.html - frontent do podstrony logowania (/auth/login)
        - register.html - frontent do podstrony rejestracji (/auth/registration)
      - __init__.py - zaalokowanie blueprinta dla sekcji administratorskiej
      - crud.py - CRUD dla sekcji autoryzacyjnej
      - routes.py - API dla sekcji autoryzacyjnej
      - views.py - ścieżki do poszczególnych podstron sekcji administratorskiej
    - database
      - data.db - baza danych
      - db_functions.py - funkcje pomocnicze do zarządzania db
      - models.py - modele ORM do db
    - helpers
      - security.py - hashowanie hasel i sprawdzanie poprawnosci danych przy logowaniu
    - main
      - templates
        - dashboard.html - frontent dla głównej tablicy (/dashboard)
        - home_page.html - frontent dla strony powitalnej (/)
      - __init__.py - zaalokowanie blueprinta dla sekcji głównej
      - crud.py - CRUD dla sekcji głównej
      - routes.py - API dla sekcji głównej
      - views.py - ścieżki do poszczególnych podstron sekcji głównej
    - static
      - css
        - inputs.css - styl dla inputów
        - style.css - styl dla body i html wraz z tłem i nagłówkiem
      - img
        - favicon.ico
        - images (.jpg, .png)
     - __init__.py - połączenie blueprintów z aplikacją
     - const_vars.py - stałe zmienne używane w aplikacji

# 3. Obrazy aplikacji
## Home Page
![home_page](https://github.com/KrissB99/Task-Manager/assets/77814273/277d8203-b868-48d9-9f3a-5bd619734a44)

## Register Page
![register_page](https://github.com/KrissB99/Task-Manager/assets/77814273/ffcaff7b-9f7e-4bc6-9d6a-6a6200a03056)

## Login Page
![login_page](https://github.com/KrissB99/Task-Manager/assets/77814273/11ceeac9-981a-4d60-be31-b2a1dc141082)

## Dashboard 
![dashboard_page](https://github.com/KrissB99/Task-Manager/assets/77814273/954139c6-02c8-4f1f-a1ec-85491bc33fc6)

## User Panel 
![user_panel](https://github.com/KrissB99/Task-Manager/assets/77814273/860320bd-6a99-4971-bc64-9d28cb43faba)

## Admin section (to be continued)

