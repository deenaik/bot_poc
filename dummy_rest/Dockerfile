FROM python:alpine

WORKDIR /app

COPY . .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

EXPOSE 80

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
