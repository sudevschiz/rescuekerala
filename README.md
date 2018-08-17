# rescuekerala

Website for coordinating the rehabilitation of the people affected in the 2018 Kerala Floods.

[![Join Kerala Rescue Slack channel](https://i.imgur.com/V7jxjak.png)](https://join.slack.com/t/keralarescue/shared_invite/enQtNDE4NzUyNjg4MjQ3LTJiMDU0ZmFhODNlNDE3ZDc4ZmFlMGI0YmQ0MzI0NWYyNThlOTgwYTM2Y2JlYzMxMDMxMzUwY2E2MmVmNDQyNmE)

# Kerala Rescue

Website for coordinating rehabilitation of people affected in the 2018 Kerala Floods.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need to have following softwares in your system:

- Python 3
- Postgres
- git

### Installing

#### Setting up a development environment

1. Create database and user in postgres for kerala rescue and give privilegesl.

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

2. Clone the repo.
```
git clone https://github.com/IEEEKeralaSection/rescuekerala.git
cd rescuekerala
```

3. Copy the sample environment file and configure it as per your local settings.

```
cp .env.example .env
```

Note: If you cannot copy the environment or you're facing any difficulty in starting the server, copy the settings file from
https://github.com/vigneshhari/keralarescue_test_settings for local testing.

3. Install dependencies.

```
pip3 install -r requirements.txt
```

4. Run database migrations.

```
python3 manage.py migrate
```

5. Setup static files.
```
python3 manage.py collectstatic
```

6. Run the server.

```
python3 manage.py runserver
```
7. Now open localhost:8000 in the browser

## How can you help?

### By testing

We have a lot of [Pull Requests](https://github.com/IEEEKeralaSection/rescuekerala/pulls) that requires testing. Pick any PR that you like, try to reproduce the original issue and fix. Also join `#testing` channel in our slack and drop a note that you
are working on it.

### By fixing bugs or by adding features

Please find issues that we need help [here](https://github.com/IEEEKeralaSection/rescuekerala/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22). Go through the comments in the issue to check if someone else is already working on it. Don't forget to drop a comment when you start working on it.
