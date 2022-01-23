-- upgrade --
CREATE TABLE IF NOT EXISTS "automobilemodel" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "model" VARCHAR(64) NOT NULL,
    "manufacturer" VARCHAR(64) NOT NULL,
    "type" VARCHAR(64) NOT NULL
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" JSONB NOT NULL
);
