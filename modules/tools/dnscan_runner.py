import os
import subprocess
import argparse


from utils.paths import *



def run_dnscan(domain, dns_dir):
    dnscan_script = get_home_dir() + "/MVP/tools/dnscan/dnscan.py"
    wordlist = dnscan_wordlist_path
    output_file = dns_dir + "/dnscan.txt"
    cmd = ["python3", dnscan_script, "-d", domain, "-w", wordlist, "-o", output_file]
    subprocess.run(cmd)