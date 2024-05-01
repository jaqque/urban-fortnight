FROM debian:latest

RUN apt-get update \
 && apt-get install -y python3

WORKDIR /app
CMD ["/bin/bash"]
