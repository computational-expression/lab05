"""
Lab 5: Smart Home Status Monitor
CMPSC 100 - Computational Expression

Student Name: [Your name here]
Date: [Lab 5 Date]

Purpose: Create a smart home monitoring system using lists to track device status.
Practice adding and removing devices from lists while using LED indicators and button control.

"""

# Import necessary modules for hardware control
from machine import Pin
import time
import sys

# TODO 1: Set up hardware for IoT simulation
# Create GPIO pin objects for 3 LEDs and 1 button (4 variables)
# - 1st LED: Pin(15, Pin.OUT) 
# - 2nd LED: Pin(14, Pin.OUT)
# - 3rd LED: Pin(13, Pin.OUT)
button = Pin(12, Pin.IN, Pin.PULL_UP) # Control button (can use other pin if desired) 


# TODO 2: Create two lists for IoT device management
# Create exactly these two lists with these names:
# - active_devices: List starting with one led name (e.g. active_devies = ["thermostat"]) (devices currently ON)
# - available_devices: List with all three controllable devices (each device corresponds to one of the 3 LED systems)


def main():
    """Main function that runs the IoT smart home monitoring system"""
    
    # TODO 3: Program introduction and setup
    # Print introductory messages:
    # - "Smart Home Control System"
    # - "Select option 3 to exit the program"
    # Print session header with equal signs (==) border
    # Get user name with input("\nHomeowner name: ")


    # TODO 4: Welcome and system testing
    # Print welcome banner with user's name
    # Print system testing messages for each LED:
    # For each LED:
    # - Print system name, turn LED on, wait some number of seconds, turn LED off, wait again
    # Print that testing is done when finished


    # TODO 5: Initialize and display device status  
    # Print something to indicate initializing smart home devices (can add delays)
    # 
    # Display initial status:
    # - Print user's smart home status with their name
    # - Print "Active devices:" and list all items in active_devices list with numbers
    # - Print "Available devices (X total):" where X is len(available_devices)
    # - Use for loops with range(len(list_name)) to display numbered lists, 
    # -- here, list_name is active_devices or available_devices


    # TODO 6: Main IoT control loop
    # Create the main program loop with operation counter:
    # operation_count = 0 (done for you)
    # while True: (done for you)
    #   - Increment operation_count (done for you)
    #   - Print operation header with count (done for you)
    #   - Update LED status based on active devices for each LED (see TODO 7)
    #   - Show menu options 1-3 and get user choice (done for you)
    #   - Handle each choice (see TODOs 8-10)
    #   - Show updated status after each operation

    operation_count = 0
    while True:
        operation_count += 1
        print(f"\n" + "="*38)
        print(f"Home Control Operation {operation_count}")
        
        # TODO 7: LED status indicator logic (use this inside your main loop)
        # For each LED system, check if corresponding devices are active
        # for example, if one of my devices is called thermostat, we would do:
        # if "thermostat" in active_devices:
        #    led_security.on()
        # else:
        #    led_security.off()


        # Show menu options 1-3 and get user choice
        print("\nChoose an action:")
        print("1. Turn ON a device (add to active list)")
        print("2. Turn OFF a device (remove from active list)")
        print("3. Exit program")
        
        choice = input("Enter choice (1, 2, or 3): ")

        # TODO 8: Turn ON device (choice == "1") - USE append() method
        # Print "Available devices to turn ON:" (done for you)
        # Create off_devices = [] (empty list) (done for you)
        # Loop through available_devices: if device not in active_devices: off_devices.append(device)
        # If len(off_devices) == 0: print "All devices are already ON!" (done for you)
        # Else: 
        #   - Display numbered list of off_devices (done for you)
        #   - Get device_choice from user input (done for you)
        #   - If valid choice: selected_device = off_devices[device_choice - 1] (done for you)
        #   - Wait for button press confirmation (done for you)
        #   - Use active_devices.append(selected_device) to add device
        #   - Print confirmation message
        if choice == "1":
            # ADD DEVICE (turn ON)
            print("\nAvailable devices to turn ON:")
            off_devices = []
            for device in available_devices:
                if device not in active_devices:
                    off_devices.append(device)
            
            if len(off_devices) == 0:
                print("All devices are already ON!")
            else:
                for i in range(len(off_devices)):
                    print(f"  {i + 1}. {off_devices[i]}")
                
                device_choice = int(input(f"Choose device (1-{len(off_devices)}): "))
                selected_device = off_devices[device_choice - 1]
                
                # Wait for button confirmation AFTER device selection
                print("Press button to confirm...")
                while button.value() == 1:  # Wait for button press
                    time.sleep(0.1)
                time.sleep(0.2)  # Prevent button bounce
                print("Button pressed - command confirmed!")

            # TODO: Add device to the list and print confirmation message

        # TODO 9: Turn OFF device (choice == "2") - USE remove() method  
        # Print "Active devices to turn OFF:"
        # If len(active_devices) == 0: print "No devices are currently ON!"
        # Else:
        #   - Display numbered list of active_devices  
        #   - Get device_choice from user input
        #   - If valid choice: selected_device = active_devices[device_choice - 1]
        #   - Wait for button press confirmation 
        #   - Use remove method to remove a selected_device from active_devices
        #   - Print confirmation message


        # TODO 10: Exit program (choice == "3")
        elif choice == "3":
                # EXIT PROGRAM
                print("\nExiting Smart Home Control System...")
                print("All systems powered down. Goodbye!")
                # TODO: Turn off all LEDs before exit
                
                sys.exit()
            
        else:
            print("Invalid action!")


    # TODO 11: Status update display (use this after each operation)
    # Print updated status showing current active devices:
    # - Print f"Updated Status ({len(active_devices)} devices active):"
    # - If len(active_devices) == 0: print "  No devices currently active"
    # - Else: loop through active_devices and print each device name
    # - time.sleep(1) for brief pause

    # Your status update code here (put this at end of main loop):

# Main guard is provided for you:
if __name__ == "__main__":
    main()