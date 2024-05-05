from termcolor import colored
shellMenu = 1
print("Welcome to...")
shellsetup = colored('''
         __         ____          __            
   _____/ /_  ___  / / /_______  / /___  ______  
  / ___/ __ \/ _ \/ / / ___/ _ \/ __/ / / / __ \ 
 (__  ) / / /  __/ / (__  )  __/ /_/ /_/ / /_/ / 
/____/_/ /_/\___/_/_/____/\___/\__/\__,_/ .___/  
                                       /_/     ''', 'green' )
print(shellsetup)
while shellMenu == 1:
    menuAnswer = int(input("Do you want \n (1) Full setup \n (2) Lite setup \n (3) More info \n "))
    if menuAnswer == 1:
        shellAnswer = int(input("What shell do you want to use? \n (1) zsh \n (2) bash \n (3) skip shell config \n "))
        shellMenu = 0
    elif menuAnswer == 2:
        shellMenu = 0
    elif menuAnswer == 3:
        print("The full setup consists of all customisation options including setting the chosen shell as default, aliases, oh my (shell) installation and plugins. \nThe light setup consists of only setting the default shell without aliases and other features. To list packages, run with -p flag.")
    else:
        pass
