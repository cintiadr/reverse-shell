FROM alpine:3.7

RUN apk add --no-cache python && rm -rf /var/cache/apk/*

COPY entrypoint.sh /entrypoint.sh
COPY client.py /client.py


RUN chmod a+x /entrypoint.sh
RUN chmod a+x /client.py

ENTRYPOINT ["/entrypoint.sh"]
