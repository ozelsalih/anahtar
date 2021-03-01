# anahtar
> anahtar is a tool for generating all your passwords with a single masterpassword.
> As it is still in development, it is not currently suitable for use.

## Table of contents
- [anahtar](#anahtar)
- [General info](#general-info)
- [Screenshots](#screenshots)
- [Technologies](#technologies)
- [Self Hosted](#self-hosted)
- [Features](#features)
- [Status](#status)
- [Inspiration](#inspiration)
- [Contact](#contact)

## General info
anahtar is not a simple password generator. Generates passwords with hash algorithm using masterpassword, username and website information. The generated passwords can be accessed again by providing the same data. Thanks to hash algorithms, your masterpassword cannot be found based on the generated passwords. If the password on a website is stolen, your other passwords are not affected. To create a new password, you only need to change one of the inputs (e.g. password length).

## Screenshots
![Example screenshot](https://i.imgur.com/nErqB7U.png)

## Self Hosted
To use anahtar on your local device, download the requirements from the `requirements.txt` file.  
  

`pip install -r requirements.txt`  
  

Then just run the file `wsgi.py` in the home directory.

## Status
Project is: _in progress_  


## Inspiration
Project inspired by [LessPass](https://github.com/lesspass/lesspass).

## Contact
Created by [@ozelsalih](salihozel.du@gmail.com) - feel free to contact me!