# Made by Joe Jagger, 03/10/2024 - Finished: TBF
#
#  .M"""bgd `7MMF' `YMM'`YMM'   `MM'`7MN.   `7MF'`7MM"""YMM MMP""MM""YMM 
# ,MI    "Y   MM   .M'    VMA   ,V    MMN.    M    MM    `7 P'   MM   `7 
# `MMb.       MM .d"       VMA ,V     M YMb   M    MM   d        MM      
#   `YMMNq.   MMMMM.        VMMP      M  `MN. M    MMmmMM        MM      
# .     `MM   MM  VMA        MM       M   `MM.M    MM   Y  ,     MM      
# Mb     dM   MM   `MM.      MM       M     YMM    MM     ,M     MM      
# P"Ybmmd"  .JMML.   MMb.  .JMML.   .JML.    YM  .JMMmmmmMMM   .JMML.    
# 
# SKYNET NODE SELECTOR
# DO NOT USE THIS TO START YOUR NODES, ONLY TO CONFIGURE THEM
#

import json
import os
import datetime
print(f"> Skynet init phase triggered @ {datetime.datetime.now()}")
node_types = {
    1: "Central Server",
    2: "Camera-enabled device",
    3: "Generic"
}
if os.path.isfile("skynet.json"):
    print("> Config exists.")
    with open("skynet.json", "r") as skyconf_file:
        skyconf = json.load(skyconf_file)
        ver = skyconf['ver']
        ntype = skyconf['nodetype']
        unconfigured = skyconf['unconfigured']
    if unconfigured and ntype == "undefined":
        print(f"> Config read success.\nRunning Skynet {ver}\n> Node is unconfigured.")
        print("--------------------\nThis node is unconfigured. Please select one of the following options:")

        chosen_node_id = int(input("1: Main Server\n2: Camera enabled device\n3: Generic / multi-use\n> "))
        print(f"You have chosen {node_types[chosen_node_id]} as your chosen nodetype. Are you sure this is correct?")
        yesno = input("Yes / No\n> ").lower()
        if yesno == "yes":
            skyconf['nodetype'] = node_types[chosen_node_id]
            skyconf['unconfigured'] = False
            
            with open("skynet.json", "w") as skyconf_file:
                json.dump(skyconf, skyconf_file, indent=4)
            print("> Node configured successfully.")
            print("> Please restart the launcher.")
        else:
            print("> Node configuration aborted.")
    else:
        print(f"> Config read success.\Running Skynet {ver}\n> Node is configured as a {ntype}.\n> Please run skynet/nodetypes/{ntype}.py manually.")
        print("------------LAUNCHER PHASE END------------")
        exit()

else:
    print("Config does not exist or we don't have access to it.")
    exit()