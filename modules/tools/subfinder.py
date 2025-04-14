import os
import subprocess
import argparse


def run_subfinder(domain, output_file):
    cmd = ["subfinder", "-d", domain, "-o", output_file]
    subprocess.run(cmd)