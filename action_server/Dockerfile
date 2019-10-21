FROM rasa/rasa-sdk:latest

WORKDIR /app

COPY . action_server/.

RUN pip install --upgrade pip \
    && pip install -r action_server/requirements.txt --no-cache-dir

EXPOSE 5055

CMD ["start", "--actions", "action_server.actions"]
