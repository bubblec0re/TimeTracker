FROM python:3.11-slim

WORKDIR /python-timetracker

COPY ./requirements.txt .

RUN pip install -r /python-timetracker/requirements.txt --no-cache-dir

COPY ./app /python-timetracker/app

COPY .env .

CMD ["python", "-u", "-m", "uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0"]