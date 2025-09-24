class Processo:
    def __init__(self, pid, arrivalTime, burstTime):
        self.pid = pid                    
        self.arrivalTime = arrivalTime    
        self.burstTime = burstTime        
        self.burstTimeRemaining = burstTime 
        self.isComplete = False          
        self.inQueue = False              