<a name="readme-top"></a>

<h3 align="center"> Align </h3>

  <p align="center">
    An online teaching platform to get education for everyone!
    <br />
    <a href="https://github.com/Tsangington/Align"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Tsangington/Align">View Demo</a>
    ·
    <a href="https://github.com/Tsangington/Align/issues">Report Bug</a>
    ·
    <a href="https://github.com/Tsangington/Align/issues">Request Feature</a>
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
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

https://align.onrender.com/

A solo starter project to understand website development and full-stack engineers. A teaching platform, with the ability to sign up, log in, log out, create a course, join a course, view other people's profiles.

* Website Architecture <br/>
![Website Architecture](https://user-images.githubusercontent.com/102903601/235075392-8a8ec66a-a85d-4122-802e-ceb9d822400f.png)<p align="right">(<a href="#readme-top">back to top</a>)</p>
* ERD <br/>
![ERD](https://user-images.githubusercontent.com/102903601/235108069-eb545b66-19db-4cf4-bd6c-e1b28d612fda.png)
* Landing Page (WIP) <br/>
![Landing Page (WIP)](https://user-images.githubusercontent.com/102903601/235075706-2338e833-2364-47ec-8ac7-a8269b09aec6.png)
* Sign Up Page <br/>
![Sign Up Page](https://user-images.githubusercontent.com/102903601/235075816-2baf4d5f-b42d-4379-80a2-aaa834c555f9.png)
* Login Page <br/>
![Login Page](https://user-images.githubusercontent.com/102903601/235075892-3a6b11af-e3e0-4fe5-8cce-c08fcc237b91.png)
* Styling <br/>
![Styling](https://user-images.githubusercontent.com/102903601/235075980-bd0016c1-a42b-4dff-961e-08629bf591dc.png)
* Dynamic <br/>
![dyanmic to fit the screen](https://user-images.githubusercontent.com/102903601/235076121-191b35c4-cc75-47da-a446-36319c0ae066.png)
* Alerts <br/>
![Alerts](https://user-images.githubusercontent.com/102903601/235108653-3518618b-454b-4cfa-8906-8066a793692b.png)


### Built With

* Flask
* SQLalchemy
* Python
* Jinja
* Render.com - Web hosting
* HTML
* CSS
* Javascript

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started



### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Installing requirements
  ```sh
  pip install -r requirements.txt 
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Tsangington/Align.git
   ```
2. Create a config.py file outside of the app folder, and use a development config, or use these values:
   ```sh
   class Config(object):
     SECRET_KEY = 'DEV_TEST_KEY_:D_BASED123456789'
     DEBUG = False
     TESTING = False
     SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    
   class DevelopmentConfig(Config):
     DEBUG = True
     SQLALCHEMY_DATABASE_URI = 'sqlite:///development.db'
     DB_NAME = "development-db"
     DB_USERNAME = "development.db"
   ```
3. Create a virtual environment:
   ```sh
   #Windows
   python -m virtualenv <venvName>
   #Mac
   virtualenv <venvName>
   ```
4. Enter the virtual environment:
   ```sh
   #Windows
   <venvName>\Scripts\activate
   #Mac
   source <venvName>/bin/activate
   
   #To Leave the venv:
   deactivate
   ```
5. Install the pre-requesites
   ```sh
   pip install -r requirements.txt 
   ```
6. To run the localhost,
   ```sh
   py main.py
   ```
7. Secret URLs
     ```sh
   align/user/<username> #searches for a user
   align/logout #logs out the current user
   align/createcourse #create a course
   align/join #see and join all available courses
   align/delete #deletes the current user from the database
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [ ] Course Privacy
- [ ] Landing Page
- [ ] Better Security

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

harry.tsang@code.berlin.com

Project Link: [https://github.com/Tsangington/Align](https://github.com/Tsangington/Align)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

