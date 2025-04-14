import os
from pathlib import Path

from utils.paths import * 
from utils.output import print_section


def dns_report(domain, dns_dir, reports_dir):
	report_path = os.path.join(reports_dir, "dns_report.html")

	html = "<html><head><title>DNS Recon Report</title></head><body>"
	html += "<h1> DNS Recon Report for " + domain + "</h1>"

	files = [
		("DNScan Results", "dnscan.txt"),
		("Subdomains", "all_subdomains.txt"), #made up of subfinder and crt.sh results
		("Subdomain Takeover Results", "subjack.txt"),
		("Typo Squatters", "dnstwist.csv")

	]

	for title, filename in files:
		file_path = os.path.join(dns_dir, filename)
		html += "<h2>" + title + "</h2><pre>"

		if os.path.exists(file_path):
			with open(file_path, "r") as f:
				html += f.read()
		else:
			html += "[!] No output available!"

		html += "</pre><hr>"

	html += "</body></html>"

	with open(report_path, "w") as f:
		f.write(html)

	print("[-->] DNS Report saved to: " + reports_dir)


	