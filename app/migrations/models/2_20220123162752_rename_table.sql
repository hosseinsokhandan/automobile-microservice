-- upgrade --
ALTER TABLE "automobilemodel" RENAME TO "automobile";
-- downgrade --
ALTER TABLE "automobile" RENAME TO "automobilemodel";
