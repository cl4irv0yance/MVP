import os
import requests
from bs4 import BeautifulSoup

def grab_dnsdumpster_map(domain, output_dir):
    print("[+] Fetching DNSDumpster map for", domain)

    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://dnsdumpster.com"
    }

    try:
        # Step 1: GET the page to grab CSRF token
        resp = session.get("https://dnsdumpster.com", headers=headers)
        soup = BeautifulSoup(resp.text, "html.parser")
        csrf_token = soup.find("input", {"name": "csrfmiddlewaretoken"}).get("value")

        # Step 2: POST to submit the domain
        data = {
            "csrfmiddlewaretoken": csrf_token,
            "targetip": domain
        }

        post_headers = headers.copy()
        post_headers["Content-Type"] = "application/x-www-form-urlencoded"
        post_headers["Referer"] = "https://dnsdumpster.com"

        resp = session.post("https://dnsdumpster.com", data=data, headers=post_headers)

        # Step 3: Parse the returned HTML for the image
        soup = BeautifulSoup(resp.text, "html.parser")
        img = soup.find("img", {"src": lambda x: x and x.endswith(".png")})
        if img:
            img_url = "https://dnsdumpster.com" + img["src"]
            img_data = session.get(img_url).content

            out_path = os.path.join(output_dir, "dnsdumpster_map.png")
            with open(out_path, "wb") as f:
                f.write(img_data)

            print("[✓] DNS map saved to:", out_path)
        else:
            print("[-] DNS map image not found.")

    except Exception as e:
        print("[-] Failed to retrieve DNSDumpster map:", e)
