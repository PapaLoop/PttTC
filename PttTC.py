import pyautogui
import keyboard
import time

def capture_coordinates():
    print("Move your mouse over the microphone button and press 'Enter' to capture the coordinates.")
    while True:
        if keyboard.is_pressed('enter'):
            x, y = pyautogui.position()
            print(f"Coordinates captured: ({x}, {y})")
            return x, y
        time.sleep(0.1)

def main():
    # Capture the coordinates
    mic_x, mic_y = capture_coordinates()

    # Key to press to activate the microphone (e.g., spacebar)
    activation_key = 'space'

    print(f"Press and hold '{activation_key}' to activate the microphone")

    try:
        while True:
            # Wait for spacebar event
            if keyboard.is_pressed(activation_key):
                pyautogui.mouseDown(mic_x, mic_y)

                # Wait until the spacebar is released
                while keyboard.is_pressed(activation_key):
                    time.sleep(0.01)  # Check every 10ms for key release

                pyautogui.mouseUp(mic_x, mic_y)

            # Small delay to reduce CPU usage
            time.sleep(0.01)  # Check every 10ms for key press
    except KeyboardInterrupt:
        print("Program stopped.")

if __name__ == "__main__":
    main()
