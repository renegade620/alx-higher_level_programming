-- list all records except those without a name value
SELECT `score`, `name` FROM `second_table` WHERE `name` != "" ORDER BY `score`
DESC;
