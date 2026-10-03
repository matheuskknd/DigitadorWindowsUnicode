# -*- coding: UTF-8 -*-

import ctypes
import time
import pyautogui
from ctypes import wintypes

user32 = ctypes.WinDLL("user32", use_last_error=True)

INPUT_KEYBOARD = 1
KEYEVENTF_UNICODE = 0x0004
KEYEVENTF_KEYUP = 0x0002

ULONG_PTR = ctypes.c_size_t


class KEYBDINPUT(ctypes.Structure):
    _fields_ = [
        ("wVk", wintypes.WORD),
        ("wScan", wintypes.WORD),
        ("dwFlags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", ULONG_PTR),
    ]


class MOUSEINPUT(ctypes.Structure):
    _fields_ = [
        ("dx", wintypes.LONG),
        ("dy", wintypes.LONG),
        ("mouseData", wintypes.DWORD),
        ("dwFlags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", ULONG_PTR),
    ]


class HARDWAREINPUT(ctypes.Structure):
    _fields_ = [
        ("uMsg", wintypes.DWORD),
        ("wParamL", wintypes.WORD),
        ("wParamH", wintypes.WORD),
    ]


class INPUT_UNION(ctypes.Union):
    _fields_ = [
        ("ki", KEYBDINPUT),
        ("mi", MOUSEINPUT),
        ("hi", HARDWAREINPUT),
    ]


class INPUT(ctypes.Structure):
    _anonymous_ = ("u",)
    _fields_ = [
        ("type", wintypes.DWORD),
        ("u", INPUT_UNION),
    ]


def send_unicode_char(char):
    code = ord(char)

    # KEY DOWN
    inp = INPUT(
        type=INPUT_KEYBOARD,
        ki=KEYBDINPUT(
            wVk=0,
            wScan=code,
            dwFlags=KEYEVENTF_UNICODE,
            time=0,
            dwExtraInfo=0,
        ),
    )

    result = user32.SendInput(
        1,
        ctypes.byref(inp),
        ctypes.sizeof(INPUT),
    )

    if result != 1:
        raise ctypes.WinError(ctypes.get_last_error())

    # KEY UP
    inp.ki.dwFlags = KEYEVENTF_UNICODE | KEYEVENTF_KEYUP

    result = user32.SendInput(
        1,
        ctypes.byref(inp),
        ctypes.sizeof(INPUT),
    )

    if result != 1:
        raise ctypes.WinError(ctypes.get_last_error())


def digitar(texto, intervalo=0.01):
    for char in texto:
        if char == "\n":
            pyautogui.press("enter")
        elif char != "\r":
            send_unicode_char(char)

        time.sleep(intervalo)


texto = """Teste de digitação:

terapêutico
ação
atenção
informação
coração
João
ã õ ç á é í ó ú â ê ô

Português: terapêutico, ação, coração, maçã
Espanhol: niño, corazón
Alemão: über, größer
Grego: Καλημέρα
Cirílico: Привет
Japonês: こんにちは
Chinês: 你好
Emojis: 😀🚀👍
"""

print("Clique no campo onde deseja digitar.")
print("Começando em 5 segundos...")
time.sleep(5)

digitar(texto, intervalo=0.02)

print("Concluído.")
