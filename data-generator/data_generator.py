import decimal
import os
import time
import random
import sys
import argparse
import psycopg2
from faker import Faker
from dotenv import load_dotenv

load_dotenv()

NUM_CUSTOMERS = 10
ACCOUNTS_PER_CUSTOMER = 2
NUM_TRANSACTIONS = 50
MAX_TRANSACTION_AMOUNT = 1000.00
CURRENCY = "USD"
INITIAL_BALANCE_MIN = decimal.Decimal("10.00")
INITIAL_BALANCE_MAX = decimal.Decimal("1000.00")
DEFAULT_LOOP = True
SLEEP_SECONDS = 2

parser = argparse.ArgumentParser(description = "Run fake data generator.")
parser.add_argument("--once", action = "store_true", help = "Run a single iteration and exit.")
args = parser.parse_args()
LOOP = not args.once and DEFAULT_LOOP

fake = Faker()

def random_money(min_val: decimal.Decimal, max_val: decimal.Decimal) -> decimal.Decimal:
    val = decimal.Decimal(str(random.uniform(float(min_val), float(max_val))))
    return val.quantize(decimal.Decimal("0.01"), rounding = decimal.ROUND_DOWN)

conn = psycopg2.connect(
    host = os.getenv("POSTGRES_HOST"),
    port = os.getenv("POSTGRES_PORT"),
    dbname = os.getenv("POSTGRES_DB"),
    user = os.getenv("POSTGRES_USER"),
    password = os.getenv("POSTGRES_PASSWORD"),
)
conn.autocommit = True
cur = conn.cursor()

def run_iteration():
    customers = []

    for _ in range(NUM_CUSTOMERS):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.unique.email()

        cur.execute(
            "INSERT INTO customers (first_name, last_name, email) VALUES (%s, %s, %s) RETURNING id",
            (first_name, last_name, email),
        )
        customer_id = cur.fetchone()[0]
        customers.append(customer_id)

    accounts = []

    for customer_id in customers:
        for _ in range(ACCOUNTS_PER_CUSTOMER):
            account_type = random.choice(["SAVINGS", "CHECKING"])
            initial_balance = random_money(INITIAL_BALANCE_MIN, INITIAL_BALANCE_MAX)
            insert_data_into_accounts_query = "INSERT INTO accounts (customer_id, account_type, balance, currency) VALUES (%s, %s, %s, %s) RETURNING id",
            
            cur.execute(
                insert_data_into_accounts_query,
                (customer_id, account_type, initial_balance, CURRENCY),
            )
            account_id = cur.fetchone()[0]
            accounts.append(account_id)

    txn_types = ["DEPOSIT", "WITHDRAWAL", "TRANSFER"]

    for _ in range(NUM_TRANSACTIONS):
        account_id = random.choice(accounts)
        txn_type = random.choice(txn_types)
        amount = round(random.uniform(1, MAX_TRANSACTION_AMOUNT), 2)
        related_account = None

        if txn_type == "TRANSFER" and len(accounts) > 1:
            related_account = random.choice([a for a in accounts if a != account_id])

        cur.execute(
            "INSERT INTO transactions (account_id, txn_type, amount, related_account_id, status) VALUES (%s, %s, %s, %s, 'COMPLETED')",
            (account_id, txn_type, amount, related_account),
        )

    print(f"Generated {len(customers)} customers, {len(accounts)} accounts, {NUM_TRANSACTIONS} transactions.")

try:
    iteration = 0
    while True:
        iteration += 1
        print(f"\nIteration {iteration} has been successfully started.")
        run_iteration()
        print(f"\nIteration {iteration} has been successfully finished.")
        if not LOOP:
            break
        time.sleep(SLEEP_SECONDS)

except KeyboardInterrupt:
    print("\nOperation has been interrupted by user, exiting gracefully...")

finally:
    cur.close()
    conn.close()
    sys.exit(0)
