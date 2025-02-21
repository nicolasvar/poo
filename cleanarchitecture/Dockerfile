FROM python:3.12-bullseye
RUN apt-get update && apt-get install -y locales && sed -i -e 's/# es_ES.UTF-8 UTF-8/es_ES.UTF-8 UTF-8/' /etc/locale.gen && dpkg-reconfigure --frontend=noninteractive locales

ENV LANG es_ES.UTF-8
ENV LC_ALL es_ES.UTF-8

RUN pip install --upgrade pip && pip install --upgrade setuptools && pip install  poetry && pip install pyarrow
WORKDIR /usr/src/app
COPY pyproject.toml ./ 
COPY poetry.toml ./
#COPY README.md ./
COPY . .
RUN poetry install
EXPOSE 8000               
#ENV GUNICORN_CMD_ARGS="--bind=0.0.0.0 --chdir=./src/"
#COPY . .
CMD ["poetry","run","uvicorn", "cleanarchitecture.Program:program.app","--host", "0.0.0.0", "--port", "8000"]  
#CMD ["gunicorn", "adapter.rest.Program:program.app"]
#"--bind", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker",