FROM nginx:latest

COPY nginx.conf /etc/nginx/nginx.conf
COPY custom_nginx.conf /etc/nginx/conf.d/

RUN mkdir -p /etc/nginx/sites-enabled/ \
    && ln -sf /etc/nginx/conf.d/custom_nginx.conf /etc/nginx/sites-enabled/

CMD ["nginx", "-g", "daemon off;"]
