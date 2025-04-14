import os
import subprocess
from utils.paths import *


def run_crtsh_tool(domain, dns_dir):
    output_file = dns_dir + "/crtsh.txt"
    
    base_dir = get_home_dir() + "/MVP/tools/crt.sh"
    cmd = [get_home_dir() + "/MVP/tools/crt.sh/crt.sh", "-d", domain]

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
