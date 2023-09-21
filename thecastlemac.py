from __future__ import print_function
import os
import PIL.Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from guizero import *
import random
import pyautogui
from pynput.mouse import Listener
def disable1():
	pic_button1.disable()
def disable2():
	pic_button2.disable()
def disable3():
	pic_button3.disable()
def disable4():
	pic_button4.disable()
def start_paint(event):
	painting.last_event = event
	painting2.last_event = event
	painting3.last_event = event
	painting4.last_event = event
	painting5.last_event = event
def stop_paint():
	painting.last_event = None
	painting.last_shape = None
	painting2.last_event = None
	painting2.last_shape = None
	painting3.last_event = None
	painting3.last_shape = None
	painting4.last_event = None
	painting4.last_shape = None
	painting5.last_event = None
	painting5.last_shape = None
def draw_paint(event):
	painting.line(painting.last_event.x, painting.last_event.y, event.x, event.y, color="red", width=6)
	painting.last_event = event
	painting2.line(painting2.last_event.x, painting2.last_event.y, event.x, event.y, color="black", width=3)
	painting2.last_event = event
	painting3.line(painting3.last_event.x, painting3.last_event.y, event.x, event.y, color="#bec9c7", width=3)
	painting3.last_event = event
	painting4.line(painting4.last_event.x, painting4.last_event.y, event.x, event.y, color="#a3d2d8", width=2)
	painting4.last_event = event	
	painting5.line(painting5.last_event.x, painting5.last_event.y, event.x, event.y, color="#ff05e8", width=1)
	painting5.last_event = event
def start_sketch1(event):
	sketching1.last_event = event
def stop_sketch1():
	sketching1.last_event = None
	sketching1.last_shape = None
def draw_sketch1(event):
	sketching1.line(sketching1.last_event.x, sketching1.last_event.y, event.x, event.y, color="#2200ff", width=1)
	sketching1.last_event = event
def start_sketch2(event):
	sketching2.last_event = event
def stop_sketch2():
	sketching2.last_event = None
	sketching2.last_shape = None
def draw_sketch2(event):
	sketching2.line(sketching2.last_event.x, sketching2.last_event.y, event.x, event.y, color="#2200ff", width=6)
	sketching2.last_event = event
def start_sketch3(event):
	sketching3.last_event = event
def stop_sketch3():
	sketching3.last_event = None
	sketching3.last_shape = None
def draw_sketch3(event):
	sketching4.line(sketching3.last_event.x, sketching3.last_event.y, event.x, event.y, color="white", width=1)
	sketching4.last_event = event
def start_sketch4(event):
	sketching4.last_event = event
def stop_sketch4():
	sketching4.last_event = None
	sketching4.last_shape = None
def draw_sketch4(event):
	sketching4.line(sketching4.last_event.x, sketching4.last_event.y, event.x, event.y, color="red", width=3)
	sketching4.last_event = event
def start_sketch5(event):
	sketching5.last_event = event
def stop_sketch5():
	sketching5.last_event = None
	sketching5.last_shape = None
def draw_sketch5(event):
	sketching5.line(sketching5.last_event.x, sketching5.last_event.y, event.x, event.y, color="#c6c5c9", width=5)
	sketching5.last_event = event
def start_sketch6(event):
	sketching6.last_event = event
def stop_sketch6():
	sketching6.last_event = None
	sketching6.last_shape = None
def draw_sketch6(event):
	sketching6.line(sketching6.last_event.x, sketching6.last_event.y, event.x, event.y, color="white", width=1)
	sketching6.last_event = event
def start_sketch7(event):
	sketching7.last_event = event
def stop_sketch7():
	sketching7.last_event = None
	sketching7.last_shape = None
def draw_sketch7(event):
	sketching7.line(sketching7.last_event.x, sketching7.last_event.y, event.x, event.y, color="#2fff00", width=3)
	sketching7.last_event = event
def start_sketch8(event):
	sketching8.last_event = event
