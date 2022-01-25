import pprint
import json
from pynput.keyboard import Key, Controller

keyboard = Controller()

pp = pprint.PrettyPrinter(indent=4)


# pylint: disable=C0326; it is easier to read column aligned keys
#: The keys used as modifiers; the first value in each tuple is the
#: base modifier to use for subsequent modifiers.
_MODIFIER_KEYS = (
    (Key.alt_gr, (Key.alt_gr.value,)),
    (Key.alt,    (Key.alt.value,   Key.alt_l.value,   Key.alt_r.value)),
    (Key.cmd,    (Key.cmd.value,   Key.cmd_l.value,   Key.cmd_r.value)),
    (Key.ctrl,   (Key.ctrl.value,  Key.ctrl_l.value,  Key.ctrl_r.value)),
    (Key.shift,  (Key.shift.value, Key.shift_l.value, Key.shift_r.value)))

#: Normalised modifiers as a mapping from virtual key code to basic modifier.
# _NORMAL_MODIFIERS = {
#     value: key
#     for combination in _MODIFIER_KEYS
#     for key, value in zip(
#         itertools.cycle((combination[0],)),
#         combination[1])}

#: Control codes to transform into key codes when typing
_CONTROL_CODES = {
    '\n': Key.enter,
    '\r': Key.enter,
    '\t': Key.tab}
# pylint: enable=C0326

stringToKey = {
	"alt": Key.alt,
	"alt_l": Key.alt_l,
	"alt_r": Key.alt_r,
	"alt_gr": Key.alt_gr,
	"backspace": Key.backspace,
	"caps_lock": Key.caps_lock,
	"cmd": Key.cmd,
	"cmd_l": Key.cmd_l,
	"cmd_r": Key.cmd_r,
	"ctrl": Key.ctrl,
	"ctrl_l": Key.ctrl_l,
	"ctrl_r": Key.ctrl_r,
	"delete": Key.delete,
	"down": Key.down,
	"end": Key.end,
	"enter": Key.enter,
	"esc": Key.esc,
	"f1": Key.f1,
	"f2": Key.f2,
	"f3": Key.f3,
	"f4": Key.f4,
	"f5": Key.f5,
	"f6": Key.f6,
	"f7": Key.f7,
	"f8": Key.f8,
	"f9": Key.f9,
	"f10": Key.f10,
	"f11": Key.f11,
	"f12": Key.f12,
	"f13": Key.f13,
	"f14": Key.f14,
	"f15": Key.f15,
	"f16": Key.f16,
	"f17": Key.f17,
	"f18": Key.f18,
	"f19": Key.f19,
	"f20": Key.f20,
	"home": Key.home,
	"left": Key.left,
	"page_down": Key.page_down,
	"page_up": Key.page_up,
	"right": Key.right,
	"shift": Key.shift,
	"shift_l": Key.shift_l,
	"shift_r": Key.shift_r,
	"space": Key.space,
	"tab": Key.tab,
	"up": Key.up,
	"media_play_pause": Key.media_play_pause,
	"media_volume_mute": Key.media_volume_mute,
	"media_volume_down": Key.media_volume_down,
	"media_volume_up": Key.media_volume_up,
	"media_previous": Key.media_previous,
	"media_next": Key.media_next,
	"insert": Key.insert,
	"menu": Key.menu,
	"num_lock": Key.num_lock,
	"pause": Key.pause,
	"print_screen": Key.print_screen,
	"scroll_lock": Key.scroll_lock
}

def execute_input(get_param, headers, body):
    if(get_param == None):
        return "Error: must have a input to be sent"
    print("recieved input: "+get_param)
    get_param_arr = get_param.split("_t")
    if len(get_param_arr) < 2:
        return "must have input seperated by _t"
    key = get_param_arr[0]
    if key in stringToKey.keys():
        key = stringToKey[key]
    is_press = True if get_param_arr[1] == "+" else False

    if is_press:
        keyboard.press(key)
    else:
        keyboard.release(key)
    return "sent: "+get_param