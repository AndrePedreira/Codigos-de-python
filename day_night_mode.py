class DayNightMode:
    def __init__(self):
        self.current_time = "day"  # Default to day

    def set_time(self, choice):
        """Sets the time of day based on player choice."""
        if choice.lower() in ["day", "night"]:
            self.current_time = choice.lower()
            print(f"It is now {self.current_time}.")
        else:
            print("Invalid choice! Please enter 'day' or 'night'.")

    def apply_day_night_effects(self, player, monster):
        """Applies effects based on the current time of day."""
        if self.current_time == "day":
            monster.attack_power -= 2  # Monsters are weaker during the day
            player.defense += 1  # Player gets a slight defense boost
        else:
            monster.attack_power += 2  # Monsters are stronger at night
            player.defense -= 1  # Player has reduced defense

    def is_shop_open(self):
        """Checks if the shop is open."""
        return self.current_time == "day"