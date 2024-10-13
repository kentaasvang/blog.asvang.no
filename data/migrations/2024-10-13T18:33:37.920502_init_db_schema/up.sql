
CREATE TABLE post (
    -- id is a UUID and must be handles in the application layer
    id TEXT PRIMARY KEY NOT NULL,
    title TEXT NOT NULL,
    content TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP NOT NULL,
    -- update at is updated automatically by trigger
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP NOT NULL,
    -- status_id defaults to the first status in post_status
    status_id INTEGER DEFAULT 0 NOT NULL,
    user_id TEXT NOT NULL,

    -- foreign keys
    FOREIGN KEY (status_id) REFERENCES post_status(id),
    FOREIGN KEY (user_id) REFERENCES user(id)
);


-- Trigger to update post.updated_at when a post is updated
CREATE TRIGGER update_post_updated_at UPDATE ON post
BEGIN
    UPDATE post SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;


CREATE TABLE post_status (
    id INTEGER PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    description TEXT
);


CREATE TABLE user (
    id TEXT PRIMARY KEY NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);


CREATE TABLE user_role (
    id TEXT PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    user_id TEXT NOT NULL,

    -- foreign keys constraints
    FOREIGN KEY (user_id) REFERENCES user(id)
);
