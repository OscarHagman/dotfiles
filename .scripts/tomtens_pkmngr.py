#!/usr/bin/python3

import tomtens_pkgs as pk
import os
import argparse

parser = argparse.ArgumentParser()
# parser.add_argument("-li", "--list-installed", help="List all installed packages")
# parser.add_argument("-ln", "--list-not-installed", help="List not installed packages")
# parser.add_argument("-uA", "--uninstall-all", help="Uninstall all packages")
# parser.add_argument("-ua", "--uninstall-apt", help="Uninstall all apt packages")
# parser.add_argument("-ua", "--uninstall-snap", help="Uninstall all snap packages")
# parser.add_argument("-ut", "--uninstall-third-party", help="Uninstall all third-party packages")
# parser.add_argument("-ap", "--add-package", help="Add package to list of packages")
install_help = f"install {pk.ARG_ALL}, {pk.ARG_APT}, {pk.ARG_SNAP} or {pk.ARG_THIRD_PARTY} packages"
parser.add_argument("-i", "--install", help=install_help)

subparsers = parser.add_subparsers(help="sub-command help", dest="command")
subparsers.add_parser("ls", help="List all packages")
args = parser.parse_args()

def install_all_packages():
    install_apt_packages()
    install_snap_packages()
    # install_third_party_packages()

def install_apt_packages():
    print("\nINSTALLING APT PACKAGES\n")
    os.system("sudo apt update")
    for package in pk.APT_PACKAGES:
        if pk.DEPEND in package:
            for dependency in package[pk.DEPEND]:
                print(f'\ninstalling dependency "{dependency}"\n')
                os.system(f'sudo apt install {dependency} -y')
        
        if pk.INSTALL_METHOD in package:
            if package[pk.INSTALL_METHOD] == pk.INSTALL_METHOD_PPA:
                print(f'\ninstalling {package["name"]}\n')
                os.system(f'sudo add-apt-repository --update {package[pk.INSTALL_METHOD_PPA]} -y')
                os.system(f'sudo apt install {package["name"]} -y')
            elif package[pk.INSTALL_METHOD] == pk.INSTALL_METHOD_CMD:
                print(f'installing package["name"]')
                os.system(package[pk.INSTALL_METHOD_CMD])
        else:
            os.system(f'sudo apt install {package["name"]} -y')

def install_snap_packages():
    print("\nINSTALLING SNAP PACKAGES\n")
    os.system("sudo apt update")
    os.system("sudo apt install snap -y")
    for package in pk.SNAP_PACKAGES:
        os_cmd = f'sudo snap install {package["name"]}'
        if pk.PKG_ARGS in package:
            os_cmd += f' {package[pk.PKG_ARGS]}'
        os.system(os_cmd)

def install_third_party_packages():
    print("\nINSTALLING THIRD PARTY PACKAGES\n")
    print("install third party")

def list_all_packages():
    print("\nAPT PACKAGES:")
    for apt in pk.APT_PACKAGES:
        print("-", apt["name"])

    print("\nSNAP PACKAGES:")
    for snap in pk.SNAP_PACKAGES:
        print("-", snap["name"])

    print("\nTHIRD PARTY PACKAGES:")
    for third_party in pk.THIRD_PARTY_PACKAGES:
        print("-", third_party["name"])

def uninstall_all():
    pass

def main():
    if args.install:
        if args.install == pk.ARG_ALL:
            install_all_packages()
        elif args.install == pk.ARG_APT:
            install_apt_packages()
        elif args.install == pk.ARG_SNAP:
            install_snap_packages()
        elif args.install == pk.ARG_THIRD_PARTY:
            install_third_party_packages()
        else:
            print(f'"{args.install}" argument not recognized, type "-h" for help')
    elif args.command == "ls":
        list_all_packages()

if __name__ == "__main__":
    main()
