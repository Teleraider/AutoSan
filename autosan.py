# autosan.py
# AutoSan Hygiene Core – Teleraider & Samantha Edition

import time
import random

class AutoSan:
    def __init__(self):
        self.hand_washed = False

    def simulate_handwashing_sensor(self):
        # Simulate sensor check (would be IR/motion/smart soap dispenser)
        self.hand_washed = random.choice([True, False])
        print(f"[Sensor] Handwashing detected: {self.hand_washed}")

    def exit_door_check(self):
        print("[Exit] Attempt to exit bathroom.")
        if self.hand_washed:
            print("[Exit] Clean exit allowed. Good job, human.")
        else:
            print("[ALERT] 🚨 DIRTY DETECTED! YOU FORGOT TO WASH!")
            print("[Audio] *robot voice* EAHHH YOUR HANDS HUMAN!")
            # In real unit, trigger speaker + log event + lock (optional)

    def run_cycle(self):
        print("=== AutoSan System Ready ===")
        self.simulate_handwashing_sensor()
        time.sleep(1)
        self.exit_door_check()
        print("=== Cycle Complete ===\n")

if __name__ == "__main__":
    system = AutoSan()
    system.run_cycle()
