import os
import subprocess
import argparse

from utils.paths import *


def run_subjack(subdomain_file, dns_dir):
    output_file = dns_dir + "/subjack.txt"
    cmd = ["subjack", "-w", subdomain_file, "-t", "100", "-timeout", "30", "-o", output_file, "-ssl", "-m", "-c", "/usr/share/subjack/fingerprints.json", "-v", "1"]
    subprocess.run(cmd)