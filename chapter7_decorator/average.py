def make_average():
    series=[]

    def average(new_value):
        series.append(new_value)
        total=sum(series)
        return total/len(series)

    return average

# 返回值为average函数
a = make_average()



def make_averager():
    count=0
    total=0
    def average(new_value):
        nonlocal count,total
        count+=1
        total+=new_value
        return total/count
    return average
if __name__ == '__main__':

    a=make_averager()
    print(a(1))
    print(a(2))







