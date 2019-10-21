FROM python:alpine

WORKDIR /app

COPY . dummy_rest/.

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

EXPOSE 5055

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
