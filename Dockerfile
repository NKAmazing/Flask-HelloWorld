FROM python:3.10-slim-bullseye AS production

WORKDIR /home/app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY ./app.py /home/app/

COPY ./entrypoint.sh ./entrypoint.sh
RUN chmod +x /home/app/entrypoint.sh

EXPOSE 5000

CMD ["/home/app/entrypoint.sh"]