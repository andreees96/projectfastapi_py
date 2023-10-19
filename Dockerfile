###COMANDOS DE DOCKER###
FROM python:3.12

WORKDIR /projectfastapi_py
COPY requeriments.txt /projectfastapi_py/requeriments.txt

RUN  pip install --no-cache-dir --upgrade -r /projectfastapi_py/requeriments.txt

COPY . /projectfastapi_py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

