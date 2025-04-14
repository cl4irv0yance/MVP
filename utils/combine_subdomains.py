import os
import subprocess
import argparse
import time
import threading

from utils.output import print_section
from utils.output import show_spinner


def combine_subdomains(output_dir, combined_file):
    seen = set()
    with open(combined_file, "w") as outfile:
        for filename in ["subfinder.txt", "crtsh.txt"]:
            filepath = os.path.join(output_dir, filename)
            if os.path.isfile(filepath):
                with open(filepath, "r") as infile:
                    for line in infile:
                        sub = line.strip()
                        if sub and sub not in seen:
                            seen.add(sub)
                            outfile.write(sub + "\n")

    class FakeProcess:
        def __init__(self, delay=5):
            self.delay = delay

        def wait(self):
            time.sleep(self.delay)

    fake_process = FakeProcess()
    print("\n" + "=" * 70 + "\n")
    show_spinner("Combining all subdomains...", fake_process)

    print_section("Discovered " + str(len(seen)) + " unique subdomains.")
    cmd = ["cat", combined_file]
    subprocess.run(cmd)