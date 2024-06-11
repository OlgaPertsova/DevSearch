# DevSearch

Учебный многостраничный сайт с аккаунтами разработчиков и их проектами. Предполагается что на сайте регистрируются разработчики, заполняют свой профиль, выкладывают свои проекты. А потенциальные заказчики просматривают профили и проекты, и могут не выходя с сайта связаться с разработчиком в его профиле. Также зарегистрированные пользователи могут оставлять комментарии под выложенными проектами и оценивать их по 100-бальной шкале. 

## Функции приложение projects

    def projects - выводит все добавленные проекты на главной странице
    def project - выводит подробную информацию об одном проекте по его id из БД
    def paginate_projects - пагинация страниц с проектами (на одной стр по три проекта)
    def search_projects - находит проекты с помощью фильтра из БД
    def create_project - создать новый проект (применяется декоратор login_required)
    def update_project - отредактировать проект (применяется декоратор login_required)
    def delete_project - удалить проект (применяется декоратор login_required)

## Функции приложение projects

    def register_user - регистрация профиля разработчика (CustomUserCreationForm)
    def login_user - авторизация 
    def logout_user - выход из профиля
    def profiles - выводит всех разработчиков на главной странице
    def user_profile - выводит информацию о разработчике для других пользователей
    def user_account - выводит всю информацию в профиле разработчика (применяется декоратор login_required)
    def edit_account - изменить профиль разработчика (применяется декоратор login_required)
    def create_skill - создать скилл в профиле разработчика (применяется декоратор login_required)
    def update_skill - изменить скилл (применяется декоратор login_required)
    def delete_skill - удалить скилл (применяется декоратор login_required)
    def inbox - выводит таблицу всех сообщений в профиле разработчика
    def view_message - выводит текст выбранного сообщения
    def create_message - отправка сообщений при помощи формы выбранному разработчику
    def paginate_profiles - пагинация страниц с профилями (на одной стр по три профиля) 
    def search_profiles - находит профили с помощью фильтра из БД

## Quickstart

Run the following commands to bootstrap your environment:

    sudo apt-get install -y git python-venv python-pip
    git clone https://github.com/OlgaPertsova/DevSearch.git
    cd devsearch

    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

    cp .env

Run the app locally:
    
    python manage.py runserver

Run the app docker:

    git clone https://github.com/OlgaPertsova/DevSearch.git
    cd devsearch
    docker build . --tag docker-devsearch
    docker images
    docker run -p 8004:8001 image_id/image_tag
    
