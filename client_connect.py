import time
import requests
from pynput import keyboard
from pynput.keyboard import Key
import threading

keyToString = {
	Key.alt: "alt",
	Key.alt_l: "alt_l",
	Key.alt_r: "alt_r",
	Key.alt_gr: "alt_gr",
	Key.backspace: "backspace",
	Key.caps_lock: "caps_lock",
	Key.cmd: "cmd",
	Key.cmd_l: "cmd_l",
	Key.cmd_r: "cmd_r",
	Key.ctrl: "ctrl",
	Key.ctrl_l: "ctrl_l",
	Key.ctrl_r: "ctrl_r",
	Key.delete: "delete",
	Key.down: "down",
	Key.end: "end",
	Key.enter: "enter",
	Key.esc: "esc",
	Key.f1: "f1",
	Key.f2: "f2",
	Key.f3: "f3",
	Key.f4: "f4",
	Key.f5: "f5",
	Key.f6: "f6",
	Key.f7: "f7",
	Key.f8: "f8",
	Key.f9: "f9",
	Key.f10: "f10",
	Key.f11: "f11",
	Key.f12: "f12",
	Key.f13: "f13",
	Key.f14: "f14",
	Key.f15: "f15",
	Key.f16: "f16",
	Key.f17: "f17",
	Key.f18: "f18",
	Key.f19: "f19",
	Key.f20: "f20",
	Key.home: "home",
	Key.left: "left",
	Key.page_down: "page_down",
	Key.page_up: "page_up",
	Key.right: "right",
	Key.shift: "shift",
	Key.shift_l: "shift_l",
	Key.shift_r: "shift_r",
	Key.space: "space",
	Key.tab: "tab",
	Key.up: "up",
	Key.media_play_pause: "media_play_pause",
	Key.media_volume_mute: "media_volume_mute",
	Key.media_volume_down: "media_volume_down",
	Key.media_volume_up: "media_volume_up",
	Key.media_previous: "media_previous",
	Key.media_next: "media_next",
	Key.insert: "insert",
	Key.menu: "menu",
	Key.num_lock: "num_lock",
	Key.pause: "pause",
	Key.print_screen: "print_screen",
	Key.scroll_lock: "scroll_lock"
}


global hostAddress
hostAddress = "127.0.0.1:99"

def sendKey(key, if_pressed):
    global hostAddress
    pressed_key = None
    try:
        pressed_key = key.char
    except AttributeError:
        pressed_key = keyToString[key]

    if pressed_key == None:
        return

    ifPressChar = "+" if if_pressed else "-"

    # response = requests.get("http://api.open-notify.org/astros.json")
    sendLink = f"http://{hostAddress}/sendInput?{pressed_key}_t{ifPressChar}"
    sendThread = threading.Thread(target=requests.get, args=(sendLink,))
    sendThread.start()


def on_press(key):
    sendKey(key, True)

def on_release(key):
    sendKey(key, False)


def start(ahostAddress):
    global hostAddress
    hostAddress = ahostAddress
    print("started")
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    while True:
        time.sleep(5)