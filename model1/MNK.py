import csv

def k(x, y):
    n = len(x)
    x_ = 0
    y_ = 0
    x2_ = 0
    xy_ = 0

    for i in range(n):
        x_ = x_ + x[i]
        y_ = y_ + y[i]
        x2_ = x2_ + x[i] * x[i]
        xy_ = xy_ + x[i] * y[i]

    x_ = x_ / n
    y_ = y_ / n
    x2_ = x2_ / n
    xy_ = xy_ / n

    a = (xy_ - x_ * y_) / (x2_ - x_ * x_)
    b = y_ - a * x_
    print(a)
    print(b)
    return a

def readfromfile(pair):

    filenames = {
        "EUR-USD" : "EURUSD.CSV",
        "EUR-RUB" : "EURRUB.CSV",
        "USD-RUB" : "USDRUB.CSV",
    }

    res = open("files/" + filenames[pair] ,"rt")
    i=0;
    s=list();
    reader = csv.DictReader(res, delimiter=';')

    for line in reader:
        s.append(float(line['Close']))
        print(s[i])
        i=i+1

    return k(range(1,26),s)


