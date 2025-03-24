# Writeup
After scanning, we know how many ports are opened, hostname and operating system is running on.
![scan](./img/scan.png)

Using `smbclient -L {ip}` to list all SMB shares. 
![smb](./img/smb.png)

Search `CVE Windows 17` on Google, we can see the payload. Set `RHOSTS` as target's IP and `LHOST` as attacker's IP, then run.
![msf](./img/msf.png)

Using `Meteploits` for exploiting.

![exploit](./img/exploit.png)
