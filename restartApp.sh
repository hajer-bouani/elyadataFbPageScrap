docker-compose -f composeFile.yaml down
h=$(docker images |grep hajerbouani | awk '{print $3}')
docker rmi $h
docker build --tag hajerbouani/python-docker:1.2 .

