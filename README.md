# MAC Address Changer

This project is a simple Python script that allows you to change the MAC address of a network interface. It uses the `subprocess` module to execute terminal commands.

## Description

The script performs the following tasks:
1. Generates a random MAC address.
2. Gets the current MAC address of a specified network interface.
3. Changes the MAC address to a new specified or randomly generated MAC address.

## Installation

1. Clone the repository or download the script.
2. Ensure you have Python installed on your system.

## Usage

1. Run the script with elevated privileges:
    ```bash
    sudo python3 main.py
    ```
    or
    ```bash
    sudo python main.py
    ```

2. Follow the prompts to enter the network interface and choose whether to enter a new MAC address or generate a random one.

## Code Implementation

### Importing Required Modules

```python
import subprocess
import random
```

### Generating a Random MAC Address

```python
def generate_random_mac():
    mac = []
    for i in range(6):
        byte = random.randint(0, 255)
        mac.append(f"{byte:02x}")
    return ":".join(mac)
```

### Getting the Current MAC Address

```python
def get_current_mac(interface):
    result = subprocess.run(["ifconfig", interface], capture_output=True, text=True)
    for line in result.stdout.split("\n"):
        if "ether" in line:
            return line.split()[1]
    return None
```

### Changing the MAC Address

```python
def change_mac(interface, new_mac):
    subprocess.run(["sudo", "ifconfig", interface, "down"])
    subprocess.run(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.run(["sudo", "ifconfig", interface, "up"])
```

### Main Function

```python
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
```

### Running the Script

```python
if __name__ == "__main__":
    main()
```
