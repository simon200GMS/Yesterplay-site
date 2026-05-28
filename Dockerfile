FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
COPY Cube.jpg /usr/share/nginx/html/Cube.jpg
COPY Bubble.jpg /usr/share/nginx/html/Bubble.jpg
EXPOSE 80
