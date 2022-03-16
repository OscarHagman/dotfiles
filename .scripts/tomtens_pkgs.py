# args
ARG_ALL = "all"
ARG_APT = "apt"
ARG_SNAP = "snap"
ARG_THIRD_PARTY = "third-party"

# Variables
INSTALL_METHOD = "install_method"
INSTALL_METHOD_PPA = "ppa"
INSTALL_METHOD_CMD = "cmd"
DEPEND = "dependencies"
PKG_ARGS = "package_arguments"

# PACKAGES
# apt
AUDACITY = {"name": "audacity"}
BLUEMAN = {"name": "blueman"}
DISCORD = {"name": "discord"}
CURL = {"name": "curl"}
FLAMESHOT = {"name": "flameshot"}
GIT = {"name": "git"}
GPG = {"name": "gpg"}
HTOP = {"name": "htop"}
INSOMNIA = {"name": "insomnia"}
KGPG = {"name": "kgpg"}
MPV = {"name": "mpv"}
NVIM = {"name": "neovim"}
PAVU = {"name": "pavucontrol"}
PIP3 = {"name": "python3-pip"}
TORRENT = {"name": "qbittorrent"}
SNAP = {"name": "snap"}
TERRAFORM = {"name": "terraform"}
TOR = {"name": "tor"}
YT_DL = {"name": "youtube-dl"}
# apt packages with extra steps
ANSIBLE = {
    "name": "ansible",
    INSTALL_METHOD: INSTALL_METHOD_PPA,
    DEPEND: [
        "software-properties-common"
    ],
    INSTALL_METHOD_PPA: "ppa:ansible/ansible"
}
DOCKER = {
    "name": "docker",
    INSTALL_METHOD: INSTALL_METHOD_CMD,
    DEPEND: [
        "curl"
    ],
    INSTALL_METHOD_CMD: "curl -fsSL https://get.docker.com | sh"
}

# snap
VSCODE = {
    "name": "code",
    PKG_ARGS: "--classic"
}
TEAMS = {"name": "teams"}
SPOTIFY = {"name": "spotify"}
# third party
alacritty_colorscheme = {
    "name": "alacritty-colorscheme",
    "url": "https://github.com/toggle-corp/alacritty-colorscheme",
    DEPEND: PIP3
}

APT_PACKAGES = [
    ANSIBLE,
    DOCKER,
    AUDACITY,
    BLUEMAN,
    DISCORD,
    CURL,
    FLAMESHOT,
    GIT,
    GPG,
    HTOP,
    INSOMNIA,
    KGPG,
    MPV,
    NVIM,
    PAVU,
    PIP3,
    TORRENT,
    SNAP,
    TERRAFORM,
    TOR,
    YT_DL
]

SNAP_PACKAGES = [
    VSCODE,
    TEAMS,
    SPOTIFY
]

THIRD_PARTY_PACKAGES = [
    alacritty_colorscheme
]