FROM alpine:3.7
RUN apk add --update netcat-openbsd && rm -rf /var/cache/apk/*

COPY entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh

EXPOSE 8888

ENTRYPOINT "/entrypoint.sh"
