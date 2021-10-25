docker-compose -f f2.yaml down
h=$(docker images |grep adam | awk '{print $3}')
docker rmi $h
docker build --tag adamlahzami/python-docker:1.1 .

