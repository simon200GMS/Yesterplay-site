FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
COPY Bubble.jpg /usr/share/nginx/html/Bubble.jpg
COPY assets/ /usr/share/nginx/html/assets/
EXPOSE 80
