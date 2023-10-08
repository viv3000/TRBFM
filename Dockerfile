FROM python:3.11
# set work directory
WORKDIR src/
# install dependencies
RUN source ../bin/activate
RUN pip install --user pytelegrambotapi
# run app
CMD ["python", "main.py"]
