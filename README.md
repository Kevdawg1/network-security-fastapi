
<a id="readme-top"></a>

[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Kevdawg1/slack-chatbot-deepseek">
<<<<<<< HEAD
    <img src="https://cdn.freebiesupply.com/logos/large/2x/slack-logo-icon.png" alt="Logo" width="80" height="80">
    <img src="https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/deepseek-logo-icon.png" alt="Logo" width="80" height="80">
    <img src="https://registry.npmmirror.com/@lobehub/icons-static-png/latest/files/light/ollama.png" alt="Logo" width="80" height="80">
=======
    <img src="https://miro.medium.com/v2/resize:fit:908/1*w4N8NNxnCo-qhADUe5BsGQ.png" alt="Logo" width="80" height="80">
    <img src="https://6104926.fs1.hubspotusercontent-na1.net/hubfs/6104926/Imported_Blog_Media/Amazon%20ec2.png" alt="Logo" width="80" height="80">
    <img src="https://upload.wikimedia.org/wikiversity/en/8/8c/FastAPI_logo.png" alt="Logo" width="80" height="80">
    <img src="https://dagshub.com/avatars/1440" alt="Logo" width="80" height="80">
    <img src="https://miro.medium.com/v2/resize:fit:512/1*doAg1_fMQKWFoub-6gwUiQ.png" alt="Logo" width="80" height="80">
>>>>>>> 3003ba2c182f056aaad4f06fe3b1563857506767
  </a>

  <h3 align="center">Network Security Projects For Phishing Data</h3>

  <p align="center">
    Detect suspicious phishing from network data.
    <br />
    <a href="https://github.com/Kevdawg1/network-security-fastapi"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Kevdawg1/network-security-fastapi">View Demo</a>
    &middot;
    <a href="https://github.com/Kevdawg1/network-security-fastapi/issues/new?template=bug_report.md">Report Bug</a>
    &middot;
    <a href="https://github.com/Kevdawg1/network-security-fastapi/issues/new?template=feature_request.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#acknowledgments">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This end-to-end project aims to showcase a complete MLOPs architecture to determine if network data received has indications of malicious intent or phishing. It includes ETL pipelines, model implementation and hyperparameter tuning, and CI/CD pipelines.

Data is extracted as a CSV file from a web source, transformed into a JSON format, and is loaded to a No-SQL database in MongoDB Atlas. 

This project contains an implementation of GridSearch training of multiple models with hyperparameter tuning to obtain the best performing model. The results of each model training run will be tracked in MLFlow on Dagshub (https://dagshub.com/kevinkamzw/network-security). The app runs on FastAPI which is used to trigger the training and prediction pipelines. 

This project contains CI/CD pipelines by publishing public Docker containers which will be uploaded into AWS ECR using GitHub Actions and deployed to an AWS EC2 instance. 

This project also comes with a full suite of custom logging and exception handlers for precise troubleshooting. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [![Python][Python]][Python]
* [![Conda][Conda]][Conda]
* Dagshub / MLFlow
* MongoDB Atlas

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* python
  ```sh
  python -m pip install --upgrade pip
  ```
* AWS CLI (See: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)


### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Clone the repo
   ```sh
   git clone https://github.com/Kevdawg1/network-security-fastapi.git
   ```
2. Create virtual environment
   ```sh
   conda create -p venv python==3.11
   ```
3. Install requirements
   ```sh
   pip install -r requirements.txt
   ```
4. Configure environment variables in a .env file
   ```
   MONGO_DB_URL="mongodb+srv://<username>:<password>@cluster1.******.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"
   ```
5. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin github_username/repo_name
   git remote -v # confirm the changes
   ```

### Setup MongoDB database

1. Log in or sign up on MongoDB Atlas (https://www.mongodb.com/lp/cloud/atlas/try4-reg)
2. Create a new cluster - select a free tier setting
3. Select AWS as the server provider
4. Create a database user and save the password for later
5. When configuring the MongoDB Driver, select `Python` with a version of `3.6 or later`.
6. When the cluster has been deployed, click the `Connect` button and expand and copy the connection string. 
7. Replace the password in the connection string with the saved password. 

### Setup Dagshub repository and MLFlow experiments

1. Log in or sign up on Dagshub (https://dagshub.com/)
2. Connect to your repository in Github that is hosting this project.

### Setup AWS ECR

1. Create a private repository in AWS ECR, keeping the default settings
2. Copy the repository URI to use in the next step.

### Setup GitHub Secrets

To keep keys and secrets secure in GitHub Actions, you will need to set up the following secrets in your GitHub project settings: 

   ```
   AWS_ACCESS_KEY_ID=

   AWS_SECRET_ACCESS_KEY=

   AWS_REGION = ap-southeast-2

   AWS_ECR_LOGIN_URI = 788614365622.dkr.ecr.us-east-1.amazonaws.com/networkssecurity
   ECR_REPOSITORY_NAME = networkssecurity
   ```

### Setup AWS EC2 instance

1. Create an EC2 instance with the following settings: 
    * OS: Ubuntu - Free tier
    * Instance Type: t2.medium 
    * Allow HTTPS traffic from the internet: enabled ✅
    * Allow HTTPS traffic from the internet: enabled ✅
2. Connect to the EC2 instance using EC2 Instance Connect
3. Run the following commands in EC2: 
    * Optional:
    ```
    sudo apt-get update -y
    sudo apt-get upgrade
    ```
    * Required: 
    ```
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker ubuntu
    newgrp docker
    ```

### Setup GitHub Self-Hosted Runner

1. In your project settings in GitHub, navigate to Actions > Runners. 
2. Click `New self-hosted runner` and select Linux
3. Follow the instructions and copy and paste the commands into your EC2 instance. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

### Python Application

To start the app locally, simply use the command below. If any changes are made, you will need to stop the program from running and restart it to see the changes applied. 

```sh
  python app.py
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

README.md template from https://github.com/othneildrew/Best-README-Template/blob/main/README.md 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/kevin-kam-eng
[Python]: https://img.shields.io/pypi/pyversions/slack_bolt?style=for-the-badge&logo=python
[Python-url]: https://www.python.org/downloads/
[Conda]: https://img.shields.io/conda/d/conda-forge/python?style=for-the-badge&logo=anaconda
[Conda-url]: https://docs.anaconda.com/anaconda/install/
