"""Initialize the database with required tables."""


def main():
    from backend.models.database import engine, Base
    Base.metadata.create_all(bind=engine)
    print("Database initialized successfully!")


if __name__ == "__main__":
    main()
