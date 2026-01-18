#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  ██████╗  ██████╗ ██╗     ██╗██╗  ██╗███████╗    ████████╗ ██████╗  ██████╗ ██╗     ║
║ ██╔════╝ ██╔═══██╗██║     ██║██║ ██╔╝██╔════╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ║
║ ██║  ███╗██║   ██║██║     ██║█████╔╝ █████╗         ██║   ██║   ██║██║   ██║██║     ║
║ ██║   ██║██║   ██║██║     ██║██╔═██╗ ██╔══╝         ██║   ██║   ██║██║   ██║██║     ║
║ ╚██████╔╝╚██████╔╝███████╗██║██║  ██╗███████╗       ██║   ╚██████╔╝╚██████╔╝███████╗║
║  ╚═════╝  ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═╝╚══════╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝║
║                    ✨ YOUTUBE TOOL PRO MAX ULTRA ✨                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import requests
import time
import os
import sys
import math
import threading
from time import sleep
import random
import json
from datetime import datetime

try:
    import colorama
    from colorama import Fore, Back, Style, init
    init(autoreset=True)
except ImportError:
    os.system('pip install colorama')
    import colorama
    from colorama import Fore, Back, Style, init
    init(autoreset=True)

# ═══════════════════════════════════════════════════════════════════════════════
# 🎨 ULTRA RAINBOW & ANIMATION SYSTEM
# ═══════════════════════════════════════════════════════════════════════════════

class UltraColors:
    """🌈 Ultra Premium Color System"""
    
    # Rainbow Colors
    RAINBOW = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    
    # Neon Colors
    NEON = [
        Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTGREEN_EX,
        Fore.LIGHTCYAN_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX
    ]
    
    # Fire Colors
    FIRE = [Fore.RED, Fore.LIGHTRED_EX, Fore.YELLOW, Fore.LIGHTYELLOW_EX]
    
    # Ocean Colors
    OCEAN = [Fore.BLUE, Fore.CYAN, Fore.LIGHTCYAN_EX, Fore.LIGHTBLUE_EX]
    
    # Matrix Colors
    MATRIX = [Fore.GREEN, Fore.LIGHTGREEN_EX]

    @staticmethod
    def rainbow_text(text, bold=True):
        """🌈 Create beautiful rainbow text"""
        result = ""
        colors = UltraColors.RAINBOW
        for i, char in enumerate(text):
            color = colors[i % len(colors)]
            if bold:
                result += f"{color}{Style.BRIGHT}{char}"
            else:
                result += f"{color}{char}"
        return result + Style.RESET_ALL

    @staticmethod
    def neon_text(text):
        """💡 Create neon glowing text"""
        result = ""
        colors = UltraColors.NEON
        for i, char in enumerate(text):
            color = colors[i % len(colors)]
            result += f"{color}{Style.BRIGHT}{char}"
        return result + Style.RESET_ALL

    @staticmethod
    def fire_text(text):
        """🔥 Create fire effect text"""
        result = ""
        colors = UltraColors.FIRE
        for i, char in enumerate(text):
            color = colors[i % len(colors)]
            result += f"{color}{Style.BRIGHT}{char}"
        return result + Style.RESET_ALL

    @staticmethod
    def wave_text(text, offset=0):
        """🌊 Create wave effect text"""
        result = ""
        colors = UltraColors.OCEAN
        for i, char in enumerate(text):
            color = colors[(i + offset) % len(colors)]
            result += f"{color}{Style.BRIGHT}{char}"
        return result + Style.RESET_ALL

    @staticmethod
    def glitch_text(text):
        """⚡ Create glitch effect text"""
        glitch_chars = ['█', '▓', '▒', '░', '│', '┤', '╡', '╢', '╖', '╕']
        result = ""
        for char in text:
            if random.random() < 0.1:
                result += f"{Fore.RED}{Style.BRIGHT}{random.choice(glitch_chars)}"
            else:
                color = random.choice(UltraColors.NEON)
                result += f"{color}{Style.BRIGHT}{char}"
        return result + Style.RESET_ALL


