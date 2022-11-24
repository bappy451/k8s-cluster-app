FROM python:3.11.0

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system
# RUN python manage.py makemigrations && python manage.py migrate

COPY . /code/

EXPOSE 8000
CMD ["python","manage.py","runserver","0.0.0.0:8000"]