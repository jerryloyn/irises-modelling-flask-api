FROM python:3.6
COPY ./requirements.txt /requirements.txt
RUN pip install -r ./requirements.txt
WORKDIR /app
COPY . /app
RUN python train_model.py
ENTRYPOINT [ "python" ]
CMD ["app.py"]