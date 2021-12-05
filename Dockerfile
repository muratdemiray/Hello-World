FROM python:alpine
COPY ./app /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 3000
CMD python ./app.py