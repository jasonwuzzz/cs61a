CREATE TABLE IF NOT EXISTS  records AS
    SELECT "Ben Bitdiddle" AS name, "Computer" AS division, "Wizard" AS title,
        60000 AS salary, "Oliver Warbucks" AS supervisor UNION
    SELECT "Alyssa P Hacker", "Computer", "Programmer", 40000, "Ben Bitdiddle" UNION
    SELECT "Cy D Fect", "Computer", "Programmer", 35000, "Ben Bitdiddle" UNION
    SELECT "Lem E Tweakit", "Computer", "Technician", 25000, "Ben Bitdiddle" UNION
    SELECT "Louis Reasoner", "Computer", "Programmer Trainee", 30000, "Alyssa P Hacker" UNION
    SELECT "Oliver Warbucks", "Administration", "Big Wheel", 150000, "Oliver Warbucks" UNION
    SELECT "Eben Scrooge", "Accounting", "Chief Accountant", 75000, "Oliver Warbucks" UNION
    SELECT "Robert Cratchet", "Accounting", "Scrivener", 18000, "Eben Scrooge" UNION
    SELECT "Lana Lambda", "Administration", "Executive Director", 610000, "Lana Lambda";

CREATE TABLE IF NOT EXISTS  meetings AS
    SELECT "Accounting" AS division, "Monday" AS day, "9am" AS time UNION
    SELECT "Computer", "Wednesday", "4pm" UNION
    SELECT "Administration", "Monday", "11am" UNION
    SELECT "Administration", "Wednesday", "4pm";

CREATE TABLE IF NOT EXISTS  courses AS
    SELECT "John DeNero" AS professor , "CS 61A" AS course , "Fa17" AS semester UNION
    SELECT "Paul Hilfinger"           , "CS 61A"           , "Fa17" UNION
    SELECT "Paul Hilfinger"           , "CS 61A"           , "Sp17" UNION
    SELECT "John DeNero"              , "Data 8"           , "Sp17" UNION
    SELECT "Josh Hug"                 , "CS 61B"           , "Sp17" UNION
    SELECT "Satish Rao"               , "CS 70 "           , "Sp17" UNION
    SELECT "Nicholas Weaver"          , "CS 61C"           , "Sp17" UNION
    SELECT "Gerald Friedland"         , "CS 61C"           , "Sp17" UNION
    SELECT "John DeNero"              , "CS 61A"           , "Fa16" UNION
    SELECT "Paul Hilfinger"           , "CS 61B"           , "Fa16";
