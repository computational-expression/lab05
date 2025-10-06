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
# Create GPIO pin objects for 3 LEDs and 1 button:
# - led_security: Pin(15, Pin.OUT) - Red LED for Security system (Pin 20 → Row 21)
# - led_hvac: Pin(14, Pin.OUT) - Yellow LED for HVAC system (Pin 19 → Row 22)  
# - led_lighting: Pin(13, Pin.OUT) - Green LED for Lighting system (Pin 17 → Row 23)
# - button: Pin(12, Pin.IN, Pin.PULL_UP) - Control button (Pin 16 → Rows 27/29)

# Your hardware setup here:


# TODO 2: Create two lists for IoT device management
# Create exactly these two lists with these names:
# - active_devices: List starting with ["thermostat"] (devices currently ON)
# - available_devices: List with ["thermostat", "front_door_lock", "living_room_lights"] (all controllable devices)
# Each device corresponds to one of the 3 LED systems

# Your device lists here:


# TODO 3: Program introduction and setup
# Print introductory messages:
# - "Smart Home Control System"
# - "Select option 3 to exit the program"
# Print session header with equal signs (==) border
# Get user name with input("\nHomeowner name: ")

# Your introduction code here:


# TODO 4: Welcome and system testing
# Print welcome banner with user's name
# Print system testing messages for each LED:
# For each system (Security, HVAC, Lighting):
# - Print system name, turn LED on, wait 0.5 seconds, turn LED off
# Print "All systems operational!" when done

# Your welcome and testing code here:


# TODO 5: Initialize and display device status  
# Add device initialization sequence:
# - Wait 1 second, print "Initializing smart home devices..."
# - Print "Adding devices to available control list..."
# - Wait 1.5 seconds, print "Device setup complete!"
# 
# Display initial status:
# - Print user's smart home status with their name
# - Print "Active devices:" and list all items in active_devices with numbers
# - Print "Available devices (X total):" where X is len(available_devices)
# - Use for loops with range(len(list_name)) to display numbered lists

# Your status display code here:


# TODO 6: Main IoT control loop
# Create the main program loop with operation counter:
# while True:
#   - Increment operation_count
#   - Print operation header with count
#   - Update LED status based on active devices (see TODO 7)
#   - Show menu options 1-3 and get user choice
#   - Handle each choice (see TODOs 8-10)
#   - Show updated status after each operation

operation_count = 0
# Your main control loop here:


# TODO 7: LED status indicator logic (use this inside your main loop)
# For each LED system, check if corresponding devices are active:
# 
# Security LED logic:
# - Create security_active = False
# - Loop through active_devices: if "lock" in device or "camera" in device or "security" in device: set security_active = True and break
# - If security_active: led_security.on(), else: led_security.off()
#
# HVAC LED logic:
# - If "thermostat" in active_devices: led_hvac.on(), else: led_hvac.off()
#
# Lighting LED logic:
# - Create lighting_active = False
# - Loop through active_devices: if "light" in device: set lighting_active = True and break  
# - If lighting_active: led_lighting.on(), else: led_lighting.off()

# Your LED status logic here (put this inside the main loop):


# TODO 8: Turn ON device (choice == "1") - USE append() method
# Print "Available devices to turn ON:"
# Create off_devices = [] (empty list)
# Loop through available_devices: if device not in active_devices: off_devices.append(device)
# If len(off_devices) == 0: print "All devices are already ON!"
# Else: 
#   - Display numbered list of off_devices
#   - Get device_choice from user input
#   - If valid choice: selected_device = off_devices[device_choice - 1]
#   - Wait for button press confirmation (see TODO 11)
#   - Use active_devices.append(selected_device) to add device
#   - Print confirmation message

# Your turn ON device code here (put this in choice == "1" section):


# TODO 9: Turn OFF device (choice == "2") - USE remove() method  
# Print "Active devices to turn OFF:"
# If len(active_devices) == 0: print "No devices are currently ON!"
# Else:
#   - Display numbered list of active_devices  
#   - Get device_choice from user input
#   - If valid choice: selected_device = active_devices[device_choice - 1]
#   - Wait for button press confirmation (see TODO 11)
#   - Use active_devices.remove(selected_device) to remove device
#   - Print confirmation message

# Your turn OFF device code here (put this in choice == "2" section):


# TODO 10: Exit program (choice == "3")
# Print "Exiting Smart Home Control System..."
# Print "All systems powered down. Goodbye!" 
# Turn off all LEDs: led_security.off(), led_hvac.off(), led_lighting.off()
# Use sys.exit() to end the program

# Your exit code here (put this in choice == "3" section):


# TODO 11: Button confirmation logic (use this in TODOs 8 and 9)
# After device selection, add button confirmation:
# - Print "Press button to confirm..."
# - while button.value() == 1: time.sleep(0.1)  # Wait for button press
# - time.sleep(0.3)  # Debounce delay
# - while button.value() == 0: time.sleep(0.1)  # Wait for button release  
# - Print "Button pressed - command confirmed!"

# Your button confirmation code here (use in device operations):


# TODO 12: Status update display (use this after each operation)
# Print updated status showing current active devices:
# - Print f"Updated Status ({len(active_devices)} devices active):"
# - If len(active_devices) == 0: print "  No devices currently active"
# - Else: loop through active_devices and print each device name
# - time.sleep(1) for brief pause

# Your status update code here (put this at end of main loop):