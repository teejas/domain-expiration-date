import sys
import socket
import datetime

def query_whois(tld, domain):
    # TLD exists. Connecting to whois server on port 43 to send query
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((tld + '.whois-servers.net', 43))
    except:
        print("Failed to connect to whois server on port 43.")
        return None

    try:
        msg = (domain + '\r\n').encode()
        s.send(msg)
    except TypeError as err:
        print("Failed to send message to whois server.")
        print("Error: " + str(err))
        s.close()
        return None

    try:
        res = ""
        while True:
            buff = s.recv(512)
            if not buff:
                break
            res += buff.decode()
        s.close()
        return res
    except TypeError as err:
        print("Failed to receive response from whois server.")
        print("Error: " + str(err))
        s.close()
        return None

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 0 or args[0] == '--usage' or args[0] == '-U':
        print("Run script with domains passed as arguments:")
        print("i.e. python3 check_domain_expiration.py www.example.com")

    else:
        # Load in list of acceptable TLDs
        tld_file = open("tld-list.txt", "r")
        tld_list = tld_file.read().split('\n')

        for domain in args:
            d_arr = domain.split('.')
            if len(d_arr) < 2:
                print("Wrong format for domain. i.e. www.example.com")
                continue

            tld = d_arr[-1]
            if tld.upper() not in tld_list:
                print("TLD does not exist.")
            else:
                whois_data = query_whois(tld, domain)
                if not whois_data:
                    print("Unable to get whois data for domain: " + domain)
                    continue

                if "Registry Expiry Date" in whois_data:
                    try:
                        data_arr = whois_data.split('\n')
                        expire_str = data_arr[6].strip()
                        date = datetime.datetime.strptime(expire_str.split(' ')[-1], "%Y-%m-%dT%H:%M:%SZ")
                        print("Domain " + domain + " expires on "  + str(date))
                    except TypeError as err:
                        print("Error getting date from whois data.\nResponse from whois server below:")
                        print(whois_data)
                        print(err)

                else:
                    print("Domain expiration date could not be found.\nResponse from whois server below:")
                    print(whois_data)
