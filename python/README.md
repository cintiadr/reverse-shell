Copied from <https://null-byte.wonderhowto.com/how-to/reverse-shell-using-python-0163875/>

## Server

```
cd server/
docker build . -t reverse-shell-server-python
docker run -it -p 8888:8888 reverse-shell-server-python
```

## Client

```
cd client/
docker build . -t reverse-shell-client-python
docker run -itd reverse-shell-client-python
```
