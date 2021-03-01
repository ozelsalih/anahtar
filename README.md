# anahtar
> [anahtar](https://anahtar.me) is a tool for generating all your passwords with a single masterpassword.
> _As it is still in development, it is not currently suitable for use._

## Table of contents
- [General info](#general-info)
- [Screenshots](#screenshots)
- [Self Hosted](#self-hosted)
- [Status](#status)
- [Inspiration](#inspiration)
- [Contact](#contact)

## General info
[anahtar](https://anahtar.me) is not a simple password generator. Generates passwords with hash algorithm using masterpassword, username and website information. The generated passwords can be accessed again by providing the same data. Thanks to hash algorithms, your masterpassword cannot be found based on the generated passwords. If the password on a website is stolen, your other passwords are not affected. To create a new password, you only need to change one of the inputs (e.g. password length).

## Screenshots
![Example screenshot](https://i.imgur.com/nErqB7U.png)

## Self Hosted
To use [anahtar](https://anahtar.me) on your local device, download the requirements from the `requirements.txt` file.  
  

`pip install -r requirements.txt`  
  

Then just run the file `wsgi.py` in the home directory.

## Status
Project is: _in progress_  


## Inspiration
Project inspired by [LessPass](https://github.com/lesspass/lesspass).

## Contact
Created by [@ozelsalih](mailto:salihozel.du@gmail.com?subject=anahtar%20Github) - feel free to contact me!
