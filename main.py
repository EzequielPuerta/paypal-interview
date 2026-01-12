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
    alice.pay(bob, 50, description="Dinner")
    bob.pay(charly, 30, description="Lunch")

    # 3.a) Implement User.retrieve_activity() method
    alice_activity = alice.retrieve_activity()
    bob_activity = bob.retrieve_activity()
    charly_activity = charly.retrieve_activity()

    print(f"Alice's activity: {len(alice_activity)} payments")
    print(f"Bob's activity: {len(bob_activity)} payments")
    print(f"Charly's activity: {len(charly_activity)} payments")

    # 3.b) Implement MiniVenmo.render_feed() method
    feed_text = venmo.render_feed()
    print("Activity Feed:")
    print(feed_text)

    # 4) Implement User.add_friend() method
    alice.add_friend(bob)
    print(f"Alice's friends: {alice.friends}")
    print(f"Bob's friends: {bob.friends}")

    # 5) Implement event rendering for sorted payments and friend additions
    alice.pay(charly, 5, description="Breakfast")
    feed_text = venmo.render_feed()
    print("Updated Activity Feed:")
    print(feed_text)

if __name__ == "__main__":
    main()
