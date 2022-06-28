FROM python:3.8
COPY . /test
WORKDIR /test
CMD [ "python", "./scratch_1.py"]

EXPOSE 8080
