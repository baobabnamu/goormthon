FROM nginx

WORKDIR /usr/share/nginx/html

COPY src ./
ADD test.sh /usr/local/bin/test.sh

RUN ["/bin/bash", "-c", "chmod +x /usr/local/bin/test.sh"]

ENTRYPOINT ["/usr/local/bin/test.sh"]
CMD ["1"]

EXPOSE 80