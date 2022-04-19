# csit314 eBay testing tool

This project is a python-based test suite for the search functionality of the [eBay sandbox](https://sandbox.ebay.com/).

## Contributing
In order to contribute to this project, clone the repo and set up your python 3.x environment.
It's recommended that you use a virtual environment, to avoid problems with polluting your system python.

### Setting up a virtual environment
From within the cloned repo, you can run this series of commands to kick up a new virtual environment and install the 
project's requirements:
```bash
# create and enter a new venv in the current directory
$ python -m venv venv
$ source venv/bin/activate
# install the project requirements to the venv
(venv) $ pip install -r requirements.txt
(venv) $ pip install -e .
# and when you're done you can deactivate it
$ deactivate
```