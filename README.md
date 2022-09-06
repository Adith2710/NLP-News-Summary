![summarize-streamlit](https://user-images.githubusercontent.com/63020303/188521301-83a0f2bc-6740-4017-9b9f-13b3e892f184.png)

# AI based News Summarization
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/jkanner/streamlit-audio/main/app.py)

*built using python 3.9, docker, AWS EC2 and Github Actions*

To view app, click [HERE](http://3.90.16.8:8501/)

Models used:

Both models use summarization based models which were trained using different datasets on **BERT**.

* Summary Version 1: [Model used](https://huggingface.co/sshleifer/distilbart-cnn-12-6)
* Summary Version 2: [Model used](https://huggingface.co/sshleifer/distilbart-cnn-6-6)

## Running the App

### On Local System

* Create a virtual environment on local computer and install python 3.9 along with pip.
* Install docker according to your system requirements.
* Clone this github repo ```git clone git@github.com:Adith2710/NLP-News-Summary.git```
* Go to the repository folder ``` cd .../NLP-News-Summary```
* Build docker image (For Ubuntu- ```sudo docker image build .```)
* Once the image is built, get the image id ```sudo docker image ls```
* Run the docker container with the appropriate ports open ```sudo docker container run -p 8501:8501 -i <image-id> &``` 
* Once the container is run, open the link [http://localhost:8501/](http://localhost:8501/) to view the app

### Deploy App on the Internet

One of the easiest ways is to build a **heroku app** and connect the docker image to heroku. For this project, the storage and compute provided by heroku was not sufficient. Also, extra compute and storage on heroku had cost constraints. Thus this app will be run using **AWS** and the following shows how.

* Create an AWS account
* Create an AWS EC2 instance. The instance I used was ```AWS EC2 t2.medium compute``` system running Ubuntu 22.04.
* Install Docker engine. I followed this [tutorial](https://docs.docker.com/engine/install/ubuntu/)
* To check if docker is installed properly, run ```sudo docker run hello-world```.
* Clone this github repo ```git clone git@github.com:Adith2710/NLP-News-Summary.git```
* Go to the repository folder ``` cd .../NLP-News-Summary```
* Build docker image ```sudo docker image build .```
* Once the image is built, get the image id ```sudo docker image ls```
* Run the docker container with the appropriate ports open ```sudo docker container run -p 8501:8501 -i <image-id> &``` 
* Once the docker container is built, you can view your app on the url mentioned in the **External Network** URL.

**Note:** The app will run as long as the terminal window is kept open. In order to detach the session in order to run it independently, follow the steps provided in this [link](https://towardsdatascience.com/how-to-deploy-a-streamlit-app-using-an-amazon-free-ec2-instance-416a41f69dc3#:~:text=a%20very%20small%20problem%20though)

## Continuous Deployment Pipeline

This app was completely deployed using the automation tool *Github Actions*. The Automation script can be found in ```.github/workflows/CI.yml```. Most of the intial sections of the script are self-explanatory and can be found in many tutorials online. An explanation of the script is as follows
```
          script: |
            rm -rf NLP-News-Summary
            git clone git@github.com:Adith2710/NLP-News-Summary.git
            cd NLP-News-Summary
            sudo systemctl restart docker
            sudo docker system prune -a --volumes --force
            sudo docker image build .
```

- Line 1 - Removes any file/folder named "NLP-News-Summary". This is done to prevent unneccesarry memory issues.
- Line 2 - Clones this repo
- Line 3 - Go to the folder
- Line 4 - Restarts docker. This is done to stop all running docker containers and volumes. This is essential because, without stopping the docker images, we will not be able to delete all the docker files related to the older version.
- Line 5 - Deletes all docker images, containers and volumes. This cleans up memory. 
- Line 6 - Build docker image

**Note:** Running this script will not automatically change the output app to the newer version. We must go to the AWS EC2 instance command line and run the docker image to do so. This is done in order to prevent excess memory build up and also as stage of security before running the app. But all the errors (if any) till now, has been identified when running the CI.yml and not after.

## Liscence

[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)
