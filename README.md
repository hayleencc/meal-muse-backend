# Meal Muse: A sharing food app
## Backend Repository
This is a project to share recipes with other people. At least for the MVP, the app will be allowed to create, edit, and delete recipes. 


## How to run the backend
1. Clone the repository:
```bash
git clone https://github.com/hayleencc/meal-muse-backend-v1.git
```

2. Create a virtual environment:
```bash
make create-env
```

3. Activate the virtual environment:

For MacOS/Linux:
```bash
source .venv/bin/activate
```

For Windows:
```bash
<path-to-env>\Scripts\activate
```

4. Install the dependencies:
```bash
make install
```

5. Create a `.env` file in the root directory of the project with the same variables in `.env.example`and ask the project owner for the real environment variables.

6. Run the backend and the database containers:
```bash
docker-compose up
```
If is the first time to build the containers, run the following command:
```bash
docker-compose up --build
```

If is the first time strting the database, run the following command:
```bash
make update-db
```
## How to run the tests
Run the following command:
```bash
make test
```

## Autogenerate Migrations
This repository uses Alembic to manage database migrations. To autogenerate a migration, run the following command:
```bash
alembic revision --autogenerate -m "<migration message>"
```

And to apply the changes to the database, run:
```bash
alembic upgrade head
```