import subprocess
import os
import sys

Select = int(input("Select type of download:\n1 - Full Bundle\n2 - My Selection\n3 - Let me choose\nType 1,2 or 3 > ").strip())

def reexec_with_sudo():
    if os.geteuid() != 0:
        os.execvp("sudo", ["sudo", "-E", sys.executable] + sys.argv)

def full_bundle():
    if Select == 1:


        OSINT_tools = ["amass","theharvester","httrack","exiftool","mat2","sherlock",
                   "instaloader","mediainfo","spiderfoot"]

        recon_tools = ["arp-scan","nmap","aircrack-ng","seclists"]

        enumeration_tools = ["enum4linux","searchsploit","netexec","sqlmap","nuclei"]

        exploitation_tools = ["metasploit-framework","mimikatz","ghidra"]

        brute_force = ["hydra", "john","patator"]

        network_tools = ["iptables","wireshark", "iproute2", "net"]

        web_tools = ["curl","feroxbuster","wfuzz","gobuster","nikto","whatweb","openssl","masscan"]

        windows_test_tools = ["smbclient", "smbmap","bloodhound","netexec","powerSploit"
                          ,"evil-winrm"]

        tools = [*OSINT_tools, *recon_tools, *enumeration_tools, *exploitation_tools, *brute_force, *network_tools, *web_tools,
             *windows_test_tools
             ]

        Pac_Manager = input("Select your packet manager:\n1 - apt\n2 - pacman\n3 - DNF\nType 1,2 or 3 > ").strip()
        if Pac_Manager == 1:
            cmd = ["sudo","apt","install","-y", *tools]
            subprocess.run(cmd, text=True)


        elif Pac_Manager == 2:
            cmd = ["sudo", "pacman", "-S", "--noconfirm", *tools]
            subprocess.run(cmd, text=True)


    pip_tools = ["socialscan", "holehe", "requests", "impacket","graphspy",
                 "git+https://github.com/Tib3rius/AutoRecon.git",
                 "git+https://github.com/blacklanternsecurity/MANSPIDER","certipy-ad","impacket minikerberos"]

    go_tools = ["github.com/cgrates/rpcclient","github.com/rookmoot/proxifier"]
    repos = [
        "https://github.com/s0md3v/Photon",
        "https://github.com/s0md3v/Arjun",
        "https://github.com/s0md3v/XSStrike",
        "https://github.com/fin3ss3g0d/secretsdump.py",  ##############################
        "https://github.com/ropnop/kerbrute",
        "https://github.com/jondonas/linux-exploit-suggester-2",
        "https://github.com/strozfriedberg/Windows-Exploit-Suggester",
        "https://github.com/Exbinary/scopelist",  ######
        "https://github.com/Exbinary/webticket",  ######
        "https://github.com/commixproject/commix",
        "https://github.com/EnableSecurity/wafw00f",
        "https://github.com/aboul3la/Sublist3r",
        "https://github.com/SploitHQ/searchsploit",
        "https://github.com/ffuf/ffuf",
        "https://github.com/peass-ng/PEASS-ng",
        "https://github.com/BishopFox/sliver",
        "https://github.com/ShutdownRepo/pywhisker",
        "https://github.com/dirkjanm/PKINITtools"

    ]

    for i, rep in enumerate(repos,
                            start=1):  # enumerate(tools, start=1) automatically gives each tool a number starting at 1.
        print(
            f"|---------------------------------------------------------------|\n -  {rep}")

    install = input("---------------------------------------------------------------------\nBesides system packet manager tools, do you want to clone github tools?: (yes/no) > ")
    if install in ("yes", "y"):
        for repo in repos:
            #run = "git clone"                  #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            print(f"Cloning {repo}...")
            subprocess.run(["sudo","git","clone",repo], text=True)

    subprocess.run(["python3", "-m", "venv", "env"], check=True)
    pip_path = os.path.join("env", "bin", "pip")
    for piptool in pip_tools:
        print(f"Installing {piptool}...")
        subprocess.run([pip_path, "install", piptool], check=True, text=True)



    gocommand = "go get"
    for gorepo in go_tools:
        print(f"Cloning {gorepo}...")
        subprocess.run([gocommand, gorepo], text=True)

    linking = input(
        "Do you want to 'system-link' the env/ tools so you can use them from anywhere in your system? (yes/no) > ").lower().strip()
    if linking in ("yes", "y"):
        for tool in tools:
            cmd = ["sudo", "ln", "-s", f"env/bin/{tool}", f"/usr/local/bin/{tool}"]
            subprocess.run(cmd, text=True)
            exit()




