#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import subprocess

# ── ANSI Colors ──────────────────────────────────────────────────────────────
RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"

WHITE   = "\033[97m"
CREAM   = "\033[93m"
GREY    = "\033[37m"
LGREY   = "\033[90m"
BROWN   = "\033[33m"
CYAN    = "\033[96m"
PINK    = "\033[95m"

def clear():
    os.system("clear")

def slow_print(text, delay=0.012):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def open_link(url):
    try:
        subprocess.run(["termux-open-url", url])
    except FileNotFoundError:
        try:
            subprocess.run(["xdg-open", url])
        except Exception:
            import webbrowser
            webbrowser.open(url)

def draw_header():
    clear()

    banner = f"""
{WHITE}{BOLD}
   ██████╗  ██████╗ ███╗   ██╗███████╗ ██████╗ ██████╗
   ██╔══██╗██╔═══██╗████╗  ██║██╔════╝██╔════╝██╔═══██╗
   ██████╔╝██║   ██║██╔██╗ ██║█████╗  ██║     ██║   ██║
   ██╔══██╗██║   ██║██║╚██╗██║██╔══╝  ██║     ██║   ██║
   ██████╔╝╚██████╔╝██║ ╚████║███████╗╚██████╗╚██████╔╝
   ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═════╝
{RESET}"""

    dog_ascii = f"""
{WHITE}              / \\__
{WHITE}         (  (  /  ⌂ \\       {CREAM}{BOLD}✦  Fred — my fluffy boy  ✦{RESET}
{WHITE}          \\  \\ \\___/        {GREY}  pure white & full of love
{WHITE}          /__|___|          {LGREY}  the goodest boy 🐾{RESET}
{WHITE}         (    )  )
{WHITE}          \\__;__/
{RESET}"""

    border = f"{GREY}{'─'*58}{RESET}"

    print(banner)
    print(border)
    print(dog_ascii)
    print(border)

    info_lines = [
        f"  {CREAM}{BOLD}👤  Handle    {RESET}{WHITE}» boneco_r8q{RESET}",
        f"  {CREAM}{BOLD}📲  Telegram  {RESET}{CYAN}» t.me/boneco_r8q{RESET}",
        f"  {CREAM}{BOLD}🎵  TikTok    {RESET}{PINK}» @boneco_preparado{RESET}",
        f"  {CREAM}{BOLD}🐶  Fred's Site {RESET}{WHITE}» fredlabs.qzz.io{RESET}",
    ]

    print()
    for line in info_lines:
        slow_print(line, delay=0.008)
        time.sleep(0.05)

    print()
    print(f"  {LGREY}{'·'*54}{RESET}")
    print()

def draw_menu():
    menu = f"""
  {CREAM}{BOLD}  Where do you want to go?{RESET}

  {WHITE}{BOLD}  [ 1 ] {RESET}{CYAN}✈  Telegram     {LGREY}— t.me/boneco_r8q{RESET}
  {WHITE}{BOLD}  [ 2 ] {RESET}{PINK}♪  TikTok       {LGREY}— @boneco_preparado{RESET}
  {WHITE}{BOLD}  [ 3 ] {RESET}{WHITE}🐾 Fred's Website {LGREY}— fredlabs.qzz.io{RESET}
  {WHITE}{BOLD}  [ 0 ] {RESET}{LGREY}✕  Exit{RESET}

  {GREY}{'─'*40}{RESET}
  {CREAM}{BOLD}  » {RESET}"""

    sys.stdout.write(menu)
    sys.stdout.flush()

def paw_animation():
    paws = ["🐾", "  🐾", "    🐾", "      🐾"]
    for p in paws:
        sys.stdout.write(f"\r  {WHITE}{p}{RESET}    ")
        sys.stdout.flush()
        time.sleep(0.12)
    print(f"\r  {WHITE}🐾🐾🐾 Opening...{RESET}        ")
    time.sleep(0.5)

def main():
    links = {
        "1": ("Telegram",           "https://t.me/boneco_r8q"),
        "2": ("TikTok",             "https://www.tiktok.com/@boneco_preparado?_r=1&_t=ZS-94gqoRgh8In"),
        "3": ("Fred's Website 🐶",  "https://www.fredlabs.qzz.io/"),
    }

    draw_header()

    while True:
        draw_menu()

        try:
            choice = input().strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n\n  {LGREY}See you! 🐾{RESET}\n")
            sys.exit(0)

        if choice == "0":
            print(f"\n  {CREAM}Take care! 🐾{RESET}\n")
            time.sleep(0.8)
            clear()
            sys.exit(0)

        elif choice in links:
            name, url = links[choice]
            print()
            paw_animation()
            print(f"  {CREAM}{BOLD}Opening {name}...{RESET}")
            print(f"  {LGREY}{url}{RESET}\n")
            open_link(url)
            time.sleep(1.5)
            draw_header()

        else:
            print(f"\n  {BROWN}⚠  Invalid option. Try 1, 2, 3 or 0.{RESET}")
            time.sleep(1.2)
            draw_header()

if __name__ == "__main__":
    main()
    
