#!/usr/bin/python
import pyautogui
import webbrowser
import time

message = input("Pesan apa Yang kamu Mau kirim : ")
repeats = int(input("Seberapa Banyak Pesan Yang Mau Kamu Kirim? : "))
delay = int(input("Berapa Lama (miliseccond) Yang Mau kamu Tunggu? : "))

isLoaded = input("Klik Tombol Enter Untuk Mengirim")



print("Kamu Punya Waktu 5 Detik Untuk Masuk Ke Aplikasi Messenger Kamu")

time.sleep(5)


for i in range(0,repeats):         #Message sending loop
	if message != "":
		pyautogui.typewrite(message)     
		pyautogui.press("enter")
	else:
		pyautogui.hotkey('ctrl', 'v')      
		pyautogui.press("enter")

	time.sleep(delay/1000)


print("Done\n")