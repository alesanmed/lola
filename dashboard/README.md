# COVID dashboard

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://frontend-alesanmed.cloud.okteto.net/)

This piece contains the dashboard. Made with [Streamlit](https://streamlit.io/).

# Table of contents

- [Running the code 🚂](#running-code)
  - [Installation 🎢](#installing)
  - [Configuration ⚙](#configuring)
  - [Execution 🎯](#running)
- [Pages](#pages)
  - [Identify your audio](#identify-audio)
  - [Data exploration](#data-exploration)
  - [Models evaluation](#models-evaluation)

## Running the code 🚂 <a name="running-code"></a>

If you want to run the dashboard from source, clone it.

```
git clone https://github.com/alesanmed-educational-projects/core-data-covid-project.git

cd core-data-covid-project/dashboard
```

### Installation 🎢 <a name="installing"></a>

First, install the dependencies using pip:

```
pip install -r requirements.txt
```

Or, if you use [Poetry](https://python-poetry.org/):

```
poetry install
```

### Configuration ⚙ <a name="configuring"></a>

The project looks for the following environment variables to configure several parts:

- BACK_URL: The URL where the backend is running

### Execution 🎯 <a name="running"></a>

Once you have installed the dependencies, you can bring the dashboard up:

```
streamlit run app/main.py
```

## Pages <a name="pages"></a>

### Identify your audio <a name="identify-audio"></a>

On this page, you can upload your mp3 file and get a prediction about the flamenco style.

Also, you will get some info about the style identified.

### Data exploration <a name="data-exploration"></a>

Here, you can find some charts exploring the different styles and their features.

### Models evaluation data <a name="models-evaluation"></a>

On this last page, there are metrics and charts about the performance of the different models.