def stop_sketch8():
	sketching8.last_event = None
	sketching8.last_shape = None
def draw_sketch8(event):
	sketching8.line(sketching8.last_event.x, sketching8.last_event.y, event.x, event.y, color="#dd8600", width=5)
	sketching8.last_event = event										
#animation functions
'''def move_horse():
	hp = random.randint(0,1)
	_horsec = 0
	if hp == 0:
		horse.show()
		_horsec += 1
	elif hp == 1:
		_horsec += 1
		horse.hide()
	if _horsec == 100:
		horse.hide()'''
def random_waf():
	#color_index_1 = random.randint(0,3)
	x = random.randint(0,100)
	y = random.randint(0,10)
	j = random.randint(0,1)
	if load_waf.get_pixel(x,y) == "black":
		if j == 0:
			load_waf.set_pixel(x,y, "red")
		else:
			load_waf.set_pixel(x,y, "#020202")
	elif load_waf.get_pixel(x,y) == "red":
		load_waf.set_pixel(x,y, "black")
	elif load_waf.get_pixel(x,y) == "black":
		load_waf.set_pixel(x,y, "#020202")
def i_prompt_3_y():
	yes_btn2.hide()
	no_btn2.hide()
	final_btn.show()
	pic_box.show()
	app.bg = "green"
	global_prompt_string.value = i_prompt_2_str
	qp1y_box1.hide()
	qp1y_box2.hide()
	qp1y_box3.hide()
	qp1n_box1.hide()
	qp1n_box2.hide()
def i_prompt_3_n():
	yes_btn2.hide()
	no_btn2.hide()
	final_btn.show()
	app.bg = "blue"
	global_prompt_string.value = i_prompt_2_str_n
	qp1n_box1.hide()
	qp1n_box2.hide()
	qp1y_box1.hide()
	qp1y_box2.hide()
	qp1y_box3.hide()
	qp2n_box1.show()
	sketching3.last_event = None
	sketching3.last_shape = None
	sketching3.when_left_button_pressed = start_sketch3
	sketching3.when_mouse_dragged = draw_sketch3
	sketching3.when_left_button_released = stop_sketch3
	qp2n_box2.show()
	sketching4.last_event = None
	sketching4.last_shape = None
	sketching4.when_left_button_pressed = start_sketch4
	sketching4.when_mouse_dragged = draw_sketch4
	sketching4.when_left_button_released = stop_sketch4
	qp2n_box3.show()
	sketching5.last_event = None
	sketching5.last_shape = None
	sketching5.when_left_button_pressed = start_sketch5
	sketching5.when_mouse_dragged = draw_sketch5
	sketching5.when_left_button_released = stop_sketch5
def q_prompt_2():
	gif_select_i2.hide()
	p1_btn.hide()
	app.bg = "black"
	yes_btn2.show()
	no_btn2.show()
	global_prompt_string.value = p3_f_string
#same level A
def second_prompt_y():
	load_waf.hide()
	yes_btn.hide()
	no_btn.hide()
	app.bg = "black"
	p1_btn.show()
	horse_box.hide()
	global_prompt_string.value = pr2_y
	qp1y_box1.show()
	sketching6.last_event = None
	sketching6.last_shape = None
	sketching6.when_left_button_pressed = start_sketch6
	sketching6.when_mouse_dragged = draw_sketch6
	sketching6.when_left_button_released = stop_sketch6
	qp1y_box2.show()
	sketching7.last_event = None
	sketching7.last_shape = None
	sketching7.when_left_button_pressed = start_sketch7
	sketching7.when_mouse_dragged = draw_sketch7
	sketching7.when_left_button_released = stop_sketch7
	qp1y_box3.show()
	sketching8.last_event = None
	sketching8.last_shape = None
	sketching8.when_left_button_pressed = start_sketch8
	sketching8.when_mouse_dragged = draw_sketch8
	sketching8.when_left_button_released = stop_sketch8
