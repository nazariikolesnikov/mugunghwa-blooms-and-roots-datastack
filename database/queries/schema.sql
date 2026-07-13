CREATE DATABASE muhunghwabloomsandrootsdb;
USE muhunghwabloomsandrootsdb;

CREATE TABLE customers (
    id SERIAL PRIMARY KEY, 
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now() 
);

CREATE TABLE customers_accounts (
    id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL REFERENCES customers(id) ON DELETE CASCADE,
    account_type VARCHAR(50) NOT NULL,
    wallet_balance NUMERIC(10, 2) NOT NULL DEFAULT 0 CHECK (wallet_balance >= 0),
    currency CHAR(3) NOT NULL DEFAULT 'USD',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);

CREATE TABLE customers_transactions (
    id BIGSERIAL PRIMARY KEY,
    account_id INT NOT NULL REFERENCES customers_accounts(id) ON DELETE CASCADE,
    transaction_type VARCHAR(50) NOT NULL,
    amount NUMERIC(10, 2) NOT NULL CHECK(amount > 0),
    related_account_id INT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'Completed',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);