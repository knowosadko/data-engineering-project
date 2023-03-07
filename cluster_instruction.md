# Instructions
Instructions for settin up the spark cluster for the project, based on the instructions found on:
https://phoenixnap.com/kb/install-spark-on-ubuntu

## 1. Launching VMs
On Snic Science cloud, launch one master VM and X amount of worker VMs 
(all using the flavor medium and Ubuntu 22.04 - 2023.01.07 and the created 
SSH key for the group. Add security group "spark-master" which allows 8080-connections

## 2. Installing required dependencies
Connect to master node, using associated floating ip. Run the following command:

sudo apt install default-jdk scala git -y

Verify the installed dependencies by running:

java -version; javac -version; scala -version; git --version

which should print the versions

## 3. Install Apache Spark
Find the link to the latest version of Spark on this website https://spark.apache.org/downloads.html. I the terminal, run

wget https://dlcdn.apache.org/spark/spark-3.3.2/spark-3.3.2-bin-hadoop3.tgz

(with spark-3.3.2 and hadoop3 being the latest releases at the time of writing this instruction)

Extract the spark archive with

tar xvf spark-*ls

Move the spark directory to opt/spark by running 

sudo mv spark-3.0.1-bin-hadoop2.7 /opt/spark

## 4. Configure spark environment
Add home paths to the user profile by running

echo "export SPARK_HOME=/opt/spark" &gt;&gt; ~/.profile
echo "export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin" &gt;&gt; ~/.profile
echo "export PYSPARK_PYTHON=/usr/bin/python3" &gt;&gt; ~/.profile

After adding, load the .profile file in the command line by running

source ~/.profile

## 5. Start Spark Master server
run start-master.sh

Run jps to see that a Master has been created

Go to floatingipofmasterVM:8080 which should show the Spark GUI

Start a worker node by running start-worker spark://nameofmasterVM:7070

