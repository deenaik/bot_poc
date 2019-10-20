FROM rasa/rasa:latest-full

SHELL ["/bin/bash", "-c"]

ENV RASA_NLU_DOCKER="YES" \
    RASA_NLU_HOME=/app \
    RASA_NLU_PYTHON_PACKAGES=/usr/local/lib/python3.6/dist-packages \
    ENT_URL=http://192.168.10.192:8080

WORKDIR ${RASA_NLU_HOME}

# RUN pip install "msgpack-numpy<0.4.4.0"

COPY . ${RASA_NLU_HOME}

EXPOSE 5005

CMD ["run", "--verbose", "--debug", "--enable-api"]
