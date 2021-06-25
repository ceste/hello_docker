FROM python:3

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

RUN python app.py

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]
