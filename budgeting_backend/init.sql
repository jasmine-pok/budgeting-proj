DO $$ BEGIN
    IF NOT EXISTS (
        SELECT FROM pg_catalog.pg_database WHERE datname = 'budgeting_app'
    ) THEN
        CREATE DATABASE budgeting_app;
    END IF;
END $$;
