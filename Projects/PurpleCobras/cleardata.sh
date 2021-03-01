sudo rm -r data/*
HOST_USER_ID=`id --user` HOST_GROUP_ID=`id --group` DJANGO_PORT=8888 docker-compose up -d

