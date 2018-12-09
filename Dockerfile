FROM python:3

WORKDIR /usr/src/app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

ENV PORT 80
CMD [ "python", "./app.py" ]

EXPOSE 80
