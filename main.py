import subprocess
import random


def generate_random_mac():
    mac = []
    for i in range(6):
        byte = random.randint(0, 255)
        mac.append(f"{byte:02x}")
    return ":".join(mac)


def get_current_mac(interface):
    result = subprocess.run(["ifconfig", interface], capture_output=True, text=True)
    for line in result.stdout.split("\n"):
        if "ether" in line:
            return line.split()[1]
    return None


def change_mac(interface, new_mac):
    subprocess.run(["sudo", "ifconfig", interface, "down"])
    subprocess.run(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.run(["sudo", "ifconfig", interface, "up"])


def main():
    interface = input("Enter the interface: ")
    user_choice = input("Do you want to enter a new MAC address? (y/n) ")

    if user_choice.lower() in "yes1":
        new_mac = input("Enter the new MAC address: ")
    else:
        new_mac = generate_random_mac()

    current_mac = get_current_mac(interface)
    print(f"Current MAC address: {current_mac}")
    
    change_mac(interface, new_mac)

    updated_mac = get_current_mac(interface)
    if updated_mac == new_mac:
        print(f"MAC address changed successfully to {updated_mac}")
    else:
        print("Failed to change MAC address")


if __name__ == "__main__":
    main()
    