class UltraAnimations:
    """✨ Ultra Premium Animation System"""

    # Special Characters Collections
    SPINNERS = {
        'dots': ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'],
        'arrows': ['←', '↖', '↑', '↗', '→', '↘', '↓', '↙'],
        'bouncing': ['⠁', '⠂', '⠄', '⡀', '⢀', '⠠', '⠐', '⠈'],
        'circle': ['◐', '◓', '◑', '◒'],
        'square': ['◰', '◳', '◲', '◱'],
        'star': ['✶', '✸', '✹', '✺', '✹', '✷'],
        'moon': ['🌑', '🌒', '🌓', '🌔', '🌕', '🌖', '🌗', '🌘'],
        'clock': ['🕐', '🕑', '🕒', '🕓', '🕔', '🕕', '🕖', '🕗', '🕘', '🕙', '🕚', '🕛'],
        'hearts': ['💗', '💖', '💝', '💘', '💕', '💓', '💞', '💟'],
        'fire': ['🔥', '💥', '✨', '⚡', '💫', '🌟', '⭐', '🔆'],
    }

    PROGRESS_BARS = {
        'blocks': ['░', '▒', '▓', '█'],
        'smooth': ['▏', '▎', '▍', '▌', '▋', '▊', '▉', '█'],
        'circles': ['○', '◔', '◑', '◕', '●'],
        'arrows': ['▸', '▹', '►', '▻'],
    }

    BORDERS = {
        'double': ['╔', '╗', '╚', '╝', '═', '║'],
        'single': ['┌', '┐', '└', '┘', '─', '│'],
        'heavy': ['┏', '┓', '┗', '┛', '━', '┃'],
        'rounded': ['╭', '╮', '╰', '╯', '─', '│'],
        'fancy': ['╔', '╗', '╚', '╝', '═', '║', '╠', '╣', '╦', '╩', '╬'],
    }

    @staticmethod
    def clear_screen():
        """🧹 Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def typing_effect(text, delay=0.03, rainbow=True):
        """⌨️ Ultra typing animation with rainbow"""
        colors = UltraColors.RAINBOW
        for i, char in enumerate(text):
            if rainbow:
                color = colors[i % len(colors)]
                sys.stdout.write(f"{color}{Style.BRIGHT}{char}")
            else:
                sys.stdout.write(f"{Fore.CYAN}{Style.BRIGHT}{char}")
            sys.stdout.flush()
            sleep(delay)
        print()

    @staticmethod
    def wave_animation(text, cycles=3, delay=0.1):
        """🌊 Wave text animation"""
        for cycle in range(cycles * len(text)):
            wave_text = UltraColors.wave_text(text, cycle)
            sys.stdout.write(f"\r{wave_text}")
            sys.stdout.flush()
            sleep(delay)
        print()

    @staticmethod
    def loading_spinner(label="Loading", duration=3, style='dots'):
        """🔄 Ultra loading spinner with rainbow"""
        spinner = UltraAnimations.SPINNERS.get(style, UltraAnimations.SPINNERS['dots'])
        colors = UltraColors.NEON
        iterations = int(duration * 10)
        
        for i in range(iterations):
            char = spinner[i % len(spinner)]
            color = colors[i % len(colors)]
            
            # Create rainbow label
            rainbow_label = UltraColors.rainbow_text(label)
            
            sys.stdout.write(
                f"\r{color}{Style.BRIGHT} {char} {rainbow_label} {char} "
            )
            sys.stdout.flush()
            sleep(0.1)
        
        sys.stdout.write(f"\r{Fore.GREEN}{Style.BRIGHT}✅ {label} Complete!{' ' * 20}\n")

    @staticmethod
    def progress_bar(label="Processing", duration=2, width=40):
        """📊 Ultra beautiful progress bar"""
        colors = UltraColors.RAINBOW
        
        for i in range(width + 1):
            percentage = int((i / width) * 100)
            filled = i
            empty = width - i
            
            # Create colorful progress bar
            bar = ""
            for j in range(filled):
                color = colors[j % len(colors)]
                bar += f"{color}{Style.BRIGHT}█"
            bar += f"{Fore.WHITE}{'░' * empty}"
            
            # Rainbow percentage
            pct_text = UltraColors.rainbow_text(f"{percentage:3d}%")
            
            sys.stdout.write(
                f"\r{Fore.CYAN}{Style.BRIGHT}⟨ {bar} {Fore.CYAN}⟩ {pct_text} "
                f"{UltraColors.fire_text(label)}"
            )
            sys.stdout.flush()
            sleep(duration / width)
        
        print(f"\r{Fore.GREEN}{Style.BRIGHT}✅ {label} Complete!{' ' * 50}")

    @staticmethod
    def countdown_animation(seconds, label="Countdown"):
        """⏰ Ultra animated countdown"""
        for remaining in range(seconds, -1, -1):
            # Create animated progress
            progress = seconds - remaining
            total = seconds
            
            # Rainbow countdown number
            num_text = UltraColors.fire_text(f"[{remaining:02d}s]")
            
            # Animated bar
            bar_width = 30
            filled = int((progress / total) * bar_width) if total > 0 else 0
            empty = bar_width - filled
            
            bar = ""
            colors = UltraColors.RAINBOW
            for i in range(filled):
                bar += f"{colors[i % len(colors)]}{Style.BRIGHT}▰"
            bar += f"{Fore.WHITE}{'▱' * empty}"
            
            # Fire emoji animation
            fire_emojis = ['🔥', '💥', '✨', '⚡', '🌟']
            fire = fire_emojis[remaining % len(fire_emojis)]
            
            sys.stdout.write(
                f"\r{fire} {num_text} {bar} {UltraColors.rainbow_text(label)} {fire}"
            )
            sys.stdout.flush()
            sleep(1)
        
        print(f"\r{Fore.GREEN}{Style.BRIGHT}✅ Hoàn thành!{' ' * 60}")

    @staticmethod
    def matrix_rain(lines=8, width=80):
        """💚 Ultra Matrix rain effect"""
        chars = "01アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモ@#$%&*"
        
        for _ in range(lines):
            line = ""
            for _ in range(width):
                char = random.choice(chars)
                intensity = random.choice([Fore.GREEN, Fore.LIGHTGREEN_EX, Fore.WHITE])
                brightness = random.choice([Style.BRIGHT, Style.NORMAL])
                line += f"{intensity}{brightness}{char}"
            print(line)
            sleep(0.08)

    @staticmethod
    def firework_effect(width=60):
        """🎆 Firework explosion effect"""
        fireworks = ['✦', '✧', '★', '☆', '✪', '✫', '✬', '✭', '✮', '✯', '✰', '⋆', '✵', '✶', '✷', '✸', '✹', '✺']
        
        for _ in range(5):
            line = ""
            colors = UltraColors.NEON
            for _ in range(width):
                if random.random() < 0.3:
                    char = random.choice(fireworks)
                    color = random.choice(colors)
                    line += f"{color}{Style.BRIGHT}{char} "
                else:
                    line += "  "
            print(line)
            sleep(0.1)

    @staticmethod
    def pulse_text(text, cycles=5):
        """💓 Pulsing text effect"""
        for i in range(cycles):
            # Fade in/out effect with different colors
            if i % 2 == 0:
                colored = UltraColors.neon_text(text)
            else:
                colored = UltraColors.fire_text(text)
            
            sys.stdout.write(f"\r{colored}")
            sys.stdout.flush()
            sleep(0.2)
        print()

    @staticmethod
    def sparkle_border(width=70, char='═'):
        """✨ Sparkle border animation"""
        sparkles = ['✨', '💫', '⭐', '🌟', '✦', '✧', '★', '☆']
        colors = UltraColors.RAINBOW
        
        border = ""
        for i in range(width):
            if random.random() < 0.15:
                border += f"{random.choice(colors)}{Style.BRIGHT}{random.choice(sparkles)}"
            else:
                color = colors[i % len(colors)]
                border += f"{color}{Style.BRIGHT}{char}"
        
        return border + Style.RESET_ALL


class UltraBanners:
    """🎨 Ultra Premium Banner Collection"""

    MAIN_BANNER = r"""
                                                                                          
    ██████╗  ██████╗ ██╗     ██╗██╗  ██╗███████╗    ██╗   ██╗████████╗██████╗ 
   ██╔════╝ ██╔═══██╗██║     ██║██║ ██╔╝██╔════╝    ╚██╗ ██╔╝╚══██╔══╝██╔══██╗
   ██║  ███╗██║   ██║██║     ██║█████╔╝ █████╗       ╚████╔╝    ██║   ██████╔╝
   ██║   ██║██║   ██║██║     ██║██╔═██╗ ██╔══╝        ╚██╔╝     ██║   ██╔══██╗
   ╚██████╔╝╚██████╔╝███████╗██║██║  ██╗███████╗       ██║      ██║   ██████╔╝
    ╚═════╝  ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═╝╚══════╝       ╚═╝      ╚═╝   ╚═════╝ 
