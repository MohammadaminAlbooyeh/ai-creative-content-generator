FROM nginx:alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY includes/ /etc/nginx/includes/
RUN mkdir -p /etc/nginx/certs
EXPOSE 80 443
