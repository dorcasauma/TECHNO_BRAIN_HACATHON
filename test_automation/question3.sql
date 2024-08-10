-- SQLite
CREATE TABLE users (
    UserId INTEGER PRIMARY KEY AUTOINCREMENT,
    Username TEXT UNIQUE NOT NULL,
    Email TEXT UNIQUE NOT NULL,
    Password TEXT NOT NULL,
    CreatedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- INSERT INTO users (Username, Email, Password, CreatedDate) VALUES ('john_doe', 'john@example.com', 'password123', '2024-05-25 10:00:00');
-- INSERT INTO users (Username, Email, Password, CreatedDate) VALUES ('jane_smith', 'jane@example.com', 'securepassword', '2024-08-30 12:30:00');
-- INSERT INTO users (Username, Email, Password, CreatedDate) VALUES ('alice_jones', 'alice@example.com', 'mypassword', '2024-08-05 15:45:00');


SELECT * FROM users WHERE CreatedDate >= DATE('now', '-30 days');