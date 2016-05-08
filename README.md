# spark-vs-dataflow
Demo code contrasting Google Dataflow (Apache Beam) with Apache Spark

## Setup
Fairly self-contained instructions to run the code in this repo
on an Ubuntu machine or Mac.

### Virtual Envirnment

Start by installing and activing a virtual environment.

if you don't have pip,
curl -sSL https://bootstrap.pypa.io/get-pip.py > get-pip.py
sudo python get-pip.py

sudo pip install virtualenv
cd spark-vs-dataflow/
virtualenv venv
source venv/bin/activate

### SciPy
sudo apt-get install -y python-numpy python-scipy python-matplotlib

### Jupyter and SciPy
(With the virtual env running)
sudo apt-get install -y build-essential python-dev
pip install jupyter

### Apache Spark

If you don't have it already install Spark,
You can get from here:
http://spark.apache.org/downloads.html
If you're using AWS or GCP, it's pretty easy,
see: http://docs.aws.amazon.com/ElasticMapReduce/latest/DeveloperGuide/emr-spark-launch.html
and: https://cloud.google.com/dataproc/create-cluster
for demo purposes, you can dev on the master node :)

Be sure to set SPARK_HOME after it's installed, e.g.,
SPARK_HOME=/usr/lib/spark/
export SPARK_HOME

### Google Dataflow
(With the virtual env running)
pip install https://github.com/GoogleCloudPlatform/DataflowPythonSDK/archive/v0.2.3.tar.gz


### Project-specific setup
Set SRC_DIR to the source directory, e.g.,
SRC_DIR=~/git-projects/spark-vs-dataflow/src
export SRC_DIR

