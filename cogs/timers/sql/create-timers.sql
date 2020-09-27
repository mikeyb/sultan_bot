CREATE TABLE Timers (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    userId TEXT NOT NULL,
    endTime INTEGER NOT NULL,
    type CHAR(1) NOT NULL REFERENCES TimerType(type)
);

CREATE TABLE TimerType (
    type char(1) PRIMARY KEY NOT NULL,
    seq INT
);

INSERT INTO TimerType (type, seq) VALUES ('A', 1);
INSERT INTO TimerType (type, seq) VALUES ('C', 2);
INSERT INTO TimerType (type, seq) VALUES ('H', 3);
