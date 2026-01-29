"""
Gold Token – Educational Prototype (v1)

A simplified, asset-backed token model to demonstrate
fixed supply, balances, minting, and transfers.

This is NOT a blockchain implementation.
It is an educational simulation.
"""

class GoldToken:
    def __init__(self, total_supply):
        self.total_supply = total_supply
        self.balances = {}
        self.minted_supply = 0

    def mint(self, account, amount):
        """Mint new tokens up to the fixed total supply."""
        if self.minted_supply + amount > self.total_supply:
            raise ValueError("Minting exceeds total gold reserve.")
        self.balances[account] = self.balances.get(account, 0) + amount
        self.minted_supply += amount

    def transfer(self, sender, receiver, amount):
        """Transfer tokens between accounts."""
        if self.balances.get(sender, 0) < amount:
            raise ValueError("Insufficient balance.")
        self.balances[sender] -= amount
        self.balances[receiver] = self.balances.get(receiver, 0) + amount

    def balance_of(self, account):
        """Return balance of a specific account."""
        return self.balances.get(account, 0)


# Example usage (for demonstration)
if __name__ == "__main__":
    gold = GoldToken(total_supply=1_000_000)

    gold.mint("Treasury", 500_000)
    gold.transfer("Treasury", "Alice", 50_000)
    gold.transfer("Treasury", "Bob", 25_000)

    print("Treasury balance:", gold.balance_of("Treasury"))
    print("Alice balance:", gold.balance_of("Alice"))
    print("Bob balance:", gold.balance_of("Bob"))
