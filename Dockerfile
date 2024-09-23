FROM python:3.12

WORKDIR /app/

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app/

RUN find . -path "*/migrations/*.py" ! -name "__init__.py" -delete

ENV DJANGO_SETTINGS_MODULE=pictures.settings