def second_prompt_n():
	load_waf.hide()
	gif_select_i2.show()
	yes_btn.hide()
	no_btn.hide()
	app.bg = "#f26e00"
	p1_btn.show()
	global_prompt_string.value = pr2_n
	qp1n_box1.show()
	sketching1.last_event = None
	sketching1.last_shape = None
	sketching1.when_left_button_pressed = start_sketch1
	sketching1.when_mouse_dragged = draw_sketch1
	sketching1.when_left_button_released = stop_sketch1
	qp1n_box2.show()
	sketching2.last_event = None
	sketching2.last_shape = None
	sketching2.when_left_button_pressed = start_sketch2
	sketching2.when_mouse_dragged = draw_sketch2
	sketching2.when_left_button_released = stop_sketch2
#same level A
def show_yes_no():
	if _n1index == 1 and _n2index == 3 and _v2index == 5 and _v1index == 7:
		app.info("YOU HAVE ESCAPED", "Prime numbers worked in your favor and you have escaped.")
	load_waf.hide()
	horse_box.hide()
	p0_btn.hide()
	gif_select_i1.hide()
	yes_btn.show()
	no_btn.show()
	load_waf.show()
	global_prompt_string.value = p1_display
	global_prompt_string.show()
	load_waf.repeat(5, random_waf)

def zeroth_prompt():
	intro_gif.hide()
	#right_box.hide()
	top_box.hide()
	left_box.hide()
	follow_mat.hide()
	global_prompt_string.hide()
	enter_button.hide()
	app.bg = "black"
	p0_btn.show()
	gif_select_i1.show()
	horse_box.show()
	painting.last_event = None
	painting.last_shape = None
	painting.when_left_button_pressed = start_paint
	painting.when_mouse_dragged = draw_paint
	painting.when_left_button_released = stop_paint
	painting2.last_event = None
	painting2.last_shape = None
	painting2.when_left_button_pressed = start_paint
	painting2.when_mouse_dragged = draw_paint
	painting2.when_left_button_released = stop_paint
	painting3.last_event = None
	painting3.last_shape = None
	painting3.when_left_button_pressed = start_paint
	painting3.when_mouse_dragged = draw_paint
	painting3.when_left_button_released = stop_paint
	painting4.last_event = None
	painting4.last_shape = None
	painting4.when_left_button_pressed = start_paint
	painting4.when_mouse_dragged = draw_paint
	painting4.when_left_button_released = stop_paint
	painting5.last_event = None
	painting5.last_shape = None
	painting5.when_left_button_pressed = start_paint
	painting5.when_mouse_dragged = draw_paint
	painting5.when_left_button_released = stop_paint
	global_prompt_string.value = prompt0
	global_prompt_string.show()
	
