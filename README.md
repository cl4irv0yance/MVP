# MVP

## What is MVP?

M(ost) (V)aluable (P)ieces is a tool that has been designed to perform various stages of a penetration test for you. Currently, it has several different modules that can be utillized to perform inital phases of a test that you **have been authorized** to perform. 

## What can it do? 

Right now, it will perform the following: 

DNS Analysis
  - SPF/DMARC/DKIM Checks
  - Zone Transfers
  - Typo Squatting Checks
  - Host Information Gathering

Subdomain Enumeration
  - Subdomain Takeovers

File Enumeration & MetaData Review

User Enumeration & Breach Data Review (coming soon)


## Usage 

For basic usage - you can use the following command: 

`python3 mvp.py -d <domain>`

This will run all modules directly. 

For a specific module, you can use the following flags: 
`--dns` - Performs the DNS Analysis & Recon Pieces 
`--users` - Performs Web Scraping for Users & User validation
`--files` - Performs File MetaData Enumeration/Hunting
`--spoof` - Perform Microsoft Direct Send Testing
`--all` - Runs all checks
