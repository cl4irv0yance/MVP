from pathlib import Path
import os

def get_home_dir():
    return str(Path.home())

def setup_output_dirs(domain):
    base_path = Path("results") / domain
    base_path.mkdir(parents=True, exist_ok=True)


    dns_recon_path = base_path / "dns"
    dns_recon_path.mkdir(parents=True, exist_ok=True)

    file_recon_path = base_path / "files"
    file_recon_path.mkdir(parents=True, exist_ok=True)

    users_path = base_path / "users"
    users_path.mkdir(parents=True, exist_ok=True)

    reports_path = base_path / "reports"
    reports_path.mkdir(parents=True, exist_ok=True)


    return {
        "base": str(base_path),
        "dns": str(dns_recon_path), 
        "files": str(file_recon_path),
        "users": str(users_path),
        "reports": str(reports_path)

    }

# Default wordlist for dnscan
dnscan_wordlist_path = "/usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-20000.txt"

# Optional: centralized tool path if using /MVP/tools/
def get_tool_path(tool_name):
    return os.path.join(get_home_dir(), "MVP", "tools", tool_name)
