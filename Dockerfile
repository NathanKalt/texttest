FROM ubuntu:18.04
ENV TZ=Europe/Moscow
RUN apt-get -y update --fix-missing && apt-get -y upgrade
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
# RUN apt-get -y install python3 python-dev python3-dev \
#      build-essential libssl-dev libffi-dev \
#      libxml2-dev libxslt1-dev zlib1g-dev \
#      python-pip nano screen
# RUN apt-get install -y tzdata
RUN apt-get -y clean
RUN apt-get install -y language-pack-ru
ENV LANGUAGE ru_RU.UTF-8
ENV LANG ru_RU.UTF-8
ENV LC_ALL ru_RU.UTF-8
RUN locale-gen ru_RU.UTF-8 && dpkg-reconfigure locales
COPY requirements.txt requirements.txt
RUN apt-get update && apt-get install -y git && pip3 install --no-dependencies -r requirements.txt
COPY /textproc /textproc
WORKDIR /textproc
CMD ["python3", "app/routes.py"]