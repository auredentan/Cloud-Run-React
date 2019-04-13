FROM nginx:alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY build /usr/share/nginx/html
COPY docker-entrypoint.sh /
RUN chmod +x docker-entrypoint.sh


ENTRYPOINT [ "/docker-entrypoint.sh" ]
CMD ["nginx", "-g", "daemon off;"]
