# POC-WINRAR

# CVE-2023-38831-WinRAR-Exploit
Proof of concept (PoC) exploit for WinRAR vulnerability (CVE-2023-38831) vulnerability

A critical vulnerability has been discovered in versions of the WinRAR software prior to 6.23, developed by RARLabs. This security flaw potentially allows attackers to execute malicious code by manipulating a specially crafted ZIP archive. The vulnerability lies in the flawed handling of ZIP archives containing harmless files, such as standard PDF documents, and folders with the same name. When a user attempts to access the harmless file, the archive may include a folder with the same name but containing malicious executable content. When attempting to access the harmless file, this malicious content is processed, potentially opening the door to arbitrary code execution by the attacker.

This vulnerability has been exploited in real-world attacks that occurred between April and August 2023, posing a security risk to WinRAR users. To protect against this threat, it is crucial to update WinRAR to version 6.23 or a later release, which addresses this security flaw.

To exploit this vulnerability, here's how it can be done:

git clone https://github.com/mkonate19/POC-WINRAR.git

cd POC-WINRAR 

Usage: _python poc.py <BAIT_FILENAME> <SCRIPT_FILENAME> <OUTPUT_FILENAME>_

Example: python poc.py vos_photos.jpg exploit.bat vos_photos.rar_

# Exploit.bat

The script downloads an image from a URL, displays the image, gathers system information, saves it to a file, copies this file to a remote server, deletes the local file, waits for a few seconds, and then restarts the system.

# Poc.py 

The script takes three files as input, uses them to create an "exploit" by modifying a template, and then saves this exploit to an output file.