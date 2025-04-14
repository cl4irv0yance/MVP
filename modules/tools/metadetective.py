import os
import subprocess
import argparse
import glob

from utils.paths import *
from utils.output import print_section


def run_metadetective(domain, files_dir, base_dir):
    metadetective_script = get_home_dir() + "/MVP/tools/MetaDetective/src/MetaDetective/MetaDetective.py"
    full_url = "https://" + domain
    cmd = ["python3", metadetective_script, "--scraping", "--download-dir", files_dir, "--url", full_url, "--depth", "1"]
    subprocess.run(cmd)

    cmd2 = ["python3", metadetective_script, "-d", files_dir, "-e"] #this exports to HTML with the name MetaData_Report
    subprocess.run(cmd2)

    print_section("Moving the HTML report back to your results directory.")
    report_files = glob.glob("MetaDetective_Export-*.html")
    if report_files:
        report_file = report_files[0]  # take the first match
        destination = os.path.join(base_dir, os.path.basename(report_file))
        os.rename(report_file, destination)
        print("[✓] Report moved to:", destination)
    else:
        print("[-] No HTML report found to move.")

    #Maybe need cmd3 here to cp the html export over to the files directory OR to clean out everythig but the HTML export
