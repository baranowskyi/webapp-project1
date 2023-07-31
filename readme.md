# SCcopy

Тестовый проект по созданию клона музыкального сайта с сохранением аналогичной функциональности.

### Стек 

* Django, Django Rest Framework, документация API (DRF Spectacular)
* HTML, CSS, JavaScript

### Внешние подключаемые компоненты

* Отображение формы звуковой волны с возможностью вопроизведения аудио [wavesurfer.js](https://wavesurfer-js.org/)  
* Автоматическая установка цвета фона аудио проигрывателя в зависимости от цвета обложки [color-thief.js](https://lokeshdhakar.com/projects/color-thief/) 
* Иконки - **Font Awesome** (free) с интергацией в Django [fontawesomefree](https://fontawesome.com/docs/web/use-with/python-django)   

### Настройки проекта

Настройки загружаемого медиа контента находятся в файле **webapp/core/service_functions/constants.py**  
В нём задаются максимально допустимые значения загружаемых файлов и имена файлов по умолчанию.

``` python
AVATAR_SIZE_LIMIT = 3 # max size in MB
DEFAULT_AVATAR = 'default_logo_artist.png' # path www.site.com/media/

HEADER_SIZE_LIMIT = 10 # max size in MB
DEFAULT_HEADER = 'default_header_artist.png' # path www.site.com/media/

COVER_SIZE_LIMIT = 5 # max size in MB
DEFAULT_COVER = 'default_logo_artist.png' # path www.site.com/media/

TRACK_SIZE_LIMIT = 200 # max size in MB
```

Настройки Django проекта находятся в файле **.env**

``` python
DEBUG=False # debug mode (false in default) 
ALLOWED_HOSTS=localhost 127.0.0.1 [::1] # allowed hosts
SECRET_KEY=django-insecure-q7sr@&2wsdoxpppp$$4555cv67785%7&^* # Django secret key
DB_ENGINE=django.db.backends.postgresql # name an engine database in Django format
DB_HOST=localhost # database host
DB_PORT=5432 # database port
DB_NAME=base # database name
DB_USER=username # database username
DB_PASS=password # database password
TZ=Europe # time zone
PGDATA=/var/lib/postgresql/data # database storage path
```