FROM python:3.11.3

ENV PATH="/root/.local/bin:${PATH}"
COPY . /notification_job
WORKDIR /notification_job

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root

CMD python main.py