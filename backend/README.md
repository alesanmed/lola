# LOLA-backend
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

This part holds the application backend. Here's where the magic happens 🏀.

# Table of contents

- [Running the code 🚂](#running-code)
  - [Pre-requisites 🛒](#pre-reqs)
  - [Installation 🎢](#installing)
  - [Execution 🎯](#running)
- [Endpoints 🛎](#endpoints)

## Running the code 🚂 <a name="running-code"></a>

If you want to run the backend from source, clone it.

```
git clone https://github.com/alesanmed-educational-projects/core-data-covid-project.git

cd core-data-covid-project/backend
```

### Pre-requisites 🛒 <a name="pre-reqs"></a>

- [ffmpeg](https://www.ffmpeg.org/)

### Installation 🎢 <a name="installing"></a>

First, install the dependencies using pip:

```
pip install -r requirements.txt
```

Or, if you use [Poetry](https://python-poetry.org/):

```
poetry install
```

### Execution 🎯 <a name="running"></a>

Once you have installed the dependencies, you can bring the server up:

```
FLASK_APP=lola-backend flask run
```

## Endpoints 🛎 <a name="endpoints"></a>

There is only one endpoint `[POST] /prediction`. This endpoint receives an mp3 file in a field called `file` with `form-data` format.