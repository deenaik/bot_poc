FROM rasa/rasa-sdk:latest

WORKDIR /app

COPY . action_server/.

RUN pip install --upgrade pip

EXPOSE 5055

CMD ["start", "--actions", "action_server.actions"]
