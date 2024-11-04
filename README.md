# GoNews 
This is a simple Google News Api. It's main goals is to receive related articles given a provided topic. 

## Table of Contents
- [GoNews Installation](#gonews-installation)
- [Browser Installation](#browser-installation)
- [Use of Examples](#use-of-examples)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## GoNews Installation 
Instructions on how to install and set up your project. For example:
```bash
git clone https://github.com/xhulio11/GoNews.git
cd GoNews
python install -r requirements.txt
```
## Browser Installation
Instructions on how to install and set up the browswer driver. 
Currently only chrome-driver is supported 

- Install Google Chrome if it is not already installed and create a simple profile 
- Donwnload according to your system the [chrome driver](https://googlechromelabs.github.io/chrome-for-testing/)
- Store it in a specific directory, open the driver and create a a simple profile

## Use examples 
In examples folder, 3 python scripts are provided to help you set up the projet easily 
- Windows User
  - Find path of the driver i.e: ```C:\\Users\\user\\OneDrive\\Desktop\\Thesis\\chromedriver-win64\\chromedriver.exe```
  - Find path of the profile i.e ```C:\Users\user\AppData\Local\Google\Chrome\User Data```
    - The above path can be found easily running in chrome ```chrome://version/``` and look at <b> Profile Path </b>
  - Set up the paths correctly in ```examples/windows_run.py``` as shown
    ```
       chrome_options.add_argument(r"--user-data-dir=C:\Users\user\AppData\Local\Google\Chrome\User Data")
       chrome_options.add_argument(r"--profile-directory=Profile 1") 
    ```
- Linux User
  - Find path of the driver i.e: ```/home/user/Downloads/chromedriver-linux64/chromedriver```
  - Find path of the profile i.e ```/home/user/.config/google-chrome/```
    - The above path can be found easily running in chrome ```chrome://version/``` and look at <b> Profile Path </b>
  - Set up the paths correctly in ```examples/windows_run.py``` as shown
    ```
       chrome_options.add_argument(r"--user-data-dir=/home/user/Downloads/chromedriver-linux64/chromedriver")
       chrome_options.add_argument(r"--profile-directory=Profile 1") 
    ```
