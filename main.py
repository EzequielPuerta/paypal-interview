from src.mini_venmo import MiniVenmo


def main():
    # 1) Create a MiniVenmo instance and create some users
    venmo = MiniVenmo()

    alice = venmo.create_user("Alice")
    bob = venmo.create_user("Bob")
    charly = venmo.create_user("Charly")

    print(f"Created users: {alice}, {bob} and {charly}")
    print(f"Users amount: {len(venmo.USERS)}")

    # 2) Implement User.pay() method
    alice.pay(bob, 50)
    bob.pay(charly, 30)

if __name__ == "__main__":
    main()
