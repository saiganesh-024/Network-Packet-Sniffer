from scapy.all import sniff
from protocol_parser import parse_packet

def capture_packet(packet):
    parse_packet(packet)

print("Starting Packet Sniffer...")

sniff(prn=capture_packet, store=False)