# Instructions
Instructions for settin up the spark cluster for the project, based on the instructions found on:
https://medium.com/ymedialabs-innovation/apache-spark-on-a-multi-node-cluster-b75967c8cb2b

## 1. Launching VMs
On Snic Science cloud, launch one master VM and X amount of worker VMs 
(all using the flavor medium and Ubuntu 22.04 - 2023.01.07 and the created 
SSH key for the group.

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