"""

    CYBER_BANNER = r"""
   ╔═══════════════════════════════════════════════════════════════════════╗
   ║  _____     _   _ _          _____         _   _____ _____ _____       ║
   ║ |   __|___| |_|_| |_ ___   |_   _|___ ___| | |  _  | __  |     |      ║
   ║ |  |  | . | | | | '_| -_|    | | | . | . | | |   __|    -|  |  |      ║
   ║ |_____|___|_|_|_|_,_|___|    |_| |___|___|_| |__|  |__|__|_____|      ║
   ║                                                                       ║
   ╚═══════════════════════════════════════════════════════════════════════╝
"""

    FIRE_BANNER = r"""
                    🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
                    
       ░██████╗░░█████╗░██╗░░░░░██╗██╗░░██╗███████╗
       ██╔════╝░██╔══██╗██║░░░░░██║██║░██╔╝██╔════╝
       ██║░░██╗░██║░░██║██║░░░░░██║█████═╝░█████╗░░
       ██║░░╚██╗██║░░██║██║░░░░░██║██╔═██╗░██╔══╝░░
       ╚██████╔╝╚█████╔╝███████╗██║██║░╚██╗███████╗
       ░╚═════╝░░╚════╝░╚══════╝╚═╝╚═╝░░╚═╝╚══════╝

                    💥💥💥 YOUTUBE TOOL PRO MAX 💥💥💥
                    🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
"""

    NEON_BANNER = r"""
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃  ╭─────────────────────────────────────────────────────────────────╮ ┃
    ┃  │  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  │ ┃
    ┃  │  █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█  │ ┃
    ┃  │  █  ██████╗  ██████╗ ██╗     ██╗██╗  ██╗███████╗          █  │ ┃
    ┃  │  █ ██╔════╝ ██╔═══██╗██║     ██║██║ ██╔╝██╔════╝          █  │ ┃
    ┃  │  █ ██║  ███╗██║   ██║██║     ██║█████╔╝ █████╗            █  │ ┃
    ┃  │  █ ██║   ██║██║   ██║██║     ██║██╔═██╗ ██╔══╝            █  │ ┃
    ┃  │  █ ╚██████╔╝╚██████╔╝███████╗██║██║  ██╗███████╗          █  │ ┃
    ┃  │  █  ╚═════╝  ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═╝╚══════╝          █  │ ┃
    ┃  │  █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█  │ ┃
    ┃  ╰─────────────────────────────────────────────────────────────────╯ ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""

    DRAGON_BANNER = r"""
                            🐉 ═══════════════════════════════ 🐉
                                                                
              ██████╗  ██████╗ ██╗     ██╗██╗  ██╗███████╗                
             ██╔════╝ ██╔═══██╗██║     ██║██║ ██╔╝██╔════╝                
             ██║  ███╗██║   ██║██║     ██║█████╔╝ █████╗                  
             ██║   ██║██║   ██║██║     ██║██╔═██╗ ██╔══╝                  
             ╚██████╔╝╚██████╔╝███████╗██║██║  ██╗███████╗                
              ╚═════╝  ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═╝╚══════╝                
                                                                          
               ██╗   ██╗████████╗██████╗     ████████╗ ██████╗  ██████╗ ██╗     
               ╚██╗ ██╔╝╚══██╔══╝██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
                ╚████╔╝    ██║   ██████╔╝       ██║   ██║   ██║██║   ██║██║     
                 ╚██╔╝     ██║   ██╔══██╗       ██║   ██║   ██║██║   ██║██║     
                  ██║      ██║   ██████╔╝       ██║   ╚██████╔╝╚██████╔╝███████╗
                  ╚═╝      ╚═╝   ╚═════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                                                
                            🐉 ═══════════════════════════════ 🐉
"""

    @staticmethod
    def get_random_banner():
        """🎲 Get random banner"""
        banners = [
            UltraBanners.MAIN_BANNER,
            UltraBanners.FIRE_BANNER,
            UltraBanners.DRAGON_BANNER,
        ]
        return random.choice(banners)


