title: Find a Computer on the Active Directory With Just an IP Address
urlname: find-computer-ad-ip-address
date: 2011-02-17T11:13

This is PowerShell.

```
import-module activedirectory
get-adcomputer -filter * -properties ipv4address | where {$_.ipv4address -eq '10.0.0.1'}
```
