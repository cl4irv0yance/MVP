from modules.tools.metadetective import run_metadetective
from utils.output import print_section
from utils.paths import *

def run_file_enum (domain, files_dir, base_dir):
    print_section("Performing File MetaData Recon")
    run_metadetective(domain, files_dir, base_dir)

    print("\n[-->] MetaData hunting is complete. Output stored in:", files_dir)
