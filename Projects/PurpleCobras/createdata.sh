HOST_USER_ID=`id -u` HOST_GROUP_ID=`id -g` DJANGO_PORT=8000 docker-compose exec django \
                                                                       python manage.py makemigrations
HOST_USER_ID=`id -u` HOST_GROUP_ID=`id -g` DJANGO_PORT=8000 docker-compose exec django \
                                                                       python manage.py migrate
docker exec -it team-tutorial-project-purple-cobras_django_1 python3 manage.py loaddata sampledata.json
docker exec -it team-tutorial-project-purple-cobras_django_1 python3 manage.py createsuperuser
