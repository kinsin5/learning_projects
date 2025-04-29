CREATE TABLE countries (
	id SERIAL,
	name VARCHAR(100) UNIQUE,
	cca3 CHAR(3),
	capital VARCHAR(100),
	region VARCHAR(20) CHECK (region IN 
	('Africa', 'Oceania', 'Europe', 'Americas', 'Asia', 'Antarctic')),
	openstreetmaps VARCHAR,
	population INTEGER,
	area DECIMAL,
	flags VARCHAR
)

CREATE TABLE logs(
	id SERIAL,
	operation VARCHAR,
	create_at TIMESTAMP
)

ALTER TABLE countries
ADD COLUMN created_at TIMESTAMP DEFAULT now(),
ADD COLUMN updated_at TIMESTAMP DEFAULT now();

UPDATE countries 
SET population = 37950803 
WHERE name = 'Poland';

SELECT * FROM logs
WHERE id = (SELECT MAX(id) FROM logs);

CREATE OR REPLACE FUNCTION trig_procedure() RETURNS TRIGGER AS 
$$
BEGIN
	INSERT INTO logs (operation, create_at)
	VALUES (TG_OP || ' on ' || New.name, now());
RETURN NEW;
END;
$$ LANGUAGE PLPGSQL;

CREATE OR REPLACE TRIGGER trig_insertion_logs
AFTER INSERT OR DELETE OR UPDATE ON countries
FOR EACH ROW EXECUTE PROCEDURE trig_procedure();

UPDATE countries 
SET population = 37950804
WHERE name = 'Poland';
