### Run App

```
. env/Scripts/activate
cd footie
python manage.py runserver
```

### Migration
```
python manage.py makemigrations player
python manage.py makemigrations game

python manage.py migrate

```
#### To see mgiration in sql format
```
python manage.py sqlmigrate game 0001
```