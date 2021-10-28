FROM python:3.10-slim-buster

WORKDIR /app/

RUN pip install --upgrade pip
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["uvicorn", "SocialNow.asgi:application", "--host", "0.0.0.0"]