# ═══════════════════════════════════════════════════════════════════════════════
# 🖼️ ULTRA BEAUTIFUL BANNER DISPLAY
# ═══════════════════════════════════════════════════════════════════════════════

def show_ultra_banner():
    """🎨 Display ultra beautiful animated banner"""
    UltraAnimations.clear_screen()
    
    # Matrix rain intro
    print()
    UltraAnimations.matrix_rain(3, 70)
    
    # Sparkle top border
    print(UltraAnimations.sparkle_border(75, '═'))
    
    # Fire effect
    print(UltraColors.fire_text("    🔥 ═══════════════════════════════════════════════════════════════ 🔥"))
    
    # Main banner with rainbow effect
    banner = UltraBanners.MAIN_BANNER
    lines = banner.split('\n')
    
    for i, line in enumerate(lines):
        colored_line = UltraColors.rainbow_text(line)
        print(colored_line)
        sleep(0.05)
    
    # Firework effect
    UltraAnimations.firework_effect(70)
    
    # Rainbow separator with sparkles
    print()
    sparkle_sep = ""
    emojis = ['✨', '💫', '⭐', '🌟', '💎', '🔮', '🎯', '🚀']
    for i in range(70):
        if i % 10 == 0:
            sparkle_sep += f"{random.choice(emojis)}"
        else:
            color = UltraColors.RAINBOW[i % len(UltraColors.RAINBOW)]
            sparkle_sep += f"{color}{Style.BRIGHT}═"
    print(sparkle_sep + Style.RESET_ALL)
    print()
    
    # Tool info with typing effect
    info_lines = [
        "╔══════════════════════════════════════════════════════════════════╗",
        "║       ✨✨✨ GOLIKE YOUTUBE TOOL PRO MAX ULTRA ✨✨✨           ║",
        "║                                                                  ║",
        "║   🚀 Version: 6.0 ULTRA PREMIUM EDITION                         ║",
        "║   💎 Status: ACTIVATED & READY                                   ║",
        "║   🔥 Power Level: MAXIMUM                                        ║",
        "║                                                                  ║",
        "╠══════════════════════════════════════════════════════════════════╣",
        "║   👨‍💻 Developer: KhangDevxCoder                                    ║",
        "║   📱 Zalo: Đang tạo nhóm                                         ║",
        "║   🎵 TikTok: @khangprokiller                                      ║",
        "║   💬 Telegram: Coming soon...                                    ║",
        "╚══════════════════════════════════════════════════════════════════╝",
    ]
    
    for line in info_lines:
        colored = UltraColors.neon_text(line)
        print(f"    {colored}")
        sleep(0.03)
    
    print()
    
    # Animated welcome message
    welcome_msg = "🎉 ═══ WELCOME TO THE ULTIMATE EXPERIENCE ═══ 🎉"
    UltraAnimations.wave_animation(welcome_msg, 2, 0.05)
    
    # Bottom sparkle border
    print(UltraAnimations.sparkle_border(75, '═'))
    print()


# ═══════════════════════════════════════════════════════════════════════════════
# 🎯 ULTRA BEAUTIFUL UI COMPONENTS
# ═══════════════════════════════════════════════════════════════════════════════

