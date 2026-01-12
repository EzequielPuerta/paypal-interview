from src.mini_venmo import MiniVenmo


def main():
    venmo = MiniVenmo()
    alice = venmo.create_user("Alice")
    bob = venmo.create_user("Bob")
    charly = venmo.create_user("Charly")
    print(f"Created users: {alice}, {bob} and {charly}")
    print(f"Users amount: {len(venmo.USERS)}")

if __name__ == "__main__":
    main()
