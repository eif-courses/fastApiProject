#
FROM python:3.9

#
WORKDIR /fastApiProject

#
COPY ./requirements.txt /code/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /fastApiProject/requirements.txt

#
COPY ./fastApiProject /code/fastApiProject

#
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
