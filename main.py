from src.mini_venmo import MiniVenmo


def main():
    print("Hello from paypal-interview!")
    venmo = MiniVenmo()
    venmo.create_user("Alice")


if __name__ == "__main__":
    main()
