import numpy as np
class MovingAverage:
    '''
    This class computes the moving average using a circular buffer that is stored inside the object and keeps updating after every computation.
    Notice that it stores the moving_average (self.ma) vector, although it can be easily modified so it only keeps in memory the circular buffer
    and its udpate index.    '''

    def __init__(self, win_size):
        self.buffer      = np.zeros(win_size);
        self.buff_runner = 0;
        self.ma = [None];
        self.win_size = win_size;
        
    def compute_start(self, x):
        '''Used when the buffer is just initialized and empty.
        Notice that the system stores the moving_average data of the whole signal. However, it can be easily modified so this content is not stored
        inside of the object, which might be useful when data is massive.
        '''
        self.ma = np.zeros(len(x));
        for i in range(len(x)):
            self.buffer[self.buff_runner] = x[i];
            self.ma[i] = np.mean(self.buffer);

            self.buff_runner += 1;
            if self.buff_runner == self.win_size:
                self.buff_runner = 0;
                
    def compute_online(self, x):
        '''
        In this case, the user can provide a single value to compute its moving average respecting to previous values computed by the same system.
        Notice that it is performed for a single sample, so this function can be used in systems that actually require the current value of their 
        moving average.
        '''
        
        # SECURITY CHECK
        if (len(self.ma) == 1) & (self.ma[0] == None):
            print('Run first compute_start(x)!')
            return -1
            
        self.buffer[self.buff_runner] = x;
        self.ma = np.append(self.ma, np.mean(self.buffer))
        
        self.buff_runner += 1;
        if self.buff_runner == self.win_size:
            self.buff_runner = 0;
            
    def give_ma(self):
        return self.ma
    def give_buffer(self):
        return self.buffer, self.buff_runner
            
