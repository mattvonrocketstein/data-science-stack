<table>
  <tr><td>dsnb</td><td style="text-align:right">
    <a href=#Preqrequisites>Preqrequisites</a> |
    <a href=#features>Features</a> |
    <a href=#running-the-code>Running the Code</a>
    </td>
  </tr>
  <tr>
    <td width=15%>
      <img src=img/stack.png style="width:50px"></td>
    <td>Data Science Notebook Template</td>
  </tr>
</table>

## About

This project is one part playground, one part project skeleton, derived from the jupyter [allspark stack](https://github.com/jupyter/docker-stacks/tree/master/all-spark-notebook),
plus [these](http://drivendata.github.io/cookiecutter-data-science/#directory-structure)
guidelines for standardizing data science project layouts.

## Preqrequisites

You really just need docker and [docker-compose](https://docs.docker.com/compose/install/).  

If you're having problems, you might be interested to know my version info which is at least confirmed working:

        $ docker --version
        Docker version 17.03.1-ce, build c6d412e

## Features

So what's in the box?  Well, obviously everything already shipping with allspark:

-   Everything in the allspark box:
-   Jupyter Notebook,
-   Python 2 and 3, scipy, numpy, pandas
-   Scala,
-   R, Spark
-   lots more

Besides that you get:

-   A [Dockerfile](Dockerfile), used by docker-compose.  Mods on top of allspark are:
    -   preconfigured to install local [requirements](requirements.txt)
    -   preconfigured to use SSL and authentication
    -   preconfigured to enable plugins like [jupyter_dashboards](http://jupyter-dashboards-layout.readthedocs.io/en/latest/getting-started.html)
-   A [docker-compose.yml](docker-compose.yml) to reduce painful command-line invocations.  Includes
    -   a jupyter service built from dockerfile, preconfigured with volume for working directory & port forwarding
    -   a mesos service (not finished yet), ready for mesos client connection from allspark
-   various jupyter notebook demos & PoCs I've found useful
    -   graph ops and visualization [networkx](https://networkx.github.io/)
    -   csv loading/summarizing/graphing with [pandas](http://pandas.pydata.org/)
    -   images with [IPython.display](http://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html) and [PIL](http://www.pythonware.com/products/pil/)

## Running the Code

Use `docker-compose up dsnb` to bring up the notebook service.  If you make changes to the Dockerfile, add requirements, etc, you'll want to use `docker-compose up --force-recreate --build dsnb`
