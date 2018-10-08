import sys
from subprocess import check_output 
import re

subdomain_list =[]
search_domain_list = "list.txt"

def takeover_scan(list):
    pattern = r"CNAME\t(.*)"
    pattern_cname = re.compile(pattern)
    with open(list,"r") as domain:
        domain.readline()
    dnslist = ['dig','www.shopify.com','cname']
    result = check_output(dnslist)

    list = pattern_cname.search(str(result))

    if(list):
        subdomain_list = list.group(1)
        print list.group(1)
    else:
        print "CNAME Record is not found"

def main():
    takeover_scan(search_domain_list)


if __name__ == '__main__':
    main()


