#
FROM python:3.9

#
WORKDIR /custom

#
COPY ./requirements.txt /custom/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /custom/requirements.txt

#
COPY ./fastApiProject /custom/fastApiProject

#
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
