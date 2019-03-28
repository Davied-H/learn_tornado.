import  multiprocessing

def par(name):
    print(name)

def par1(name):
    print(name)
if __name__ == "__main__":
    p = multiprocessing.Process(target=par,args=("dong",))
    p1 = multiprocessing.Process(target=par1,args=("xixi",))
    p.start()
    p1.start()
    p.join()
    p1.join()
    print(p.pid,p1.pid)
