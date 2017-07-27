FROM jupyter/all-spark-notebook
ADD requirements.txt /
RUN pip install -r /requirements.txt
RUN jupyter nbextension install --py jupyter_dashboards --sys-prefix
RUN jupyter nbextension enable --py jupyter_dashboards --sys-prefix
