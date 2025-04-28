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

CREATE OR REPLACE FUNCTION trig_procedure() RETURNS TRIGGER AS 
$$
BEGIN
	INSERT INTO logs (operation, create_at)
	VALUES (TG_OP, now());
RETURN NEW;
END;
$$ LANGUAGE PLPGSQL;

CREATE TRIGGER trig_insertion_logs
AFTER INSERT OR DELETE ON countries
FOR EACH ROW EXECUTE PROCEDURE trig_procedure();

SELECT * FROM logs;
