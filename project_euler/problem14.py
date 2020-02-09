'''
양의 정수 n에 대하여 다음과 같은 계산 과정을 반복
n -> n/2  (n짝수)
n -> 3n+1 (n홀수)

EX) 13에 대해 10번 과정을 통해 1
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 ->1

백만 이하의 수로 시작했을 때 1까지 도달하는 데
가장 긴 과정을 거치는 숫자는?
(계산 과전 도중에 숫자가 백만을 넘어도 됨)

해결 X
'''

li = list([1]*1000000)
for i in range(0,1000000):

    while i!=1 :
        if i%2==0:
            i = i//2
            li[i]+=1
        else :
            i = 3*i+1
            li[i] += 1