#die methode wie man die Fibonacci zahlen errechnet
def fibo(n):
    a, b = 0, 1
    for start in range(n):
       #1, 1 = 1, 0 + 1
        a, b = b, a + b
    return a
#user abfrage ab welcher fibonacci zahl man beginnen soll
start = input("Von :")
#user abfrage bei welcher man aufhören soll
end = input("Bis :")

#sollange von nicht end erreicht hat wird die schleife ausgeführt
while start != end:
    if fibo(int(start)) != fibo(int(end)):
        print(fibo(int(start)))
        start = int(start) + 1

