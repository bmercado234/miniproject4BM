<!--- (10/10 points) There should be a README.md file in your project that explains what 
your project is, how to install the pip requirements, and how to execute the program. 
Please use the GitHub flavor of Markdown. Be thorough on the explanations. 
You will need to explain the steps of initializing the database and then how to run the 
development server for your project. --->


# Mini Project 4

Fourth little project assigned in my INF601 - Advanced Programming with Python
class. Utilizes Django in creating web applications.


## Description

Program creates a small web application testing out basic features of django and bootstrap. 
Web application contains login, register, and form pages. Has proper GET and POST routes setup. 

## Getting Started

### Dependencies

*  Packages: django, sqlite3

<!--- (5/5 points) Proper import of packages used. --->

<!--- (5/5 points) I will be checking out the master branch of your project. 
Please be sure to include a requirements.txt file which contains all the packages that need installed. 
You can create this fille with the output of pip freeze at the terminal prompt. --->

### Installing

* Pip install
  * Please run the following
```
pip install -p requirements.txt
```

### Initializing the Database
In a terminal window, please type the following:
```
python manage.py makemigrations
```


### Applying Migirations
In a terminal window, please type the following:
```
python manage.py migrate
```

### Creating the Admin
In a terminal window, please type the following:
```
python manage.py createsuperuser
```


## Author

* Braulio Mercado  
  * b_mercado@mail.fhsu.edu

## Version History

* 0.1
    * Initial Release

## Acknowledgments

* [Jason Zeller](https://www.youtube.com/@profzeller)
