import serial
import time

# Func to send AT command, returnd utf-8 decoded result
def send_at_command(ttyUSB: str, command: str, time_to_sleep: int = 1) -> str:
    """Send AT comman to modem, get imput of `/dev/ttyUSB`, `command` string,
    and `time_to_sleep` in secounds to wait until get the result (some commannds takes more time, the default set to 1 sec).
    returns the serial response as string"""
    result = ""
    try:
        console = serial.Serial(ttyUSB, 115200, timeout=2)
        print(f"Set modem {command}...")
        command_to_send = f"{command}\r\n"
        try:
            console.write(command_to_send.encode("utf-8"))
            time.sleep(time_to_sleep)
            result = console.read_until(b"OK\r\n" or b"ERROR\r\n").decode("utf-8")
            console.close()
            if "OK" in result:
                print(f"{command} result is OK:")
                return result
            elif "ERROR" in result:
                print(f"{command} result is ERROR:")
                return result
        except Exception as e:
            print(f"ERROR: could NOT set {command} -{e}")
    except Exception as e:
        print(
            f"ERROR: Something went wrong or slot is empty ...  or slot is empty - {e}"
        )
    return result


def print_image() -> None:
    response = ""
    try:
        response = send_at_command("/dev/ttyUSB1", "AT!IMAGE?", 1)
        print(response)
    except Exception as e:
        print(
            f"Failed to retrieve FW version {response} - {e}"
        )


print_image()