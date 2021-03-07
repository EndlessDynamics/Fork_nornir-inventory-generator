def nor_inv(filename): 
    with open(filename) as f: 
        data = f.read().splitlines() 
        newlist = [] 
        for values in data: 
            name_ip = tuple(values.split(" ")) 
            newlist.append(name_ip) 
        for name,ip in newlist: 
            print(f"{name.upper()}:") 
            print(f"   hostname: {ip}") 
            print("   group") 
            site_abb = name.split("-") 
            print(f"       - {site_abb[0].upper()}")
            print("   platform: 'ios'")

if __name__ == '__main__':
  nor_inv("ip_addr.txt")
