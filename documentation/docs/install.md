# Install

## Requirements

This project is made on a
[Raspberry Pi Model
3](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/ "Raspberry Pi 3")
 with the [Sense HAT](https://www.raspberrypi.org/products/sense-hat/ "Sense
Hat").
This project must work on all Raspberry Pi which can have a Sense HAT.

---

## Download

The first thing to do is to download the project source code.
To do that clone the remote or download a ZIP file on the
[GitHub repository](https://github.com/Keftcha/SenseHat-connected-clock "GitHub
repository").

---

## Project architecture

The project architecture is simple.  
```
.
|- clock/
|- docs/
|- documentation/
|- LICENSE
|- README
```

### The `clock` folder

The clock folder is where all the source code of the application is.

### The `docs` folder

The docs folder is the source code of the documentation generate by
[MkDocs](https://www.mkdocs.org/ "MkDocs site").

### The `documentation` folder

The documentation folder is the source code for the generation of the documentation by 
[MkDocs](https://www.mkdocs.org/ "MkDocs site").

### The `LICENSE` file

The LICENSE file is the liscense of the project.  
You can read it [here](license.md "LICENSE").

### The `README` file

The README file is the readme of the project.

---

## Setup

The app is in the `clock` folder. You have to go in that folder.

First you have to install dependencies. To do that, run:
```bash
pip install -r requirements.txt
```

---

## Launch

To launch an app, you can execute each python file.
Each one do dirrerents feature, to know how to use them, go to the [Usage
page](usage.md "Usage")
