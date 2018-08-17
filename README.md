# rescuekerala

Website for coordinating rehabilitation of people affected in the 2018 Kerala Floods

Join our slack channel

https://join.slack.com/t/keralarescue/shared_invite/enQtNDE4NzUyNjg4MjQ3LTJiMDU0ZmFhODNlNDE3ZDc4ZmFlMGI0YmQ0MzI0NWYyNThlOTgwYTM2Y2JlYzMxMDMxMzUwY2E2MmVmNDQyNmE


# Kerala Rescue

Website for coordinating rehabilitation of people affected in the 2018 Kerala Floods

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need to have following softwares in your system

- Python 3
- Postgres
- git

### Installing

Setting up development environment

create database and user in postgres for kerala rescue and give privileges

```
psql user=postgres
Password:
psql (10.4 (Ubuntu 10.4-0ubuntu0.18.04))
Type "help" for help.

postgres=# CREATE DATABASE rescuekerala;
CREATE DATABASE
postgres=# CREATE USER rescueuser WITH PASSWORD 'password';
CREATE ROLE
postgres=# GRANT ALL PRIVILEGES ON DATABASE rescuekerala TO rescueuser;
GRANT
postgres=# \q

```
Clone the repo
```
git clone https://github.com/IEEEKeralaSection/rescuekerala.git
cd rescuekerala
```

Copy sample environment file and configure it as per your local settings

```
cp .env.example .env
```

If you cant copy the environment or is facing difficulty in starting the server , Copy the settings file from
https://github.com/vigneshhari/keralarescue_test_settings for local testing

Install dependencies

```
pip3 install -r requirements.txt
```

Run Database migrations

```
python3 manage.py migrate
```

Setup staticfiles
```
python3 manage.py collectstatic
```

Run the server

```
python3 manage.py runserver
```
Now open localhost:8000 in the browser

## How can you help?

### By testing

We have a lot of [Pull Requests](https://github.com/IEEEKeralaSection/rescuekerala/pulls) that requires testing. Pick any PR you like, try to reproduce the original issue and fix. Also join `#testing` channel in our slack and drop a note that you
are working on it.

### By fixing bugs or by adding features

Please find issues that we need help [here](https://github.com/IEEEKeralaSection/rescuekerala/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22). Go through the comments in the issue to check if someone else is already working on it. Don't forget to drop a comment when you start working on it.
