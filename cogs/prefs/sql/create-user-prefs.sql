CREATE TABLE UserPrefs (
    id INT NOT NULL PRIMARY KEY,
    userId TEXT NOT NULL,
    timezone TEXT DEFAULT 'UTC'
);
