### Account Management System API - Beginning

This repository shows the beginning of me attempting to build an Account Management System using Python (Django).

The tools used in this repository:
 - Python
 - Django
 - Django-REST-Framework
 - Docker

#### Getting started

In order to start the project:

- Clone this Git repo locally
- Run the following in command-line:

```
docker-compose up
```

- The app will then be available on your docker host's default IP on port 8000.

#### Purpose

The idea behind this project is that this Account Management System should be able to:
- Register new users (players)
- Players can close their accounts
- Create new games (to which players can subscribe)
- Create new subscriptions
- Players can cancel subscriptions
- Restrict access to information, such that:
    - Players cannot see back-end reports.
    - Studios can see the popularity of their own games, but nobody elses.
    

#### State of play:
This project is incomplete (and very much at the beginning of its development cycle), it still needs further development in order for it to be ready for a production environment.

###### Current features:
- Create a user (/users/create)
- Authenticate users (/users/token)
- Create a new game (/api/games - POST)
- Retrieve all games (/api/games - GET)
- Persistent Storage (volumes)
- Containerised Application & Database

###### To be Added:
- Restrictions on who can create games (i.e, studios would be the ones who can release games to the platform - this would be determined by `account_type`).
- Functionality to add/alter subscriptions (Adding subscriptions would be allowed by Players, altering by both Studios and Players).
- CI/CD Deployment Pipeline
- Consideration of scaling (using Docker Swarm/K8s, or their cloud counterparts (ECS/EKS)).
- Productionisation considerations (for example, not having the `secret_key` explicitly in the `settings.py` file).

###### Data Model

The data model is defined in the diagram below:

![title](/Data_Model.PNG)

It's designed such that:

- We can manage permissions using the `account_type` field in the `user` table.
- Games (to be created by studio users) will always belong to a Studio.
- Subscriptions consist of both a Player and a Game (which can be created and updated).
- The structure is based a basic entity-relationship model and is easy to implement.
- Whether or not an account/subscription is active is determined by the `active_flag`.
- The keys are protected downstream on delete, which should allow us to preserve relationships for reporting purposes. 