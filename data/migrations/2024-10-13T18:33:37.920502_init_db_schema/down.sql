-- Drop trigger first because it references the post table
DROP TRIGGER IF EXISTS update_post_updated_at;

-- Drop tables in reverse order to ensure foreign key constraints do not cause errors
DROP TABLE IF EXISTS user_role;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post_status;
DROP TABLE IF EXISTS post;

