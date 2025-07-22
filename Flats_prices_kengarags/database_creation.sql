create table kengarags_prices(
id SERIAL PRIMARY KEY,
    address TEXT,
    rooms integer,
    square_meters INTEGER,
	floor_ INTEGER,
	total_floors INTEGER,
	project TEXT,
	type_ TEXT,
	price INTEGER,
	price_per_m2 REAL,
	created_at DATE
    
)