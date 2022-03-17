#!/usr/bin/python3

from importlib.abc import Loader
import tomtens_pkgs as pk
import os
import sys
import argparse
import yaml

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
    install_apt_packages(pk.APT_PACKAGES)
    install_snap_packages(pk.SNAP_PACKAGES)
    # install_third_party_packages(pk.THIRD_PARTY_PACKAGES)

def install_apt_packages(packages):
    print("\nINSTALLING APT PACKAGES\n")
    os.system("sudo apt update")
    for package in packages:
        if pk.DEPEND in package:
            for dependency in package[pk.DEPEND]:
                print(f'\ninstalling {package["name"]} dependency "{dependency}"\n')
                os.system(f'sudo apt install {dependency} -y')
        
        if pk.INSTALL_METHOD in package:
            if package[pk.INSTALL_METHOD] == pk.INSTALL_METHOD_PPA:
                print(f'\ninstalling {package["name"]}\n')
                os.system(f'sudo add-apt-repository --update {package[pk.INSTALL_METHOD_PPA]} -y')
                os.system(f'sudo apt install {package["name"]} -y')
            elif package[pk.INSTALL_METHOD] == pk.INSTALL_METHOD_CMD:
                print(f'installing {package["name"]}')
                os.system(package[pk.INSTALL_METHOD_CMD])
        else:
            os.system(f'sudo apt install {package["name"]} -y')

def install_snap_packages(packages):
    print("\nINSTALLING SNAP PACKAGES\n")
    os.system("sudo apt update")
    os.system("sudo apt install snap -y")
    for package in packages:
        os_cmd = f'sudo snap install {package["name"]}'
        if pk.PKG_ARGS in package:
            os_cmd += f' {package[pk.PKG_ARGS]}'
        os.system(os_cmd)

def install_third_party_packages(packages):
    print("\nINSTALLING THIRD PARTY PACKAGES\n")
    for package in packages:
        print(f'installing {package["name"]}')

def get_packages_index(packages: list) -> list:
    """
    Return list of valid choices (index numbers)
    Can be used just for listing packages
    """
    valid_choices = []
    for i, package in enumerate(packages):
        print(f'[{i}] {package["name"]}')
        valid_choices.append(i)
    return valid_choices

def uninstall_all():
    pass

def choose_packages(package_manager_list: list):
    get_packages_index(package_manager_list)
    
    chosen_packages = []
    while True:
        try:
            choices = input(": ")
            choices = choices.split(" ")
            for choice in choices:
                choice = int(choice)
                chosen_packages.append(package_manager_list[choice])
            break
        except ValueError:
            if choice == "":
                break
            print(f'Invalid input "{choice}"')
            print("Start over")
            chosen_packages = []
        except IndexError:
            print(f'There is no package with index number: {choice}')
            print("Start over")
            chosen_packages = []
        except KeyboardInterrupt:
            print("\nGood bye")
            sys.exit()
        except Exception as err:
            print(f'UNEXPECTED ERROR:\n\n{err}')
            sys.exit()
    return chosen_packages

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
        print("\nAPT PACKAGES:")
        get_packages_index(pk.APT_PACKAGES)
        print("\nSNAP PACKAGES:")
        get_packages_index(pk.SNAP_PACKAGES)
        print("\nTHIRD PARTY PACKAGES:")
        get_packages_index(pk.THIRD_PARTY_PACKAGES)
    else:
        print("\nChoose packages you want to install (enter index numbers seperated with a space)")
        print("For example\n: 0 19 7 12")
        print("\nAPT PACKAGES:")
        chosen_apt_packages = choose_packages(pk.APT_PACKAGES)
        print("\nSNAP PACKAGES:")
        chosen_snap_packages = choose_packages(pk.SNAP_PACKAGES)
        print("\nTHIRD PARTY PACKAGES:")
        chosen_third_party_packages = choose_packages(pk.THIRD_PARTY_PACKAGES)
        
        if chosen_apt_packages != [] or chosen_snap_packages != [] or chosen_third_party_packages != []:
            print("\nChosen packages:")
            [print("-",package["name"]) for package in chosen_apt_packages]
            [print("-",package["name"]) for package in chosen_snap_packages]
            [print("-",package["name"]) for package in chosen_third_party_packages]
            print("\nInstall packages? (y/n)")
            while True:
                yes_or_no = input(": ")
                if yes_or_no.lower() == "y":
                    install_apt_packages(chosen_apt_packages)
                    install_snap_packages(chosen_snap_packages)
                    install_third_party_packages(chosen_third_party_packages)
                    break
                elif yes_or_no.lower() == "n":
                    main()
                    break
                else:
                    print(f'Invalid input "{yes_or_no}"')
        else:
            print("\nNo packages were selected")
            main()

def try_yaml():
    # READ YAML
    # with open("tomtens_packages.yaml", "r") as yaml_file:
    #     data = yaml.safe_load(yaml_file)
    #     print(data)

    # WRITE YAML
    # users = [{'name': 'John Doe', 'occupation': 'gardener'},
    #         {'name': 'Lucy Black', 'occupation': 'teacher'}]

    # with open('users.yaml', 'w') as f:
    #     data = yaml.dump(users, f)

if __name__ == "__main__":
    #main()
    try_yaml()