class UltraUI:
    """✨ Ultra Beautiful User Interface Components"""

    @staticmethod
    def fancy_box(title, content_lines, style='double'):
        """📦 Create fancy box with content"""
        borders = UltraAnimations.BORDERS[style]
        tl, tr, bl, br, h, v = borders[:6]
        
        # Calculate width
        max_width = max(len(title) + 4, max(len(line) for line in content_lines) + 4)
        
        # Top border with title
        title_line = f"{tl}{h * 2} {UltraColors.rainbow_text(title)} {h * (max_width - len(title) - 5)}{tr}"
        print(UltraColors.neon_text(title_line))
        
        # Content
        for line in content_lines:
            padding = max_width - len(line) - 2
            content = f"{v} {line}{' ' * padding}{v}"
            print(UltraColors.neon_text(content))
        
        # Bottom border
        bottom = f"{bl}{h * max_width}{br}"
        print(UltraColors.neon_text(bottom))

    @staticmethod
    def success_box(message):
        """✅ Ultra success message box"""
        border_chars = ['✦', '✧', '★', '☆', '✪', '✫']
        
        print()
        border = ''.join([f"{Fore.GREEN}{Style.BRIGHT}{random.choice(border_chars)}" for _ in range(len(message) + 8)])
        print(border)
        print(f"{Fore.GREEN}{Style.BRIGHT}┃ ✅ {message} ┃")
        print(border)
        print()

    @staticmethod
    def error_box(message):
        """❌ Ultra error message box"""
        print()
        print(f"{Fore.RED}{Style.BRIGHT}╔{'═' * (len(message) + 6)}╗")
        print(f"{Fore.RED}{Style.BRIGHT}║ ❌ {message} ║")
        print(f"{Fore.RED}{Style.BRIGHT}╚{'═' * (len(message) + 6)}╝")
        print()

    @staticmethod
    def warning_box(message):
        """⚠️ Ultra warning message box"""
        print()
        print(f"{Fore.YELLOW}{Style.BRIGHT}╔{'═' * (len(message) + 6)}╗")
        print(f"{Fore.YELLOW}{Style.BRIGHT}║ ⚠️  {message} ║")
        print(f"{Fore.YELLOW}{Style.BRIGHT}╚{'═' * (len(message) + 6)}╝")
        print()

    @staticmethod
    def info_box(message):
        """ℹ️ Ultra info message box"""
        print()
        border = UltraColors.rainbow_text('═' * (len(message) + 8))
        print(f"╔{border}╗")
        print(f"║ {Fore.CYAN}{Style.BRIGHT}ℹ️  {message} {Fore.WHITE}║")
        print(f"╚{border}╝")
        print()

    @staticmethod
    def menu_header(title):
        """📋 Ultra menu header"""
        print()
        print(UltraAnimations.sparkle_border(60, '═'))
        centered_title = title.center(56)
        print(f"║{UltraColors.rainbow_text(centered_title)}║")
        print(UltraAnimations.sparkle_border(60, '═'))
        print()

    @staticmethod
    def menu_item(number, description, icon="🎯", active=False):
        """📋 Ultra beautiful menu item"""
        colors = UltraColors.RAINBOW
        
        # Rainbow number
        num_text = UltraColors.fire_text(f"[{number}]")
        
        # Gradient description
        if active:
            desc_text = UltraColors.neon_text(description)
            prefix = "▶▶"
        else:
            desc_text = UltraColors.rainbow_text(description)
            prefix = "  "
        
        # Animated icon
        icons = ['✨', '💫', '⭐', '🌟']
        animated_icon = icon if icon not in icons else random.choice(icons)
        
        print(f"  {prefix} {num_text} {animated_icon} {desc_text}")
        sleep(0.02)

    @staticmethod
    def input_field(label, icon="✏️ ", color=Fore.CYAN):
        """📝 Ultra beautiful input field"""
        rainbow_label = UltraColors.rainbow_text(label)
        prompt = f"\n{Fore.CYAN}{Style.BRIGHT}╭─── {icon} {rainbow_label}\n╰─▶ "
        user_input = input(prompt)
        return user_input.strip()

    @staticmethod
    def account_card(index, username, status, balance=0):
        """💳 Ultra beautiful account card"""
        colors = [Fore.CYAN, Fore.MAGENTA, Fore.YELLOW, Fore.GREEN, Fore.LIGHTCYAN_EX]
        color = colors[index % len(colors)]
        
        # Card border with animation
        sparkles = ['✨', '💎', '⭐', '🌟', '💫']
        sparkle = random.choice(sparkles)
        
        card = f"""
{color}{Style.BRIGHT}    {sparkle}╔══════════════════════════════════════════════════╗{sparkle}
    ║  {UltraColors.fire_text(f'🔖 ACCOUNT #{index}')}                               ║
    ╠══════════════════════════════════════════════════╣
    ║  {Fore.CYAN}{Style.BRIGHT}👤 Username: {Fore.WHITE}{Style.BRIGHT}{username.ljust(30)}{color}║
    ║  {Fore.GREEN}{Style.BRIGHT}✅ Status:   {Fore.LIGHTGREEN_EX}{Style.BRIGHT}{status.ljust(30)}{color}║
    ║  {Fore.YELLOW}{Style.BRIGHT}💰 Balance:  {Fore.LIGHTYELLOW_EX}{Style.BRIGHT}{str(balance).ljust(28)} đ{color}║
    {sparkle}╚══════════════════════════════════════════════════╝{sparkle}
"""
        print(card)

    @staticmethod
    def result_row(job_num, time_str, status, action, reward, total):
        """📊 Ultra beautiful result row"""
        status_icons = {
            "success": ("✅", Fore.GREEN),
            "failed": ("❌", Fore.RED),
            "pending": ("⏳", Fore.YELLOW),
        }
        
        icon, status_color = status_icons.get(status.lower(), ("❓", Fore.WHITE))
        
        # Rainbow job number
        job_text = UltraColors.fire_text(f"[JOB #{job_num:03d}]")
        
        # Time with glow effect
        time_text = f"{Fore.LIGHTCYAN_EX}{Style.BRIGHT}⏰ {time_str}"
        
        # Status with icon
        status_text = f"{status_color}{Style.BRIGHT}{icon} {status.upper()}"
        
        # Action with neon
        action_text = UltraColors.neon_text(f"🎬 {action}")
        
        # Reward with fire
        reward_text = f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}💰 +{reward} đ"
        
        # Total with rainbow
        total_text = UltraColors.rainbow_text(f"📊 Total: {total} đ")
        
        print(f"""
╭──────────────────────────────────────────────────────────────────╮
│ {job_text} │ {time_text} │ {status_text} │
├──────────────────────────────────────────────────────────────────┤
│ {action_text} │ {reward_text} │ {total_text} │
╰──────────────────────────────────────────────────────────────────╯
""")

    @staticmethod
    def stats_dashboard(completed, failed, total_earned, elapsed_time):
        """📈 Ultra stats dashboard"""
        dashboard = f"""
{UltraColors.rainbow_text('╔══════════════════════════════════════════════════════════════════╗')}
{UltraColors.neon_text('║                    📊 REAL-TIME STATISTICS 📊                    ║')}
{UltraColors.rainbow_text('╠══════════════════════════════════════════════════════════════════╣')}
║  {Fore.GREEN}{Style.BRIGHT}✅ Completed Jobs:    {str(completed).ljust(20)}{Fore.WHITE}                   ║
║  {Fore.RED}{Style.BRIGHT}❌ Failed Jobs:       {str(failed).ljust(20)}{Fore.WHITE}                   ║
║  {Fore.YELLOW}{Style.BRIGHT}💰 Total Earned:      {str(total_earned).ljust(18)} đ{Fore.WHITE}                 ║
║  {Fore.CYAN}{Style.BRIGHT}⏱️  Elapsed Time:      {elapsed_time.ljust(20)}{Fore.WHITE}                   ║
{UltraColors.rainbow_text('╚══════════════════════════════════════════════════════════════════╝')}
"""
        print(dashboard)


