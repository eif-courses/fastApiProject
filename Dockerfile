#
FROM python:3.9

#
WORKDIR /fastApiProject

#
COPY ./requirements.txt /fastApiProject/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /fastApiProject/requirements.txt

#
COPY ./app /fastApiProject/app

#
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
