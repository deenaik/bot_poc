FROM rasa/rasa:1.4.1-full

SHELL ["/bin/bash", "-c"]

ENV RASA_NLU_DOCKER="YES" \
    RASA_NLU_HOME=/app \
    RASA_NLU_PYTHON_PACKAGES=/usr/local/lib/python3.6/dist-packages

WORKDIR ${RASA_NLU_HOME}

USER root
RUN pip install --upgrade pip
RUN pip install joblib
RUN pip install chatterbot --no-deps
RUN pip install mathparse
RUN pip install pint
RUN pip install nltk
RUN mkdir /nltk_data
RUN chmod 777 -R /nltk_data
RUN pip install chatterbot_corpus --no-deps
USER 1001

COPY . ${RASA_NLU_HOME}

COPY slack.py /build/lib/python3.6/site-packages/rasa/core/channels/slack.py

EXPOSE 5005

CMD ["run", "--verbose", "--debug", "--enable-api"]
