
from modules.dnsdumpster import grab_dnsdumpster_map

import os
import subprocess
import argparse
import json
import time
from pathlib import Path
import requests
import socket
import shutil
import re
import threading
import itertools
import sys

home = str(Path.home())
dnscan_wordlist_path = "/usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-20000.txt"

#Making a little progress spinner 

import threading
import itertools
import sys

#Creating a spinner for tools that don't have visible output
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
    print("\r[✓] " + message + " complete.")
    print("\n")




# Tool Functions

def run_crtsh_tool(domain, output_dir):
    output_file = output_dir + "/crtsh.txt"
    
    base_dir = home + "/MVP/tools/crt.sh"
    cmd = [home + "/MVP/tools/crt.sh/crt.sh", "-d", domain]

    with open(output_file, "w") as outfile:
        try:
            subprocess.run(cmd, stdout=outfile, stderr=subprocess.PIPE, check=True, cwd=base_dir)
        except subprocess.CalledProcessError as e:
            print("[-] crt.sh script failed:", e)

    source_file = base_dir + "/output/domain." + domain + ".txt"
    cmd2 = ["cp", source_file, output_file]
    try:
        subprocess.run(cmd2, check=True)
    except subprocess.CalledProcessError as e:
        print("[-] Failed to copy the results to the output file.")

    cmd3 = ["cat", output_file]
    try:
        subprocess.run(cmd3, check=True)
    except subprocess.CalledProcessError as e:
        print("[-] Having issues displaying the crt.sh results..moving")


def run_dnstwist(domain, output_dir):
    output_file = output_dir + "/squatters.csv"
    cmd = ["dnstwist", "-o", output_file, "-f", "csv", "-t", "20", "-r", domain]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    show_spinner("Running dnstwist", process)
    #subprocess.run(cmd)

    source_file = home + "/MVP/recon/" + domain + "/squatters.csv"
    cmd2 = ["cat", source_file]
    subprocess.run(cmd2)


def run_subfinder(domain, output_file):
    cmd = ["subfinder", "-d", domain, "-o", output_file]
    subprocess.run(cmd)


def run_dnscan(domain, output_dir):
    dnscan_script = home + "/MVP/tools/dnscan/dnscan.py"
    wordlist = dnscan_wordlist_path
    output_file = output_dir + "/dnscan.txt"
    cmd = ["python3", dnscan_script, "-d", domain, "-w", wordlist, "-o", output_file]
    subprocess.run(cmd)



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
    print_section("Discovered " + str(len(seen)) + " unique subdomains.")
    cmd = ["cat", combined_file]
    subprocess.run(cmd)


def run_subjack(subdomain_file, output_dir):
    output_file = output_dir + "/subjack.txt"
    cmd = ["subjack", "-w", subdomain_file, "-t", "100", "-timeout", "30", "-o", output_file, "-ssl", "-m", "-c", "/usr/share/subjack/fingerprints.json", "-v", "1"]
    subprocess.run(cmd)


def setup_output_dirs(domain):
    base_path = Path("recon") / domain 
    base_path.mkdir(parents=True, exist_ok=True)
    return str(base_path)

#Pretty Banner functions and stuff

def print_section(title):
    print("\n" + "-" * 70)
    print("[*]" + title.center(64))
    print("-" * 70 + "\n")




    
