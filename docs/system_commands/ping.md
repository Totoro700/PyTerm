# ping

The `ping` command pings a server by a IP address (like in Windows cmd). 

```
> ping
IP address to ping?
............

Pinging ............ with 32 bytes of data:
Request timed out.
Request timed out.
Request timed out.
Request timed out.

Ping statistics for ............:
    Packets: Sent = 4, Received = 1, Lost = 3 (75% loss),
> 
```

(Replace the dots with the real IP address)

# Parameters

`-s` or `--self`: Pings your own server ( `socket.gethostbyname(socket.gethostname())` )

