from colorama import Fore

def itemToSlug(itemName):
    itemName = itemName.lower()
    slug = itemName.replace(" ", "_")

    return slug

def title():
    print(r"__________.__          __ " + Fore.BLUE + r"___________.__            .___            " + Fore.RESET)
    print(r"\______   \  | _____ _/  |" + Fore.BLUE + r"\_   _____/|__| ____    __| _/___________ " + Fore.RESET)
    print(r" |     ___/  | \__  \\   __" + Fore.BLUE + r"\    __)  |  |/    \  / __ |/ __ \_  __ \\" + Fore.RESET)
    print(r" |    |   |  |__/ __ \|  | " + Fore.BLUE + r"|     \   |  |   |  \/ /_/ \  ___/|  | \/" + Fore.RESET)
    print(r" |____|   |____(____  /__| " + Fore.BLUE + r"\___  /   |__|___|  /\____ |\___  >__|   " + Fore.RESET)
    print(r"                    \/       " + Fore.BLUE + r"  \/            \/      \/    \/       " + Fore.RESET)