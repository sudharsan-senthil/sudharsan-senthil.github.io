t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    s_d, t_d = {}, {}    
    s_s, t_s = set(), set()
    for i in range(n):
        if S[i] in s_s:
            s_d[S[i]] += 1
        else:
            s_s.add(S[i])
            s_d[S[i]] = 1 

        if T[i] in t_s:
            t_d[T[i]] += 1
        else:
            t_s.add(T[i]) 
            t_d[T[i]] = 1
    for key_s in s_d.keys():
        if key_s in t_s:
            if t_d[key_s] >= s_d[key_s]:
                t_d[key_s] -= s_d[key_s]
                s_d[key_s] = 0
            else:
                s_d[key_s] -= t_d[key_s]
                t_d[key_s] = 0

    s_e, t_e = list(s_d.keys()), list(t_d.keys())
    tn_d = {}
    sn_d = {}
    for i in range(k):
        tn_d[i] = 0
    for key_t in t_d.keys():
        tn_d[key_t%k] = t_d[key_t]

    for i in range(k):
        sn_d[i] = 0
    for key_s in s_d.keys():
        sn_d[key_s%k] = s_d[key_s]
    for j in range(1,int((k+1)/2)):
        # if i == k - j - 1:
        #     break
        # print(j)
        tn_d[j] += tn_d[k-j]
        sn_d[j] += sn_d[k-j]

    flag = False
    for i in range(int((k+1)/2)):
        if tn_d[i] != sn_d[i]:
            # if k%2 == 1 and i == int((k+1)/2):
            #     continue
            print("NO")
            flag = True            
            break
    if not flag:
        print("YES")    
    # print(tn_d)
    # print(sn_d)

    