# value arrays
#END OF FUNCTION DECLARATIONS.  THE FUNCTIONS KIND OF MOVE UPWARDS IN SEQUENCE
p4_a1 = [" two", " three", " any number of", " one or more"]
p4_a2 = [" geometrical", " formless", " syzygial", " incompatible", " compatible"]
p4_n1 = [" shapes", " abstractions", " bodies", " masses", " thoughts"]
p4_v1 = [" to generate", " to produce", " to be shown", " and you will receive a compilation of"]
p4_n2 = [" compatible ideas", " incompatible ideas", " concrete images", " their logical counterparts", " funny videos", " hilarious images"]
empty5 = []
a1_q = random.randint(0,3)
a2_q = random.randint(0,4)
n1_q = random.randint(0,4)
v1_q = random.randint(0,3)
n2_q = random.randint(0,5)
empty5.append("Draw")
empty5.append(p4_a1[a1_q])
empty5.append(p4_a2[a2_q])
empty5.append(p4_n1[n1_q])
empty5.append("\n")
empty5.append(p4_v1[v1_q])
empty5.append(p4_n2[n2_q])
i_prompt_2_str_n = ''.join(empty5)
_v1_fork = [" obscure", " taint", " sway", " abstract", " infuse", " corrupt", " penetrate"]
_n1_fork = [" mind", " ideas", " nervous system", " ancestral evils", " possessions", " transactional relationships", " entrails"]
_n2_fork = [" data", " perversions", " daggers", " psychosis", " parasites", " locusts", " beliefs"]
_p1_fork = [" can", " will", " would"]
_v2_fork = [" transcend", " fall into", " capture", " subvert", " violate", " distort", " obliterate"]
_n3_fork = [" reality", " biological paradox", " cognition", " morality"]
empty2 = []
vr1_f = random.randint(0,6)
no1_f = random.randint(0,6)
no2_f = random.randint(0,6)
p1_f = random.randint(0,2)
vr2_f = random.randint(0,6)
no3_f = random.randint(0,3)
empty2.append("\n")
empty2.append("If you")
empty2.append(_v1_fork[vr1_f])
empty2.append(" your")
empty2.append(_n1_fork[no1_f])
empty2.append(" with")
empty2.append(_n2_fork[no2_f])
empty2.append(_p1_fork[p1_f])
empty2.append(" you")
empty2.append(_v2_fork[vr2_f])
empty2.append("\n")
empty2.append(_n3_fork[no3_f])
empty2.append("?")
p3_f_string = ''.join(empty2)	
vl1 = [" remove", " feel", " impose", " respect", " secrete"]
nlist = [" melancholy", " your face", " your home", " filth", " a precedent", " your car"]
nlist2 = [" your dreams", " your self", " your thoughts", " a toilet", " your conscious life", " the world"]
prep = [" in", " outside of"]
p1_hold = []
p1_hold.append("Do you")
j = random.randint(0,4)
o = random.randint(0,5)
k = random.randint(0,5)
l = random.randint(0,1)
p1_hold.append(vl1[j])
p1_hold.append(nlist[o])
p1_hold.append(prep[l])
p1_hold.append(nlist2[k])
#p1_hold.append("? NEEDS GIF")
p1_display = ''.join(p1_hold)
promptholder = []
nouns2 = [" an wall", " a cave", " a series of closeups.", " images of dissimilarities", " a vantage point.", " a thermal image.", " an inverted crop.", " a duplication."]
nouns1 = [" miasma", " circular forms", " asymmetries", " entrails", " limbs", " eyes",  " animals", " sources of light"]
verblst2 = ["produce", "create", "describe", "conjure", "compose"]
verblst1 = ["Indicate", "Remove", "Augment", "Highlight", "Pair up", "Transform", "Enlarge", "Eliminate"]
_n1index = random.randint(0,7)
_n2index = random.randint(0,7)
_v1index = random.randint(0,7)
_v2index = random.randint(0,4)
promptholder.append(verblst1[_v1index])
promptholder.append(nouns1[_n1index])
promptholder.append(" to ")
promptholder.append("\n")
promptholder.append(verblst2[_v2index])
promptholder.append(nouns2[_n2index])
prompt0 = ''.join(promptholder)
vrb1 = ["Draw", "Sketch", "Arrange"]
noun0 = [" series", " sequence", " tryptich"]
adj1 = [" strange", " globular", " gelatinous", " sessile", " patronymic", " harmonious", " seven-fold", " chimeric"]
nounz1 = [" connections", " lines", " conclusions", " invertebrates", " fins", " abstractions", " abominations", " serpents"]
prps2 = [" in", " harboring", " surrounding", " residing in", " depriving a village of", " creating a conflict within", " shifting tides of", " complacent in"]
nounz2 = [" war", " libidinal force", " time", " a home", " a vision of hell", " a concavity", " a toroid highway"]
blank = []
_v1 = random.randint(0,2)
_n0 = random.randint(0,2)
_a1 = random.randint(0,7)
_n1 = random.randint(0,7)
_p2 = random.randint(0,7)
_n2 = random.randint(0,6)
blank.append(vrb1[_v1])
blank.append(" a")
blank.append(noun0[_n0])
blank.append(" of")
blank.append("\n")
blank.append(adj1[_a1])
blank.append(nounz1[_n1])
blank.append("\n")
blank.append(prps2[_p2])
blank.append(nounz2[_n2])
blank.append("\n")
#blank.append(" LS YES 1")
pr2_y = ''.join(blank) #after clicking yes for 1st time update global prompt string to this
prEmpty = []
# NOT ALLOCATED
p3_v1 = [" demonstrating", " depicting", " containing", " devoid of", " lacking", " with an abundance of", " unrelated to"]
p3_n1 = [" abstraction", " sessility", " botany", " stability", " continuity", " fertility", " uniformity", " division", " morbidity"]
p3_v2 = [" to reveal", " and the program will generate", ", a successful selection will present", " to be rewarded with", " to receive", " to produce"]
p3_n2 = [" an unobstructed image", " the terms of victory", " a blank screen", " a verbal paradox", " the underlying connection", " the intended pattern"]
empty4 = []
m = random.randint(0,6)
m1 = random.randint(0,8)
m2 = random.randint(0,5)
m3 = random.randint(0,5)
empty4.append("Select all images")
empty4.append(p3_v1[m])
empty4.append(p3_n1[m1])
empty4.append("\n")
empty4.append(p3_v2[m2])
empty4.append(p3_n2[m3])
i_prompt_2_str = ''.join(empty4)
_vv1 = ["Draw", "Sketch", "Trace", "Cross out", "Connect"]
_adj1 = [" most important", " most inconsequential", " least important", " obviously grotesque", " clearly superfluous", " epistemically significant", " interchangeable"]
_nn1 = [" portion of", " feature of", " section of", " theme present in"]
_nn2 = [" image", " subject", " composition"]
_vv2 = [" produce", " generate", " reveal"]
_nn3 = [" the true image", " the logical form", " a correct representation", " the full image", " the rest of the series"]
_ver1 = random.randint(0,4)
_ad1 = random.randint(0,6)
_non1 = random.randint(0,3)
_non2 = random.randint(0,2)
_ver2 = random.randint(0,2)
_non3 = random.randint(0,4)
prEmpty.append(_vv1[_ver1])
prEmpty.append(" the")
prEmpty.append(_adj1[_ad1])
prEmpty.append(_nn1[_non1])
prEmpty.append("\n")
prEmpty.append(" the")
prEmpty.append(_nn2[_non2])
prEmpty.append(" in order to")
prEmpty.append("\n")
prEmpty.append(_vv2[_ver2]) 
prEmpty.append(_nn3[_non3])
prEmpty.append("\n")
#prEmpty.append("LS NO 1")
pr2_n = ''.join(prEmpty)
#global stuff
app = App(layout = "grid", bg = "black")
app.tk.attributes("-fullscreen", True)
#pictures shown variably
global_prompt_string = Text(app, font="Comic Sans", grid = [2,0], color="white", size=18)
follow_mat = Picture(app, image="titlepage/followmatte2.gif", grid = [1,2], width = 900, height = 150)
intro_gif = Picture(app, image="titlepage/continue.gif", grid = [1,3], width = 900, height = 115)
enter_button = PushButton(app, image="titlepage/enterbutton.png", grid = [1,4], width = 220, height = 50, command=zeroth_prompt) 
yes_btn = PushButton(app, image="titlepage/yes1.png", width = 100, height = 70, grid = [0,0], command=second_prompt_y)
yes_btn.hide()
gif_select_i1 = Picture(app, grid=[0,1], width = 300, height = 500)
sel_i1 = random.randint(0,4)
if sel_i1 == 0:
	gif_select_i1.image = "iprompt1gifs/acorn1.gif"
