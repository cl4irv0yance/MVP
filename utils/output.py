import sys
import itertools
import threading
import time

def print_section(title):
    print("\n" + "=" * 70)
    print("[*] " + title.center(64))
    print("=" * 70 + "\n")

def show_spinner(message, process):
    spinner_running = True

    def animate():
        for c in itertools.cycle(["|", "/", "-", "\\"]):
            if not spinner_running:
                break
            sys.stdout.write("\r[.] " + message + " " + c)
            sys.stdout.flush()
            time.sleep(0.1)

    spinner = threading.Thread(target=animate)
    spinner.start()

    process.wait()
    spinner_running = False
    spinner.join()
    print("\r[✓] " + message + " complete.\n")