def My_selection():
    if Select == 2:
        Pac_Manager = int(input("Select your packet manager:\n1 - apt\n2 - pacman\n3 - DNF\nType 1,2 or 3 > ").strip())
        if Pac_Manager == 1:
            runpac = "apt"

        elif Pac_Manager == 2:
            runpac = "pacman"

        elif Pac_Manager == 3:
            runpac = "dnf"
        else:
            print("Wrong input")


    pip_tools = ["socialscan","holehe","requests","impacket","certipy-ad"] ####################################

    go_tools = ["github.com/cgrates/rpcclient","github.com/rookmoot/proxifier"]



    OSINT_tools = ["amass", "theharvester", "httrack",
                    "instaloader", "gallery-dl", "spiderfoot"]

    recon_tools = ["arp-scan", "nmap", "aircrack-ng"]

    enumeration_tools = ["enum4linux", "netexec", "sqlmap","seclists"]

    exploitation_tools = ["mimikatz","ghidra"]

    brute_force = ["hydra", "john"]

    network_tools = ["iptables","netcat-traditional"]

    web_tools = ["curl", "wfuzz", "nikto", "whatweb", "openssl", "masscan"]

    windows_test_tools = ["smbclient", "smbmap", "netexec"
        , "evil-winrm"]

    tools = [*OSINT_tools, *recon_tools, *enumeration_tools, *exploitation_tools, *brute_force, *network_tools,
             *web_tools,
             *windows_test_tools
             ]

    if runpac in ("apt", "dnf"):
        cmd = ["sudo", f"{runpac}", "install", "-y", "--fix-missing", *tools]
        subprocess.run(cmd, text=True)


    elif runpac == "pacman":
        cmd = ["sudo", f"{runpac}", "-S", "--noconfirm", *tools]
        subprocess.run(cmd, text=True)


    subprocess.run(["python3", "-m", "venv", "env"], check=True)
    pip_path = os.path.join("env", "bin", "pip")
    for piptool in pip_tools:
        print(f"Installing {piptool}...")
        subprocess.run([pip_path, "install", piptool], check=True, text=True)



    repos = [
        "https://github.com/s0md3v/Arjun",
        "https://github.com/s0md3v/XSStrike",
        "https://github.com/fin3ss3g0d/secretsdump.py",  ##############################
        "https://github.com/ropnop/kerbrute",
        "https://github.com/jondonas/linux-exploit-suggester-2",
        "https://github.com/strozfriedberg/Windows-Exploit-Suggester",
        "https://github.com/Exbinary/scopelist",  ######
        "https://github.com/Exbinary/webticket",  ######
        "https://github.com/commixproject/commix",
        "https://github.com/EnableSecurity/wafw00f",
        "https://github.com/aboul3la/Sublist3r",
        "https://github.com/SploitHQ/searchsploit",
        "https://github.com/ffuf/ffuf",
        "https://github.com/peass-ng/PEASS-ng",
        "https://github.com/BishopFox/sliver",
        "https://github.com/ShutdownRepo/pywhisker",
        "https://github.com/dirkjanm/PKINITtools"

    ]
    gitcommand = "git clone"
    for repo in repos:
        print(f"Cloning {repo}...")
        subprocess.run([gitcommand, repo], text=True)

    gocommand = "go get"
    for gorepo in go_tools:
        print(f"Cloning {gorepo}...")
        subprocess.run([gocommand, gorepo], text=True)

    linking = input(
        "Do you want to 'system-link' the env/ tools so you can use them from anywhere in your system? (yes/no) > ").lower().strip()
    if linking in ("yes", "y"):
        for tool in tools:
            cmd = ["sudo", "ln", "-s", f"env/bin/{tool}", f"/usr/local/bin/{tool}"]
            subprocess.run(cmd, text=True)
            exit()




