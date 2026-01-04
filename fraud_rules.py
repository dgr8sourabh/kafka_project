def is_fraud(transaction):
    if transaction["amount"] > 10000:
        return True, "High transaction amount"
    return False, None
