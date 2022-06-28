FROM python:3.8
COPY . /test
WORKDIR /test
ARG maxn=23
CMD [ "python", "./scratch_1.py"]

EXPOSE 8080
