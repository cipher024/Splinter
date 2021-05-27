import os,sys

def done():
  ac = input("Task done Press R to split another combo or Q to quit" + "\n")
  if "R" or "r" in ac :
     splt()
  elif "Q" or "q" in ac:
    quit()

def splt():
  print("\n"+"\n")
  print(" __     ___     __    _____       __   _____     __     __  ")
  print("/ _\   / _ \   / /    \_   \   /\ \ \ /__   \   /__\   /__\ ")
  print("\ \   / /_)/  / /      / /\/  /  \/ /   / /\/  /_\    / \// ")
  print("_\ \ / ___/  / /___ /\/ /_   / /\  /   / /    //__   / _  \ ")
  print("\__/ \/      \____/ \____/   \_\ \/    \/     \__/   \/ \_/   Made by cipher 420 ")
  print("                                                            ")
  combo = input("Entre the combo list that you want to split : " + '\n')
  spliter = input("entre the spliter used : " + '\n')
  savepath = input("Entre the path where the splited pass/email will be saved :" + '\n')
  if not savepath.endswith(r"\\"):
     savepath= savepath + r"\\"
  with open(combo,'rt') as combo:
    with open(savepath+'usernames.txt','wt') as x:
        with open(savepath+'passwords.txt','wt') as y:
            for line in combo:
                combo = line.strip().split(spliter)
                x.write(combo[0] + '\n')
                y.write(combo[1] + '\n') 
  done()
splt()
