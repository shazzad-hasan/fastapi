CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    origin VERCHAR NOT NULL,
    destination VERCHAR NOT NULL,
    duration INTEGER NOT NULL
);