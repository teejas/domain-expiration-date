# Fetch domain expiration date using whois server lookup

This is a script for Python 3.7 which fetches the expiration date of a given domain through a whois server lookup

## Usage

1. Clone/download this repository
2. `pip install datetime` (this is the only requirement)
3. Run Python script and pass domains for lookup as command-line arguments (i.e. python3 check_domain_expiration.py www.example.com)
4. Results are printed to console as "Domain <Domain Name> expires on <Expiration Date>". Otherwise, a useful error message will be given.

NOTE: You can run lookup on multiple domains by passing multiple command-line arguments.

## Alternative Solutions

This solution does not use any pre-built API's, packages, or Python libraries. However, a quicker solution could be achieved by leveraging the [py-whois](https://pypi.org/project/whois/) package.
