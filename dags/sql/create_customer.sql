  CREATE TABLE IF NOT EXISTS customers (
            customer_id SERIAL PRIMARY KEY,
            customer_name VARCHAR(100) NOT NULL,
            address VARCHAR(255) NOT NULL,
            birth_date DATE NOT NULL
        );