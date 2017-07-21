FROM jupyter/all-spark-notebook
#RUN pip install -r requirements.txt
ADD requirements.txt /
RUN pip install -r /requirements.txt
