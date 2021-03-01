HOST_USER_ID=`id --user` HOST_GROUP_ID=`id --group` DJANGO_PORT=8888 docker-compose exec django \
                                                                       python manage.py makemigrations
HOST_USER_ID=`id --user` HOST_GROUP_ID=`id --group` DJANGO_PORT=8888 docker-compose exec django \
                                                                       python manage.py migrate