def let_me_choose():
    if Select == 3:
        mode = int(input(
            "Do you want to download a category or hand pick tools?:\n1 - Show categories\n2 - Show all tools\nType 1 or 2 > ")) #possible mode 3 - Search toolc
        Pac_Manager = int(input("Select your packet manager:\n1 - apt\n2 - pacman\n3 - DNF\nType 1, 2 or 3 > ").strip())
        if Pac_Manager == 1:
            runpac = "apt"

        elif Pac_Manager == 2:
            runpac = "pacman"

        elif Pac_Manager == 3:
            runpac = "dnf"
        else:
            print("Wrong input")

    OSINT_tools = ["amass", "theharvester", "httrack", "exiftool", "mat2", "sherlock",
                    "instaloader", "mediainfo", "spiderfoot"]

    recon_tools = ["arp-scan", "nmap", "aircrack-ng"]

    enumeration_tools = ["enum4linux", "netexec", "linpeas", "sqlmap","seclists","nuclei"]

    exploitation_tools = ["metasploit-framework", "mimikatz","ghidra"]

    brute_force = ["hydra", "john", "patator"]

    network_tools = ["iptables", "wireshark"]

    web_tools = ["curl", "wfuzz", "gobuster", "nikto", "whatweb", "openssl", "masscan"]

    windows_test_tools = ["smbclient", "smbmap", "bloodhound", "netexec", "powerSploit"
        , "evil-winrm"]

    tools = [*OSINT_tools, *recon_tools, *enumeration_tools, *exploitation_tools, *brute_force, *network_tools,
             *web_tools,
             *windows_test_tools
             ]



    if mode == 1:
        print(
            "--------------\n[ CATEGORIES ]:\n--------------\n0 - OSINT\n1 - Recon\n2 - Enumeration\n3 - Exploitation\n4 - Brute Forcing\n--------------\n5 - Network\n6 - Web\n7 - Windows\n--------------\n8 - Python Scripts / GitHub\n9 - Useful URLs")
        category = int(input("Select Category. Type 1, 2, ... > "))

        if category == 0:
            print("--------------")
            print("0 - OSINT")
            print("--------------")
            print("\n".join(OSINT_tools))
            print("--------------")
            install = input("Do you want to install this category?: (yes/no)\n > ").strip().lower()
            if install in ("yes","y"):

                if runpac in ("apt", "dnf"):
                    cmd = ["sudo", f"{runpac}", "install", "-y", *OSINT_tools]
                    subprocess.run(cmd, text=True)


                elif runpac == "pacman":
                    cmd = ["sudo", f"{runpac}", "-S", "--noconfirm", *OSINT_tools]
                    subprocess.run(cmd, text=True)

            linking = input(
                "Do you want to 'system-link' the tools so you can use them from anywhere in your system? (yes/no) > ").lower().strip()
            if linking in ("yes", "y"):
                for tool in OSINT_tools:
                    cmd = ["sudo", "ln", "-s", f"env/bin/{tool}", f"/usr/local/bin/{tool}"]
                    subprocess.run(cmd, text=True)
                    exit()

        if category == 1:
            print("--------------")
            print("1 - Recon")
            print("--------------")
            print("\n".join(recon_tools))
            print("--------------")
            install = input("Do you want to install this category?: (yes/no)\n > ").strip().lower()
            if install in ("yes", "y"):
                if runpac in ("apt", "dnf"):
                    cmd = ["sudo", f"{runpac}", "install", "-y", *recon_tools]
                    subprocess.run(cmd, text=True)


                elif runpac == "pacman":
                    cmd = ["sudo", f"{runpac}", "-S", "--noconfirm", *recon_tools]
                    subprocess.run(cmd, text=True)

            linking = input(
                "Do you want to 'system-link' the tools so you can use them from anywhere in your system? (yes/no) > ").lower().strip()
            if linking in ("yes", "y"):
                for tool in recon_tools:
                    cmd = ["sudo", "ln", "-s", f"env/bin/{tool}", f"/usr/local/bin/{tool}"]
                    subprocess.run(cmd, text=True)
                    exit()

        elif category == 2:
            print("--------------")
            print("2 - Enumeration")
            print("--------------")
            print("\n".join(enumeration_tools))
            print("--------------")
            install = input("Do you want to install this category?: (yes/no)\n > ").strip().lower()
            if install in ("yes", "y"):
                if runpac in ("apt", "dnf"):
                    cmd = ["sudo", f"{runpac}", "install", "-y", *enumeration_tools]
                    subprocess.run(cmd, text=True)


                elif runpac == "pacman":
                    cmd = ["sudo", f"{runpac}", "-S", "--noconfirm", *enumeration_tools]
                    subprocess.run(cmd, text=True)

            linking = input(
                "Do you want to 'system-link' the tools so you can use them from anywhere in your system? (yes/no) > ").lower().strip()
            if linking in ("yes", "y"):
                for tool in enumeration_tools:
                    cmd = ["sudo", "ln", "-s", f"env/bin/{tool}", f"/usr/local/bin/{tool}"]
                    subprocess.run(cmd, text=True)
                    exit()

        elif category == 3:
            print("--------------")
            print("3 - Exploitation")
            print("--------------")
            print("\n".join(exploitation_tools))
            print("--------------")
            install = input("Do you want to install this category?: (yes/no)\n > ").strip().lower()
            if install in ("yes", "y"):
                if runpac in ("apt", "dnf"):
                    cmd = ["sudo", f"{runpac}", "install", "-y", *exploitation_tools]
                    subprocess.run(cmd, text=True)


                elif runpac == "pacman":
                    cmd = ["sudo", f"{runpac}", "-S", "--noconfirm", *exploitation_tools]
                    subprocess.run(cmd, text=True)

            linking = input(
                "Do you want to 'system-link' the tools so you can use them from anywhere in your system? (yes/no) > ").lower().strip()
            if linking in ("yes", "y"):
                for tool in exploitation_tools:
                    cmd = ["sudo", "ln", "-s", f"env/bin/{tool}", f"/usr/local/bin/{tool}"]
                    subprocess.run(cmd, text=True)
                    exit()

        elif category == 4:
            print("--------------")
            print("4 - Brute Forcing")
            print("--------------")
            print("\n".join(brute_force))
            print("--------------")
            install = input("Do you want to install this category?: (yes/no)\n > ").strip().lower()
            if install in ("yes", "y"):
                if runpac in ("apt", "dnf"):
                    cmd = ["sudo", f"{runpac}", "install", "-y", *brute_force]
                    subprocess.run(cmd, text=True)


                elif runpac == "pacman":
                    cmd = ["sudo", f"{runpac}", "-S", "--noconfirm", *brute_force]
                    subprocess.run(cmd, text=True)

            linking = input(
                "Do you want to 'system-link' the tools so you can use them from anywhere in your system? (yes/no) > ").lower().strip()
            if linking in ("yes", "y"):
                for tool in brute_force:
                    cmd = ["sudo", "ln", "-s", f"env/bin/{tool}", f"/usr/local/bin/{tool}"]
                    subprocess.run(cmd, text=True)
                    exit()


        elif category == 5:
            print("--------------")
            print("5 - Network")
            print("--------------")
            print("\n".join(network_tools))
            print("--------------")
            install = input("Do you want to install this category?: (yes/no)\n > ").strip().lower()
            if install in ("yes", "y"):
                if runpac in ("apt", "dnf"):
                    cmd = ["sudo", f"{runpac}", "install", "-y", *network_tools]
                    subprocess.run(cmd, text=True)


                elif runpac == "pacman":
                    cmd = ["sudo", f"{runpac}", "-S", "--noconfirm", *network_tools]
                    subprocess.run(cmd, text=True)

            linking = input(
                "Do you want to 'system-link' the tools so you can use them from anywhere in your system? (yes/no) > ").lower().strip()
            if linking in ("yes", "y"):
                for tool in network_tools:
                    cmd = ["sudo", "ln", "-s", f"env/bin/{tool}", f"/usr/local/bin/{tool}"]
                    subprocess.run(cmd, text=True)
                    exit()

        elif category == 6:
            print("--------------")
            print("6 - Web")
            print("--------------")
            print("\n".join(web_tools))
            print("--------------")
            install = input("Do you want to install this category?: (yes/no)\n > ").strip().lower()
            if install in ("yes", "y"):
                if runpac in ("apt", "dnf"):
                    cmd = ["sudo", f"{runpac}", "install", "-y", *web_tools]
                    subprocess.run(cmd, text=True)


                elif runpac == "pacman":
                    cmd = ["sudo", f"{runpac}", "-S", "--noconfirm", *web_tools]
                    subprocess.run(cmd, text=True)

            linking = input(
                "Do you want to 'system-link' the tools so you can use them from anywhere in your system? (yes/no) > ").lower().strip()
            if linking in ("yes", "y"):
                for tool in web_tools:
                    cmd = ["sudo", "ln", "-s", f"env/bin/{tool}", f"/usr/local/bin/{tool}"]
                    subprocess.run(cmd, text=True)
                    exit()


        elif category == 7:

            print("--------------")
            print("7 - Windows")
            print("--------------")
            print("\n".join(windows_test_tools))
            print("--------------")
            install = input("Do you want to install this category?: (yes/no)\n > ").strip().lower()
            if install in ("yes", "y"):
                if runpac in ("apt", "dnf"):
                    cmd = ["sudo", f"{runpac}", "install", "-y", *windows_test_tools]
                    subprocess.run(cmd, text=True)


                elif runpac == "pacman":
                    cmd = ["sudo", f"{runpac}", "-S", "--noconfirm", *windows_test_tools]
                    subprocess.run(cmd, text=True)

            linking = input(
                "Do you want to 'system-link' the tools so you can use them from anywhere in your system? (yes/no) > ").lower().strip()
            if linking in ("yes", "y"):
                for tool in windows_test_tools:
                    cmd = ["sudo", "ln", "-s", f"env/bin/{tool}", f"/usr/local/bin/{tool}"]
                    subprocess.run(cmd, text=True)
                    exit()




        elif category == 8:
            runpac = "git clone"

            repos = [
                "https://github.com/s0md3v/Photon",
                "https://github.com/s0md3v/Arjun",
                "https://github.com/s0md3v/XSStrike",
                "https://github.com/fin3ss3g0d/secretsdump.py",  ##############################
                "https://github.com/ropnop/kerbrute",
                "https://github.com/jondonas/linux-exploit-suggester-2",
                "https://github.com/strozfriedberg/Windows-Exploit-Suggester",
                "https://github.com/Exbinary/scopelist",  ######
                "https://github.com/Exbinary/webticket",  ######
                "https://github.com/commixproject/commix",
                "https://github.com/EnableSecurity/wafw00f",
                "https://github.com/aboul3la/Sublist3r",
                "https://github.com/SploitHQ/searchsploit",
                "https://github.com/ffuf/ffuf",
                "https://github.com/peass-ng/PEASS-ng",
                "https://github.com/BishopFox/sliver",
                "https://github.com/ShutdownRepo/pywhisker",
                "https://github.com/dirkjanm/PKINITtools"

            ]

            for i, rep in enumerate(repos,start=1):
                print(
                    f"|---------------------------------------------------------------|\n{i} - {rep}")
            install = int(input("Do you want to 1 - Clone all the repos or 2 - Choose? Type 1 or 2 > "))

            if install == 1:

                for repo in repos:
                    print(f"Cloning {repo}...")
                    subprocess.run(runpac, repo, text=True)

            elif install == 2:
                repo_selection = input(
                    "|------------------------|\nType the number for each repo you want to install: (Example > 1 2 6) > ")

                try:
                    chosen_numbers = [int(num) for num in repo_selection.split()]
                except ValueError:
                    print("Error: Please enter only numbers separated by spaces.")
                    exit()

                # Filter out invalid numbers
                chosen_repos = [repos[i - 1] for i in chosen_numbers if 1 <= i <= len(repos)]

                if not chosen_repos:
                    print("Error: No valid selections.")
                    exit()

                print(f"\nYou selected: {', '.join(chosen_repos)}")

                for repo in chosen_repos:

                    cmd = ["git","clone", repo]


                    print(f"--------------------------------------------------\n  +   Installing {repo}...\n--------------------------------------------------")
                    subprocess.run(cmd, text=True)




        elif category == 9:
            URLs = [
                "https://crackstation.net/",
                "https://www.revshells.com/",
                "https://gtfobins.github.io/",
                "https://book.hacktricks.wiki/en/index.html",

            ]
            print("--------------\n[ URLs ]:")
            print("----------------------------------------------------------------------------------------------")
            print(URLs[0] + "   -->   Free Password Hash Cracker")
            print("----------------------------------------------------------------------------------------------")
            print(URLs[1] + "   -->   Reverse Shell Generator")
            print("----------------------------------------------------------------------------------------------")
            print(URLs[2] + "   -->   Unix Binaries List for PrivEsc")
            print("----------------------------------------------------------------------------------------------")
            print(URLs[3] + "   -->   Hack Wiki")


        else:
            print("Category not found")




    # Hand pick
    elif mode == 2:
        print("----------------------------------------------------------------------------------------------\n* searchsploit , PEAS-ng (WinPeas, LinPeas) , Kerbrute , ffuf and more in python / GitHub category *\n----------------------------------------------------------------------------------------------")
        print("  --------------\n  [ ALL TOOLS ]:")
        for i, tool in enumerate(tools, start=1):      # enumerate(tools, start=1) automatically gives each tool a number starting at 1.
            print(f"|------------------------|\n{i} - {tool}")                     # You can later refer to a tool by its index if needed: tools[0] is "arp-scan"


        tool_selection = input("|------------------------|\nType the number for each tool you want to install: (Example > 1 2 6 12) > ")

        try:
            chosen_numbers = [int(num) for num in tool_selection.split()]
        except ValueError:
            print("Error: Please enter only numbers separated by spaces.")
            exit()


        chosen_tools = [tools[i - 1] for i in chosen_numbers if 1 <= i <= len(tools)]

        if not chosen_tools:
            print("Error: No valid selections.")
            exit()

        print(f"\nYou selected: {', '.join(chosen_tools)}")


        for tool in chosen_tools:
            if runpac in ("apt", "dnf"):
                cmd = ["sudo", runpac, "install", "-y", tool]
            elif runpac == "pacman":
                cmd = ["sudo", "pacman", "--noconfirm", tool]
            else:
                print("Unsupported package manager")
                break

            print(f"-------------------------\n  +   Installing {tool}...\n-------------------------")
            subprocess.run(cmd, text=True)

        linking = input(
            "-----------------------------------------------------------------------------\nDo you want to 'system-link' the env/ tools so you can use them from anywhere in your system? ( yes [recommended] / no ) > ").lower().strip()
        if linking in ("yes", "y"):
            for tool in tools:
                cmd = ["sudo", "ln", "-s", f"env/bin/{tool}", f"/usr/local/bin/{tool}"]
                subprocess.run(cmd, text=True)
                exit()


    print("-----------------------------------------------------------------------------\n"
          "For more tools, I recommend you to check GitHub tools in category selection")



def main():
    if Select == 1:
        full_bundle()
        exit()
    elif Select == 2:
        My_selection()
        exit()
    elif Select == 3:
        let_me_choose()
        exit()
    else:
        print("error: Wrong input")
        exit()


if __name__ == main():
    reexec_with_sudo()
    main()
