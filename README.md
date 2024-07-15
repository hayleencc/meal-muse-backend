# Meal Muse: A sharing food app

## Backend Repository

### Autogenerate Migrations
This repository uses Alembic to manage database migrations. To autogenerate a migration, run the following command:
```bash
alembic revision --autogenerate -m "<migration message>"
```

And to apply the changes to the database, run:
```bash
alembic upgrade head
```