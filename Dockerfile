FROM ubuntu:latest

RUN apt update
RUN apt upgrade -y
RUN apt install -y tzdata

RUN apt install -y fonts-noto

RUN apt install -y python3-pip python3-cffi python3-brotli libpango-1.0-0 libharfbuzz0b libpangoft2-1.0-0

RUN apt autoremove
RUN apt clean

RUN pip install weasyprint
RUN pip install Jinja2

CMD weasyprint --info
