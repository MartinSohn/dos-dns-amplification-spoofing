# dos-dns-amplification-spoofing
Python tool for doing Denial of Service with DNS amplification and spoofing

DNS RFC 1035 specificerer: "Messages sent using UDP user server port 53 (decimal)." Men som observeret med Wireshark starter Windows med tilfældig dynamisk port og incrementer med én for hver query.  
https://www.ietf.org/rfc/rfc1035.txt

ANY query vil retunere mest data til amplification - der vælges derfor et domæne der får request til at fylde mindst muligt men retunerer meget, eks. TXT records for b.dk  
Alternativt kan angriberen registrere et domæne selv (eller overtage navneserver kontrol) og indsætte meget DNS data på et domæne (eller subdomæne) og bruge det i angrebet.

Der er som standard begrænsning på DNS responses. For at få ANY query response til at fylde mere skal man i DNS headers aktivere EDNS0:
"DNS uses TCP when the size of the request or the response is greater than a single packet such as with responses that have many records or many IPv6 responses or most DNSSEC responses.
[..]there is an extension to the DNS protocol that allows clients to indicate that they can handle UDP responses of up to 4096 bytes."  
Kilde: https://serverfault.com/questions/404840/when-do-dns-queries-use-tcp-instead-of-udp  
Kilde til Scapy kode der bruger EDNS0: https://lost-and-found-narihiro.blogspot.com/2014/01/scapy-dev-220-generate-crafted-edns0.html

Eksempel på amplification ved at brugte b.dk's ANY record:  
send: 75 bytes  
modtag: 973 bytes  
12,97 gange amplification.  
Langt fra den gennemsnitlige på 54.6 ANY query fra papiret "Amplification Hell: Revisiting Network Protocols for DDoS Abuse".  
Teoretisk burde det være muligt at modtage et 4096 byte UDP svar på en 33 byte UDP request, det giver amplification på 123,88

Source IP kan spoofes - men skulle gerne *ikke* virke på WAN hvis din ISP er kompetent.

Værktøj til amplification: https://github.com/OffensivePython/Saddam
- Kan lave DNS, NTP, SMTP, SSDP amplification.
- Giver mulighed for at lave et estimat på trafikmængden i et angreb.
