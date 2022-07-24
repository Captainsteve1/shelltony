FROM ubuntu:20.04

WORKDIR /usr/src/app

ENV DEBIAN_FRONTEND="noninteractive" \
    LANG="en_US.UTF-8" \
    LANGUAGE="en_US:en" \
    LC_ALL="en_US.UTF-8"


RUN chmod 777 /usr/src/app \
    && apt-get -y update && apt-get -y upgrade \
    && apt-get install -y software-properties-common \
    && apt-get install -y python3 python3-pip python3-lxml \
    curl ffmpeg locales git p7zip-full p7zip-rar xz-utils unzip nano \
    && locale-gen en_US.UTF-8

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["bash", "start.sh"]