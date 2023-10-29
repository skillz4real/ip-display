class file_handler():
    def log_ip_update(self):        
        with open("log.txt","a+") as log:
            log.write(f"the ip-display was updated on {datetime.now()}\n")
        
    def log_reminder(self):
        with open("log.txt","a+") as log:
            log.write(f"Displayed a reminder on {datetime.now()}\n")
