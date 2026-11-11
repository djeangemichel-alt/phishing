from scapy.all import IP, ICMP,Raw,UDP,TCP ,send


with open("hello.py","", "rb") as f:    # rb pour read binary 
    data = f.read()
message = IP(dst= "192.168.56.1") / ICMP() / Raw(load=data)
send(message)