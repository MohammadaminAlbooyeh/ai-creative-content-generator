class TransactionalEmailTemplate:
    def __init__(self):
        self.name = "transactional"

    def render(self, subject: str, recipient_name: str, transaction_details: dict) -> str:
        details = "\n".join([f"{k}: {v}" for k, v in transaction_details.items()])
        return f"Subject: {subject}\n\nHi {recipient_name},\n\nHere are your transaction details:\n\n{details}"
