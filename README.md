# POC-WINRAR

# CVE-2023-38831-WinRAR-Exploit
Proof of concept (PoC) exploit for WinRAR vulnerability (CVE-2023-38831) vulnerability

Usage: _python poc.py <BAIT_FILENAME> <SCRIPT_FILENAME> <OUTPUT_FILENAME>_

Example: python poc.py vos_photos.jpg exploit.bat vos_photos.rar_

# Exploit.bat

The script downloads an image from a URL, displays the image, gathers system information, saves it to a file, copies this file to a remote server, deletes the local file, waits for a few seconds, and then restarts the system.

# Poc.py 

The script takes three files as input, uses them to create an "exploit" by modifying a template, and then saves this exploit to an output file.