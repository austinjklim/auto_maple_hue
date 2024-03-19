import tkinter as tk
from src.gui.interfaces import Tab, Frame, LabelFrame
from src.common import config
from src.common.interfaces import Configurable

class Runtime_Flags(Tab):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, 'Monitoring', **kwargs)
        self.threadMonitor = Thread_Monitor(self)
        self.threadMonitor.pack(fill=tk.BOTH, padx=5,pady=5)
        self.runtimeFlags = Runtime_Flags_Frame(self)
        self.runtimeFlags.pack(fill=tk.BOTH, padx=5,pady=5)

class Thread_Monitor(LabelFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, 'Threads Running', **kwargs)

        self.botThread = tk.StringVar()
        self.captureThread = tk.StringVar()
        self.notifierThread = tk.StringVar()
        self.listenerThread = tk.StringVar()
        self.watcherThread = tk.StringVar()

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)

        threadDict = {
            "bot_thread":{"entryObj":None, "status":self.botThread},
            "capture_thread":{"entryObj":None, "status":self.captureThread},
            "listener_thread":{"entryObj":None, "status":self.notifierThread},
            "watcher_thread":{"entryObj":None, "status":self.listenerThread},
            "notifier_thread":{"entryObj":None, "status":self.watcherThread}
        }

        for thread in threadDict.keys():
            label = tk.Label(self, text=thread)
            label.grid(column=0,padx=5,pady=5,sticky=tk.EW)
            rowNow = label.grid_info()['row']
            threadDict[thread]["entryObj"]=tk.Entry(self, textvariable=threadDict[thread]["status"], state=tk.DISABLED)
            threadDict[thread]["entryObj"].grid(row=rowNow,column=1,padx=5,pady=5, sticky=tk.EW)

    def check_threads(self):
        self.botThread.set(str(config.bot.thread.is_alive()))
        self.captureThread.set(str(config.capture.thread.is_alive()))
        self.listenerThread.set(str(config.listener.thread.is_alive()))
        self.watcherThread.set(str(config.watcher.thread.is_alive()))
        self.notifierThread.set(str(config.notifier.thread.is_alive()))

class Runtime_Flags_Frame(LabelFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, 'Runtime Flags', **kwargs)

        self.enabled_flag = tk.StringVar()
        self.rune_cd_flag = tk.StringVar()
        self.cursed_rune_flag = tk.StringVar()
        self.no_damage_numbers_flag = tk.StringVar()
        self.map_overcrowded_flag = tk.StringVar()
        self.violetta_minigame_flag = tk.StringVar()
        self.lie_detector_failed_flag = tk.StringVar()
        self.game_disconnected_flag = tk.StringVar()
        self.character_dead_flag = tk.StringVar()
        self.chatbox_msg_flag = tk.StringVar()
        self.stuck_in_cs_flag = tk.StringVar()
        self.player_stuck_flag = tk.StringVar()
        self.polo_portal_flag = tk.StringVar()
        self.especia_portal_flag = tk.StringVar()
        self.char_in_town_flag = tk.StringVar()

        flaglist = ["bot_enabled", 
                    "rune_cd", 
                    "cursed_rune", 
                    "no_damage_numbers", 
                    "map_overcrowded", 
                    "violetta_minigame", 
                    "lie_detector_failed",
                    "game_disconnected",
                    "character_dead",
                    "chatbox_msg",
                    "stuck_in_cs",
                    "player_stuck",
                    "especia_portal",
                    "char_in_town"
                    ]
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)

        for i in range(len(flaglist)):
            tk.Label(self, text=flaglist[i]).grid(row=i, column=0, padx=5, pady=5, sticky=tk.EW)

        self.f1v = tk.Entry(self, textvariable=self.enabled_flag, state=tk.DISABLED).grid(row=0, column=1, padx=(0, 5), pady=(5, 0), sticky=tk.EW)
        self.f2v = tk.Entry(self, textvariable=self.rune_cd_flag, state=tk.DISABLED).grid(row=1, column=1, padx=(0, 5), pady=(5, 0), sticky=tk.EW)
        self.f3v = tk.Entry(self, textvariable=self.cursed_rune_flag, state=tk.DISABLED).grid(row=2, column=1, padx=(0, 5), pady=(5, 0), sticky=tk.EW)
        self.f4v = tk.Entry(self, textvariable=self.no_damage_numbers_flag, state=tk.DISABLED).grid(row=3, column=1, padx=(0, 5), pady=(5, 0), sticky=tk.EW)
        self.f5v = tk.Entry(self, textvariable=self.map_overcrowded_flag, state=tk.DISABLED).grid(row=4, column=1, padx=(0, 5), pady=(5, 0), sticky=tk.EW)
        self.f6v = tk.Entry(self, textvariable=self.violetta_minigame_flag, state=tk.DISABLED).grid(row=5, column=1, padx=(0, 5), pady=(5, 0), sticky=tk.EW)
        self.f7v = tk.Entry(self, textvariable=self.lie_detector_failed_flag, state=tk.DISABLED).grid(row=6, column=1, padx=(0, 5), pady=(5, 0), sticky=tk.EW)
        self.f8v = tk.Entry(self, textvariable=self.game_disconnected_flag, state=tk.DISABLED).grid(row=7, column=1, padx=(0, 5), pady=(5, 0), sticky=tk.EW)
        self.f9v = tk.Entry(self, textvariable=self.character_dead_flag, state=tk.DISABLED).grid(row=8, column=1, padx=(0, 5), pady=(5, 0), sticky=tk.EW)
        self.f10v = tk.Entry(self, textvariable=self.chatbox_msg_flag, state=tk.DISABLED).grid(row=9, column=1, padx=(0, 5), pady=(5, 0), sticky=tk.EW)
        self.f11v = tk.Entry(self, textvariable=self.stuck_in_cs_flag, state=tk.DISABLED).grid(row=10, column=1, padx=(0, 5), pady=(5, 0), sticky=tk.EW)
        self.f12v = tk.Entry(self, textvariable=self.player_stuck_flag, state=tk.DISABLED).grid(row=11, column=1, padx=(0, 5), pady=(5, 0), sticky=tk.EW)
        self.f14v = tk.Entry(self, textvariable=self.especia_portal_flag, state=tk.DISABLED).grid(row=12, column=1, padx=(0, 5), pady=(5, 0), sticky=tk.EW)
        self.f15v = tk.Entry(self, textvariable=self.char_in_town_flag, state=tk.DISABLED).grid(row=13, column=1, padx=(0, 5), pady=(5, 0), sticky=tk.EW)


    def update_All_Flags(self):
        self.enabled_flag.set(str(config.enabled))
        self.rune_cd_flag.set(str(config.rune_cd))
        self.cursed_rune_flag.set(str(config.cursed_rune))
        self.no_damage_numbers_flag.set(str(config.no_damage_numbers))
        self.map_overcrowded_flag.set(str(config.map_overcrowded))
        self.violetta_minigame_flag.set(str(config.violetta_minigame))
        self.lie_detector_failed_flag.set(str(config.lie_detector_failed))
        self.game_disconnected_flag.set(str(config.game_disconnected))
        self.character_dead_flag.set(str(config.character_dead))
        self.chatbox_msg_flag.set(str(config.chatbox_msg))
        self.stuck_in_cs_flag.set(str(config.stuck_in_cs))
        self.player_stuck_flag.set(str(config.player_stuck))
        self.especia_portal_flag.set(str(config.especia_portal))
        self.char_in_town_flag.set(str(config.char_in_town))