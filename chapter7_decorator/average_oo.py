class Average():
    def __init__(self):
        self.series=[]

    def __call__(self,new_value):
        self.series.append(new_value)
        total=sum(self.series)
        return total/len(self.series)

    def avg(self):
        print('sd')

if __name__ == '__main__':

    a = Average()




