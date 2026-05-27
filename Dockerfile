FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
COPY Cube.jpg /usr/share/nginx/html/Cube.jpg
EXPOSE 80
