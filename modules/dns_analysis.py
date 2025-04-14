from modules.tools.dnsdumpster import grab_dnsdumpster_map
from modules.tools.crt_sh import run_crtsh_tool
from modules.tools.dnstwist import run_dnstwist
from modules.tools.subfinder import run_subfinder
from modules.tools.dnscan_runner import run_dnscan
from utils.combine_subdomains import combine_subdomains
from modules.tools.subjack import run_subjack
from utils.output import print_section
from utils.paths import *
from modules.reporting.dns_report import dns_report


def run_dns_analysis(domain, dns_dir, reports_dir):
    print_section("Running DNScan")
    run_dnscan(domain, dns_dir)

    print_section("Checking for Typo Squatters with DNSTwist")
    run_dnstwist(domain, dns_dir)

    print_section("Checking for Subdomains with Subfinder")
    run_subfinder(domain, dns_dir + "/subfinder.txt")

    print_section("Checking for More Subdomains with crt.sh")
    run_crtsh_tool(domain, dns_dir)

    #print_section("Combining All Subdomains")
    combined_file = dns_dir + "/all_subdomains.txt"
    combine_subdomains(dns_dir, combined_file)

    print_section("Checking for Takeovers with Subjack")
    run_subjack(combined_file, dns_dir)


    print_section("Generating an HTML Report.")
    dns_report(domain, dns_dir, reports_dir)


    print_section("DNS Analysis Complete. Output stored in: " + dns_dir)