elif sel_i1 == 1:
	gif_select_i1.image = "iprompt1gifs/acorndix.gif"
elif sel_i1 == 2:
	gif_select_i1.image = "iprompt1gifs/blobbin.gif"
elif sel_i1 == 3:
	gif_select_i1.image = "iprompt1gifs/humannude.gif"
else:
	gif_select_i1.image = "iprompt1gifs/prewormm.gif"
gif_select_i1.hide()
gif_select_i2 = Picture(app, grid = [0,3], width = 300, height = 400)
sel_i2 = random.randint(0,4)
if sel_i2 == 0:
	gif_select_i2.image = "Nqprompt1gifs/eyegoop.gif"
elif sel_i2 == 1:
	gif_select_i2.image = "Nqprompt1gifs/manowar.gif"
elif sel_i2 == 2:
	gif_select_i2.image = "Nqprompt1gifs/mold.gif"
elif sel_i2 == 3:
	gif_select_i2.image = "Nqprompt1gifs/whalepus.gif" #problem
else:
	gif_select_i2.image = "Nqprompt1gifs/pill.gif"
gif_select_i2.hide()
#INTERIM TEXT OBJECTS TO BE TURNED INTO PICTURE OBJECTS
pic_box = Box(app, layout="grid", grid = [2,2])
pic_button1 = PushButton(pic_box, grid=[0,0], width = 150, height = 150, command = disable1)
pic_button2 = PushButton(pic_box, grid=[1,1], width = 150, height = 150, command = disable2)
pic_button3 = PushButton(pic_box, grid=[1,0], width = 150, height = 150, command = disable3)
pic_button4 = PushButton(pic_box, grid=[4,1], width = 150, height = 150, command = disable4)
pic_dict = {1: "qprompt2Y/p_img_1.png", 2: "qprompt2Y/p_img_1.png", 3: "qprompt2Y/p_img_3.jpg", 4: "qprompt2Y/p_img_4.png", 5: "qprompt2Y/p_img_5.jpg", 6: "qprompt2Y/p_img_6.jpg", 7: "qprompt2Y/p_img_7.jpg", 8: "qprompt2Y/p_img_8.jpg", 9: "qprompt2Y/p_img_9.jpg", 10: "qprompt2Y/p_img_10.jpg", 11: "qprompt2Y/p_img_11.jpg", 12: "qprompt2Y/p_img_12.jpg", 13: "qprompt2Y/p_img_13.jpg", 14: "qprompt2Y/p_img_14.png", 15: "qprompt2Y/p_img_15.jpg", 16: "qprompt2Y/p_img_16.jpg", 17: "qprompt2Y/p_img_17.jpg", 18: "qprompt2Y/p_img_18.jpg", 19: "qprompt2Y/p_img_19.jpg", 20: "qprompt2Y/p_img_20.jpg", 21: "qprompt2Y/p_img_21.png", 22: "qprompt2Y/p_img_22.png", 23: "qprompt2Y/p_img_23.png", 24: "qprompt2Y/p_img_24.jpg" }
a = random.sample(range(1,24), 23)
b = random.randint(1,6)
if b == 1:
	pic_button1.image = pic_dict[a[0]]
	pic_button2.image = pic_dict[a[1]]
	pic_button3.image = pic_dict[a[2]]
	pic_button4.image = pic_dict[a[3]]
