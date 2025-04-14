import os
import subprocess
import argparse
from utils.output import show_spinner
from utils.paths import *

def run_dnstwist(domain, dns_dir):
    output_file = dns_dir + "/squatters.csv"
    cmd = ["dnstwist", "-o", output_file, "-f", "csv", "-t", "20", "-r", domain]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    show_spinner("Running dnstwist", process)
    #subprocess.run(cmd)

    source_file = get_home_dir() + "/MVP/results/dns/" + domain + "/squatters.csv"
    cmd2 = ["cat", source_file]
    subprocess.run(cmd2)