# ═══════════════════════════════════════════════════════════════════════════════
# 🔧 GOLIKE TOOL CORE FUNCTIONALITY
# ═══════════════════════════════════════════════════════════════════════════════

class GolikeToolUltra:
    """🎯 Golike YouTube Tool Pro Max Ultra Edition"""

    def __init__(self):
        self.session = requests.Session()
        self.headers = {}
        self.accounts = []
        self.total_earned = 0
        self.completed_jobs = 0
        self.failed_jobs = 0
        self.user_data = {}
        self.start_time = None

        # User agents pool
        self.user_agents = self._get_user_agents()

    def _get_user_agents(self):
        """📱 Get list of user agents"""
        return [
            "android|Mozilla/5.0 (Linux; U; Android 7.1; GT-I9100 Build/KTU84P) AppleWebKit/603.12 (KHTML, like Gecko) Chrome/50.0.3755.367 Mobile Safari/600.8",
            "android|Mozilla/5.0 (Linux; Android 5.0; SM-N910V Build/LRX22C) AppleWebKit/601.33 (KHTML, like Gecko) Chrome/54.0.1548.302 Mobile Safari/537.0",
            "android|Mozilla/5.0 (Linux; U; Android 7.1; Pixel C Build/NRD90M) AppleWebKit/600.2 (KHTML, like Gecko) Chrome/53.0.2480.357 Mobile Safari/600.7",
            "android|Mozilla/5.0 (Linux; U; Android 7.0; Nexus 7 Build/NME91E) AppleWebKit/537.24 (KHTML, like Gecko) Chrome/55.0.1165.180 Mobile Safari/535.4",
            "android|Mozilla/5.0 (Android; Android 4.4.4; IQ4502 Quad Build/KOT49H) AppleWebKit/603.22 (KHTML, like Gecko) Chrome/55.0.3246.371 Mobile Safari/535.0",
            "android|Mozilla/5.0 (Linux; U; Android 5.0.1; SAMSUNG SM-G925FQ Build/KOT49H) AppleWebKit/536.8 (KHTML, like Gecko) Chrome/49.0.2349.273 Mobile Safari/533.8",
            "android|Mozilla/5.0 (Android; Android 5.1.1; SM-G935S Build/LMY47X) AppleWebKit/601.8 (KHTML, like Gecko) Chrome/51.0.1541.177 Mobile Safari/603.6",
            "android|Mozilla/5.0 (Android; Android 7.1; Nexus 6 Build/NME91E) AppleWebKit/533.39 (KHTML, like Gecko) Chrome/52.0.3581.331 Mobile Safari/602.0",
            "android|Mozilla/5.0 (Android; Android 7.1; Pixel C Build/NME91E) AppleWebKit/536.42 (KHTML, like Gecko) Chrome/47.0.2862.396 Mobile Safari/534.0",
            "android|Mozilla/5.0 (Linux; U; Android 5.0.1; LG-D725 Build/LRX22G) AppleWebKit/603.18 (KHTML, like Gecko) Chrome/54.0.3919.385 Mobile Safari/601.9",
        ]

    def get_authorization(self):
        """🔑 Get Golike authorization"""
        auth_file = 'user.txt'

        if os.path.exists(auth_file):
            with open(auth_file, 'r') as f:
                auth = f.read().strip()
            if auth:
                return auth

        UltraUI.info_box("🔐 Please enter your Golike Authorization token")
        auth = UltraUI.input_field("Authorization Token", "🔑 ", Fore.CYAN)

        with open(auth_file, 'w') as f:
            f.write(auth)

        return auth

    def setup_headers(self, auth):
        """⚙️ Setup request headers"""
        user_agent = random.choice(self.user_agents)
        self.headers = {
            'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
            'Referer': 'https://app.golike.net/',
            'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': "Windows",
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'T': 'VFZSamQwOUVSVEpQVkVFd1RrRTlQUT09',
            'User-Agent': user_agent,
            'Authorization': auth,
            'Content-Type': 'application/json;charset=utf-8'
        }

    def verify_user(self):
        """✅ Verify user login"""
        UltraAnimations.loading_spinner("🔐 Authenticating", 2, 'star')

        url = 'https://gateway.golike.net/api/users/me'

        try:
            response = self.session.get(url, headers=self.headers)
            data = response.json()

            if data.get('status') == 200:
                self.user_data = data.get('data', {})
                UltraUI.success_box("LOGIN SUCCESSFUL!")
                return True
            else:
                UltraUI.error_box("LOGIN FAILED!")
                return False
        except Exception as e:
            UltraUI.error_box(f"Connection Error: {str(e)}")
            return False

    def show_user_info(self):
        """👤 Display user information"""
        if not self.user_data:
            return

        username = self.user_data.get('username', 'Unknown')
        coin = self.user_data.get('coin', 0)
        user_id = self.user_data.get('id', 'Unknown')

        print()
        UltraUI.menu_header("👤 USER INFORMATION")
        UltraUI.account_card(1, username, "🟢 Active", coin)
        
        # Additional info with animation
        info_text = f"🆔 User ID: {user_id}"
        UltraAnimations.typing_effect(info_text, 0.02)
        print()

    def get_youtube_accounts(self):
        """📺 Get YouTube accounts"""
        UltraAnimations.progress_bar("🔄 Loading YouTube accounts", 1.5)

        url = 'https://gateway.golike.net/api/youtube-account'

        try:
            response = self.session.get(url, headers=self.headers)
            data = response.json()

            if data.get('status') == 200:
                self.accounts = data.get('data', [])
                return True
            else:
                UltraUI.error_box("Failed to load YouTube accounts")
                return False
        except Exception as e:
            UltraUI.error_box(f"Error: {str(e)}")
            return False

    def show_accounts_menu(self):
        """📋 Display accounts menu"""
        if not self.accounts:
            UltraUI.warning_box("No YouTube accounts found!")
            return None

        UltraUI.menu_header("📺 YOUTUBE ACCOUNTS")

        for i, account in enumerate(self.accounts, 1):
            username = account.get('name', 'Unknown')
            UltraUI.account_card(i, username, "🟢 Active")

        print()
        choice = UltraUI.input_field("📝 Enter account number", "🎯 ", Fore.CYAN)

        try:
            choice_num = int(choice)
            if 1 <= choice_num <= len(self.accounts):
                return self.accounts[choice_num - 1]
            else:
                UltraUI.error_box("Invalid account number!")
                return None
        except ValueError:
            UltraUI.error_box("Please enter a valid number!")
            return None

    def run_youtube_bot(self, account):
        """🤖 Run YouTube automation bot"""
        UltraAnimations.clear_screen()
        show_ultra_banner()

        account_id = account.get('id')
        account_name = account.get('name')

        # Load saved auth and cookie
        auth = self.load_credential(f'AUTHYTB{account_id}')
        cookie = self.load_credential(f'COOKIEYTB{account_id}')

        if not auth:
            UltraUI.info_box("🔐 Enter YouTube Authorization")
            auth = UltraUI.input_field("YouTube Auth Token", "🔑 ", Fore.CYAN)
            self.save_credential(f'AUTHYTB{account_id}', auth)

        if not cookie:
            UltraUI.info_box("🍪 Enter YouTube Cookie")
            cookie = UltraUI.input_field("YouTube Cookie", "🍪 ", Fore.CYAN)
            self.save_credential(f'COOKIEYTB{account_id}', cookie)

        # Get job settings
        UltraAnimations.clear_screen()
        show_ultra_banner()

        UltraUI.menu_header("⚙️ BOT SETTINGS")

        try:
            num_jobs = int(UltraUI.input_field("🔢 Number of jobs", "📊 ", Fore.CYAN))
            delay = int(UltraUI.input_field("⏱️  Delay between jobs (seconds)", "⏰ ", Fore.CYAN))
        except ValueError:
            UltraUI.error_box("Invalid input! Using default values.")
            num_jobs = 10
            delay = 5

        # Start bot
        self.start_bot(account_id, num_jobs, delay, auth, cookie)

    def load_credential(self, filename):
        """📂 Load saved credential"""
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                return f.read().strip()
        return None

    def save_credential(self, filename, data):
        """💾 Save credential to file"""
        with open(filename, 'w') as f:
            f.write(data)

    def start_bot(self, account_id, num_jobs, delay, auth, cookie):
        """🚀 Start the bot"""
        print()
        UltraUI.success_box("🚀 BOT STARTED!")
        print()
        
        self.start_time = datetime.now()
        self.completed_jobs = 0
        self.failed_jobs = 0
        self.total_earned = 0

        for i in range(num_jobs):
            # Progress indicator with rainbow
            progress_text = f"📊 Progress: [{i + 1}/{num_jobs}] {'█' * (i + 1)}{'░' * (num_jobs - i - 1)}"
            print(UltraColors.rainbow_text(progress_text))
            print()

            try:
                # Get job with animation
                UltraAnimations.loading_spinner("🔍 Searching for jobs", 1, 'star')
                job = self.get_job(account_id)

                if not job:
                    print(f"{Fore.YELLOW}{Style.BRIGHT}⚠️ No jobs available, waiting...")
                    UltraAnimations.countdown_animation(15, "⏳ Waiting for new jobs")
                    continue

                # Process job
                UltraAnimations.loading_spinner("⚙️ Processing job", 1.5, 'fire')
                result = self.process_job(job, auth, cookie, account_id)

                if result:
                    self.completed_jobs += 1
                    self.total_earned += result.get('reward', 0)
                    self.display_result(i + 1, result)
                else:
                    self.failed_jobs += 1

                # Show live stats
                elapsed = datetime.now() - self.start_time
                elapsed_str = str(elapsed).split('.')[0]
                UltraUI.stats_dashboard(
                    self.completed_jobs,
                    self.failed_jobs,
                    self.total_earned,
                    elapsed_str
                )

                # Countdown delay with animation
                UltraAnimations.countdown_animation(delay, "⏳ Next job in")

            except Exception as e:
                self.failed_jobs += 1
                UltraUI.error_box(f"Error: {str(e)}")

        # Summary
        self.show_summary()

    def get_job(self, account_id):
        """📋 Get available job"""
        url = f'https://gateway.golike.net/api/advertising/publishers/youtube/jobs?account_id={account_id}'

        try:
            response = self.session.get(url, headers=self.headers)
            data = response.json()

            if data.get('status') == 200:
                return data.get('data')
            else:
                return None
        except:
            return None

    def process_job(self, job, auth, cookie, account_id):
        """⚙️ Process single job"""
        job_type = job.get('type')
        object_id = job.get('object_id')
        ads_id = job.get('id')

        if job_type == 'subscribe':
            return self.process_subscribe(object_id, ads_id, auth, cookie, account_id)

        return None

    def process_subscribe(self, channel_id, ads_id, auth, cookie, account_id):
        """🔔 Process subscribe job"""
        headers = {
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8',
            'authorization': auth,
            'content-type': 'application/json',
            'cookie': cookie,
            'origin': 'https://www.youtube.com',
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
        }

        try:
            response = requests.post(
                'https://www.youtube.com/youtubei/v1/subscription/subscribe',
                headers=headers,
                json={
                    'context': {
                        'client': {
                            'hl': 'en',
                            'gl': 'VN',
                            'clientName': 'MWEB',
                            'clientVersion': '2.20240722.07.00',
                        }
                    },
                    'channelIds': [channel_id],
                    'params': 'EgIIAhgA',
                }
            ).json()

            # Complete job
            complete_url = 'https://gateway.golike.net/api/advertising/publishers/youtube/complete-jobs'
            complete_data = {
                'account_id': account_id,
                'ads_id': ads_id,
            }

            sleep(3)

            response = self.session.post(
                complete_url,
                headers=self.headers,
                json=complete_data
            ).json()

            if response.get('success'):
                return {
                    'status': 'success',
                    'reward': response.get('data', {}).get('prices', 0),
                    'action': 'Subscribe'
                }

        except:
            pass

        return None

    def display_result(self, job_num, result):
        """📊 Display job result"""
        local_time = time.localtime()
        time_str = f"{local_time.tm_hour:02d}:{local_time.tm_min:02d}:{local_time.tm_sec:02d}"

        UltraUI.result_row(
            job_num,
            time_str,
            result['status'],
            result['action'],
            result['reward'],
            self.total_earned
        )

    def show_summary(self):
        """📈 Show bot summary"""
        print()
        UltraUI.menu_header("📈 BOT SUMMARY")
        
        elapsed = datetime.now() - self.start_time if self.start_time else "N/A"
        elapsed_str = str(elapsed).split('.')[0] if self.start_time else "N/A"
        
        summary = f"""
{UltraColors.rainbow_text('╔══════════════════════════════════════════════════════════════════╗')}
{UltraColors.neon_text('║                    🏆 FINAL STATISTICS 🏆                         ║')}
{UltraColors.rainbow_text('╠══════════════════════════════════════════════════════════════════╣')}
║  {Fore.GREEN}{Style.BRIGHT}✅ Completed Jobs:    {str(self.completed_jobs).ljust(20)}{Fore.WHITE}                   ║
║  {Fore.RED}{Style.BRIGHT}❌ Failed Jobs:       {str(self.failed_jobs).ljust(20)}{Fore.WHITE}                   ║
║  {Fore.YELLOW}{Style.BRIGHT}💰 Total Earned:      {str(self.total_earned).ljust(18)} đ{Fore.WHITE}                 ║
║  {Fore.CYAN}{Style.BRIGHT}⏱️  Total Time:        {str(elapsed_str).ljust(20)}{Fore.WHITE}                   ║
║  {Fore.MAGENTA}{Style.BRIGHT}📊 Success Rate:      {str(round(self.completed_jobs/(self.completed_jobs+self.failed_jobs)*100 if (self.completed_jobs+self.failed_jobs) > 0 else 0, 1)).ljust(18)}%{Fore.WHITE}                 ║
{UltraColors.rainbow_text('╚══════════════════════════════════════════════════════════════════╝')}
"""
        print(summary)
        
        # Firework celebration
        UltraAnimations.firework_effect(60)
        UltraUI.success_box("🎉 BOT COMPLETED SUCCESSFULLY!")
        print()

    def show_main_menu(self):
        """📋 Display main menu"""
        UltraUI.menu_header("🎮 MAIN MENU")

        UltraUI.menu_item(1, "🎬 YouTube Tool - Start Earning!", "📺")
        UltraUI.menu_item(2, "🗑️  Clear Authorization", "🧹")
        UltraUI.menu_item(3, "📊 View Statistics", "📈")
        UltraUI.menu_item(0, "🚪 Exit Program", "👋")

        print()
        print(UltraAnimations.sparkle_border(60, '═'))
        print()

        choice = UltraUI.input_field("👉 Enter your choice", "✨ ", Fore.CYAN)

        return choice

    def clear_authorization(self):
        """🗑️ Clear saved authorization"""
        if os.path.exists('user.txt'):
            os.remove('user.txt')
            UltraUI.success_box("Authorization cleared successfully!")
        else:
            UltraUI.warning_box("No authorization file found!")


