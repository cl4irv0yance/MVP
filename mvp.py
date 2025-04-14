import time
import argparse
from pathlib import Path


from modules.dns_analysis import run_dns_analysis
from modules.file_enum import run_file_enum
from utils.output import print_section
from utils.paths import *
from utils.setup import tool_checks
 


def main():
    parser = argparse.ArgumentParser(description="Most Valuable Pieces")
    parser.add_argument("-d", "--domain", required=True, help="Target domain")
    parser.add_argument("--dns", action="store_true", help="Run DNS analysis phase")
    parser.add_argument("--users", action="store_true", help="Runs the User Enumeration phase")
    parser.add_argument("--files", action="store_true", help="Runs the File Enumeration phase")
    parser.add_argument("--spoof", action="store_true", help="Performs Microsoft Direct Send Testing")
    parser.add_argument("--all", action="store_true", help="Run all phases")
    args = parser.parse_args()

    domain = args.domain
    output_dir = setup_output_dirs(domain)

    base_dir = output_dir["base"]
    dns_dir = output_dir["dns"]
    files_dir = output_dir["files"]
    reports_dir = output_dir["reports"]

    if args.all:
        print_section("Running all phases.")
        tool_checks()
        run_dns_analysis(domain, dns_dir, reports_dir)
        run_file_enum(domain, files_dir, base_dir)
        #run_user_enum(domain, output_dir)

    elif args.dns:
        tool_checks()
        run_dns_analysis(domain, dns_dir, reports_dir)

    elif args.files:
        tool_checks()
        run_file_enum(domain, files_dir, base_dir)

    else:
        print_section("[!] No phase selected. Running everything.")
        tool_checks()
        time.sleep(3)
        run_dns_analysis(domain, dns_dir, reports_dir)
        run_file_enum(domain, files_dir, base_dir)


    print_section("MVP is complete. Output stored in:" + base_dir)


if __name__ == "__main__":
    main()
