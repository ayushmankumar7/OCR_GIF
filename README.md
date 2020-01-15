# OCR_GIF

This is a sample project for extracting texts from a GIF and other images too.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Python3
Virtual Environment
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

For Linux and MacOS
```
pip3 install virtualenv
virtualenv ORCtesse
source ORCtesse/bin/avtivate
pip3 install -r requirements.txt
```

For Windows

```
pip install virtualenv
virtualenv ORCtesse
ORCtesse\Script\activate
pip install -r requirements.txt
```
## Running the tests

For Linux and MacOS
```
python3 main.py
```
For Windows

```
python main.py
```

For using your custom image or GIF.

```
python3 main.py --i [ file name ]
```
Exmaple: 
```
python3 main.py --i textimg.png
```
## Built With

* [Python3](http://www.python.org) - The Programming Langauge used
* [Pytesseract](https://github.com/madmaze/pytesseract) - ORC Algorithm
* [Pillow](https://github.com/python-pillow/Pillow) - Image reading library




## Authors

* **Ayushman Kumar** - *Initial work* - [Ayushman Kumar](https://github.com/ayushmankumar7)


## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
