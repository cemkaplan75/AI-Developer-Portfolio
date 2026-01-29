"""
Silver Token – Educational Prototype (v1)

This module implements a simplified silver-backed digital asset model.
It is designed for educational purposes only and is NOT a blockchain.

Key concepts:
- Higher circulation supply than gold
- Industrial demand considerations
- Minting and transfers with supply controls
"""

class SilverToken:
    def __init__(self, total_supply):
        self.total_supply = total_supply
        self.minted_supply = 0
        self.balances = {}

    def mint(self, account, amount):
        """Mint new tokens up to the fixed total supply."""
        if self.minted_supply + amount > self.total_supply:
            raise ValueError("Minting exceeds total silver reserves")

        self.balances[account] = self.balances.get(account, 0) + amount
        self.minted_supply += amount

    def transfer(self, sender, receiver, amount):
        """Transfer tokens between accounts."""
        if self.balances.get(sender, 0) < amount:
            raise ValueError("Insufficient balance")

        self.balances[sender] -= amount
        self.balances[receiver] = self.balances.get(receiver, 0) + amount

    def balance_of(self, account):
        """Return the token balance of an account."""
        return self.balances.get(account, 0)
