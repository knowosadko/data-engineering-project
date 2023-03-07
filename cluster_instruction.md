# Instructions
Instructions for settin up the spark cluster for the project, based on the instructions found on:
https://phoenixnap.com/kb/install-spark-on-ubuntu

## 1. Launching VMs
On Snic Science cloud, launch one master VM and X amount of worker VMs 
(all using the flavor medium and Ubuntu 22.04 - 2023.01.07 and the created 
SSH key for the group. Add security group "spark-master" which allows 8080-connections

## 2. Installing required dependencies (master and workers)
Connect to nodes, using associated floating ip. Run the following command:

sudo apt install default-jdk scala git -y

Verify the installed dependencies by running:

java -version; javac -version; scala -version; git --version

which should print the versions

## 2. Add entries in hosts file
Add the private IP adress with name of each VM in /etc/hosts, using sudo nano /etc/hosts
For this project it will look like:

127.0.0.1 localhost                

192.168.2.186 Group-14-Master
192.168.2.188 Group-14-Worker1
192.168.2.224 Group-14-Worker2

## 3. On Master only
In /opt/spark/conf, run cp spark-env.sh.template spark-env.sh

Then run: sudo nano spark-env.sh

and add at the bottom

export SPARK_MASTER_HOST='Master-IP'
export JAVA_HOME=Path_of_JAVA_installation
  
In our case:
export SPARK_MASTER_HOST=192.168.2.186
export JAVA_HOME = /usr/lib/jvm/java-11-openjdk-amd64

In /opt/spark/conf, create a file called slaves
sudo nano slaves

and add the name of the master and workers:

Group-14-Master
Group-14-Worker1
Group-14-Worker2

## 3. Configure SSH (master)
1) sudo apt-get install openssh-server openssh-client

2) ssh-keygen -t rsa -P ""
Press enter

3) Copy the content of .ssh/id_rsa.pub (of master) to .ssh/authorized_keys (of all the slaves as well as master).
4) Check if you can run ssh Group-14-Worker1 and Group-14-Worker2 on master. If it works, use exit to return to master VM


## 4. Install Apache Spark (master and workers)
Find the link to the latest version of Spark on this website https://spark.apache.org/downloads.html. I the terminal, run

wget https://dlcdn.apache.org/spark/spark-3.3.2/spark-3.3.2-bin-hadoop3.tgz

(with spark-3.3.2 and hadoop3 being the latest releases at the time of writing this instruction)

Extract the spark archive with

tar xvf spark-*

Move the spark directory to opt/spark by running 

sudo mv spark-3.0.1-bin-hadoop2.7 /opt/spark

## 5. Configure spark environment (master and workers)
Add home paths to the user profile by running

echo "export SPARK_HOME=/opt/spark" >> ~/.profile
echo "export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin" >> ~/.profile
echo "export PYSPARK_PYTHON=/usr/bin/python3" >> ~/.profile

After adding, load the .profile file in the command line by running

source ~/.profile

## 6. Start Spark Master server
run start-all.sh

Run jps to see that a Master and workers have been created

Go to floatingipofmasterVM:8080 which should show the Spark GUI

Start a worker node by running start-worker spark://localhost:7070

