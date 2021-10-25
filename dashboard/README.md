# COVID dashboard

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://frontend-alesanmed.cloud.okteto.net/)

This piece contains the dashboard. Made with [Streamlit](https://streamlit.io/).

# Table of contents

- [Some screenshots 📸](#screenshots)
- [Running the code 🚂](#running-code)
  - [Installation 🎢](#installing)
  - [Configuration ⚙](#configuring)
  - [Execution 🎯](#running)
- [Pages](#pages)
  - [General data](#general-data)
  - [Country data](#country-data)
  - [Manage data](#manage-data)

## Some screenshots 📸 <a name="screenshots"></a>
![Cases per province](assets/cases_by_province.png)

![Spain map with cases info](assets/provinces_contributions.png)

![Evolution of cases](../assets/img/dashboard.png)

![World map with cases info](assets/img/worldmap.png)

## Running the code 🚂 <a name="running-code"></a>

If you want to run the dashboard from source, clone it and install the dependencies.

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

- BACK_URL: URL de la API de flask

### Execution 🎯 <a name="running"></a>

Once you have installed the dependencies, you can bring the dashboard up:

```
streamlit run app/main.py
```

## Pages <a name="pages"></a>

### General data <a name="general-data"></a>

This page shows general COVID data. You can find global cases, global charts as well as a map with rates per country.

You can also filter the data by countries and types, as well as the chart type.

### Country data <a name="country-data"></a>

This page is a per-country detailed page. It splits the data by provinces (states). You can export that page to PDF and also send it via email.

Again, you can filter by provinces, case type, and chart type.

### Manage data <a name="manage-data"></a>

This page allows creating new countries using an API key. The created data should be available right away in the dashboard.