# ═══════════════════════════════════════════════════════════════════════════════
# 🎮 MAIN APPLICATION
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    """🎯 Main application entry point"""
    tool = GolikeToolUltra()

    while True:
        show_ultra_banner()

        # Get authorization
        auth = tool.get_authorization()
        tool.setup_headers(auth)

        # Verify user
        if not tool.verify_user():
            if os.path.exists('user.txt'):
                os.remove('user.txt')
            continue

        # Show user info
        tool.show_user_info()

        # Show menu
        choice = tool.show_main_menu()

        if choice == "1":
            # Get YouTube accounts
            if not tool.get_youtube_accounts():
                continue

            # Show accounts and get selected
            selected_account = tool.show_accounts_menu()

            if selected_account:
                tool.run_youtube_bot(selected_account)

        elif choice == "2":
            tool.clear_authorization()

        elif choice == "3":
            UltraUI.info_box("📊 Statistics feature coming soon!")

        elif choice == "0":
            print()
            UltraAnimations.matrix_rain(5, 60)
            UltraUI.success_box("👋 Thank you for using Golike Tool! Goodbye!")
            UltraAnimations.typing_effect("💖 See you next time! 💖", 0.05)
            break

        else:
            UltraUI.error_box("Invalid choice! Please try again.")

        # Pause before continuing
        print()
        input(f"{Fore.CYAN}{Style.BRIGHT}⏸️  Press Enter to continue...")


# ═══════════════════════════════════════════════════════════════════════════════
# 🚀 ENTRY POINT
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}{Style.BRIGHT}⚠️  Program interrupted by user. Goodbye! 👋\n")
        UltraAnimations.matrix_rain(3, 50)
    except Exception as e:
        print(f"\n\n{Fore.RED}{Style.BRIGHT}❌ An error occurred: {str(e)}\n")