elif b == 2:
	pic_button1.image = pic_dict[a[4]]
	pic_button2.image = pic_dict[a[5]]
	pic_button3.image = pic_dict[a[6]]
	pic_button4.image = pic_dict[a[7]]
elif b == 3:
	pic_button1.image = pic_dict[a[8]]
	pic_button2.image = pic_dict[a[9]]
	pic_button3.image = pic_dict[a[10]]
	pic_button4.image = pic_dict[a[11]]
elif b == 4:
	pic_button1.image = pic_dict[a[12]]
	pic_button2.image = pic_dict[a[13]]
	pic_button3.image = pic_dict[a[14]]
	pic_button4.image = pic_dict[a[15]]
elif b == 5:
	pic_button1.image = pic_dict[a[16]]
	pic_button2.image = pic_dict[a[17]]
	pic_button3.image = pic_dict[a[18]]
	pic_button4.image = pic_dict[a[19]]
elif b == 6:
	pic_button1.image = pic_dict[a[20]]
	pic_button2.image = pic_dict[a[21]]
	pic_button3.image = pic_dict[a[22]]
	pic_button4.image = pic_dict[24]
pic_box.hide()
p0_btn = PushButton(app, command=show_yes_no, image = "buttons/proceed1.png", grid = [0,0], width = 100, height = 50)
p0_btn.hide()
no_btn = PushButton(app, image="buttons/no1.png", width = 100, height = 100, grid = [0,1], command=second_prompt_n)
no_btn.hide()
p1_btn = PushButton(app, image = "buttons/proceed1.png", grid = [1,3], height = 100, width = 70, command=q_prompt_2)
p1_btn.hide()
yes_btn2 = PushButton(app, image="buttons/yes1.png", grid = [0,3], width = 100, height = 100, command=i_prompt_3_y)
yes_btn2.hide()
no_btn2 = PushButton(app, image = "buttons/no1.png", grid = [0,1], width = 100, height = 100, command=i_prompt_3_n)
no_btn2.hide()
final_btn = PushButton(app, grid = [0,2], image = "buttons/resultbutton2.png", width = 100, height = 50)
final_btn.hide()
load_waf = Waffle(app, width = 1000, height = 100, pad = 6, dim = 4, grid = [3,8], color = "black")
load_waf.hide()
#BOXES FOR TITLE SCREEN
#right_box = Box(app, grid = [2,0], width = 100)
#nudge_box = Box(app, grid = [1,1], width = 300, height = 100)
left_box = Box(app, grid = [0,1], width = 20)
#left_box2 = Box(app, grid = [1,3], width = 200, height = 50)
top_box = Box(app, grid = [2,0], height = 150)
horse_box = Box(app, layout = "grid", grid = [2,1], width=360, height=640, border=True)
horse_box.hide()
painting = Drawing(horse_box, grid = [0,0], width="360", height="180")
painting2 = Drawing(horse_box, grid = [0,1], width="360", height="60")
painting3 = Drawing(horse_box, grid = [0,2], width="360", height="100")
painting4 = Drawing(horse_box, grid = [0,3], width="360", height="100")
painting5 = Drawing(horse_box, grid = [0,4], width="360", height="20")
qp1n_box1 = Box(app, layout = "grid", grid = [2,3], width=300, height=500, border=False)
qp1n_box1.hide()
sketching1 = Drawing(qp1n_box1, grid = [0,0], width = "300", height = "500")
qp1n_box2 = Box(app, layout = "grid", grid = [3,3], width=300, height=500, border=True)
qp1n_box2.hide()
sketching2 = Drawing(qp1n_box2, grid = [0,0], width = "300", height = "500")
qp2n_box1 = Box(app, layout = "grid", grid = [1,1], width=200, height=300, border=True)
qp2n_box1.hide()
sketching3 = Drawing(qp2n_box1, grid = [0,0], width = "200", height = "300")
qp2n_box2 = Box(app, layout = "grid", grid = [2,1], width=200, height=300, border=True)
qp2n_box2.hide()
sketching4 = Drawing(qp2n_box2, grid = [0,0], width = "200", height = "300")
qp2n_box3 = Box(app, layout = "grid", grid = [3,1], width=200, height=300, border=True)
qp2n_box3.hide()
sketching5 = Drawing(qp2n_box3, grid = [0,0], width = "200", height = "300")
qp1y_box1 = Box(app, layout = "grid", grid = [2,3], width=200, height=300, border=True)
qp1y_box1.hide()
sketching6 = Drawing(qp1y_box1, grid = [0,0], width = "200", height = "500")
qp1y_box2 = Box(app, layout = "grid", grid = [5,3], width=600, height=500, border=True)
qp1y_box2.hide()
sketching7 = Drawing(qp1y_box2, grid = [0,0], width = "200", height = "500")
qp1y_box3 = Box(app, layout = "grid", grid = [6,3], width=200, height=300, border=True)
qp1y_box3.hide()
sketching8 = Drawing(qp1y_box3, grid = [0,0], width = "200", height = "300")
app.display()
