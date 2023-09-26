FROM python:3.11
WORKDIR /
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY alembic.ini /
COPY /src ./src
