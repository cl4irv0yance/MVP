import os
import subprocess
from utils.paths import get_home_dir

def tool_checks():
	tools = {
		"crt.sh": "https://github.com/az7rb/crt.sh.git",
        "dnscan": "https://github.com/rbsec/dnscan.git",
       	"LinkedInDumper": "https://github.com/l4rm4nd/LinkedInDumper.git",
       	"MetaDetective": "https://github.com/franckferman/MetaDetective.git",
       	"TREVORspray": "https://github.com/blacklanternsecurity/TREVORspray.git"
	}

	tools_dir = os.path.join(get_home_dir(), "MVP", "tools")
	os.makedirs(tools_dir, exist_ok=True)

	for name, repo in tools.items():
		tools_path = os.path.join(tools_dir, name)

		if not os.path.exists(tools_path):
			print("\n[-->] Installing " + name + "....")
			cmd = (["git", "clone", repo, tools_path])
			subprocess.run(cmd)

			#Have to make this executable so built in the check 
			if name == "crt.sh":
				crt_sh_path = os.path.join(tools_dir, "crt.sh", "crt.sh")
				if os.path.exists(crt_sh_path):
					os.chmod(crt_sh_path,0o755)

		else: 
			print("\n[X] " + name + " is already installed!")

