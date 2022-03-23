# use indices to denote values that the variable takes on
B = [0.99, 0.01]
E = [0.98, 0.02]
# outer index is B; inner is E. don't do this at home.
A = [[[0.99, 0.01], [0.10, 0.90]], [[0.05, 0.95], [0.01, 0.99]]]
# outer index is value of A
# F = [[0.95, 0.05], [0.25, 0.75]]
F = [[[0.99, 0.01], [0.98, 0.02]], [[0.97, 0.03], [0.96, 0.04]]]
L = [[0.90, 0.10], [0.05, 0.95]]

# P(F) -- same as before
PF = [0, 0]
for f in [0, 1]:
    for b in [0,1]: 
        for e in [0,1]:
            for a in [0,1]:
                for l in [0,1]:
                    # P(F|A)P(L|A)P(A|B,E)P(B)P(E)
                    PF[f] += F[a][b][f]*L[a][l]*A[b][e][a]*B[b]*E[e]
PFdoA = [[0,0], [0,0]]
for f in [0, 1]:
    for a in [0,1]:
        for l in [0,1]:
            for b in [0,1]:
                # P(F|do(A))P(L|do(A))P(B)
                PFdoA[a][f] += F[a][b][f]*L[a][l]*B[b]



print(PF, PFdoA) # [0.924079, 0.075921]
print(PF[0] + PF[1]) # 1.0

# now make B a cause of F
# outer index is value of A, inner B


PFdoA1 = [0,0]
for f in [0,1]:
    for l in [0,1]:
        for b in [0,1]:
            PFdoA1[f] += F[1][b][f] * L[1][l] * B[b]

PFdoA0 = [0,0]
for f in [0,1]:
    for l in [0,1]:
        for b in [0,1]:
            PFdoA0[f] += F[0][b][f] * L[0][l] * B[b]
print(PFdoA1, PFdoA0)

EFdoA1 = sum([f * PFdoA1[f] for f in range(len(PFdoA1))])
EFdoA0 = sum([f * PFdoA0[f] for f in range(len(PFdoA0))])
print(EFdoA1 - EFdoA0)




# # # under A=0
# # B = [0.99, 0.01]
# # E = [0.98, 0.02]
# # # outer index is B; inner is E. don't do this at home.
# # A = [[[1, 0], [1, 0]], [[1, 0], [1, 0]]]
# # # outer index is value of A
# # F = [[0.95, 0.05], [0.25, 0.75]]
# # L = [[0.90, 0.10], [0.05, 0.95]]

# # # P(F) -- naive
# # PF = [0, 0]
# # for f in [0, 1]:
# #     for b in [0,1]: 
# #         for e in [0,1]:
# #             for a in [0,1]:
# #                 for l in [0,1]:
# #                     # P(F|A)P(L|A)P(A|B,E)P(B)P(E)
# #                     PF[f] += F[a][f]*L[a][l]*A[b][e][a]*B[b]*E[e]

# # print(PF) # [0.25, 0.7499999999999999]
# # print(PF[0] + PF[1]) # 0.9999999999999999

# # # under intervention A=1
# # B = [0.99, 0.01]
# # E = [0.98, 0.02]
# # # outer index is B; inner is E. don't do this at home.
# # A = [[[0, 1], [0, 1]], [[0, 1], [0, 1]]]
# # # outer index is value of A
# # F = [[0.95, 0.05], [0.25, 0.75]]
# # L = [[0.90, 0.10], [0.05, 0.95]]

# # # P(F) -- naive
# # PF = [0, 0]
# # for f in [0, 1]:
# #     for b in [0,1]: 
# #         for e in [0,1]:
# #             for a in [0,1]:
# #                 for l in [0,1]:
# #                     # P(F|A)P(L|A)P(A|B,E)P(B)P(E)
# #                     PF[f] += F[a][f]*L[a][l]*A[b][e][a]*B[b]*E[e]

# # print("do(A:=1)") # 0.9999999999999999
# # print(PF) # [0.25, 0.7499999999999999]

# # PF = [0,0]
# # for a in [1]:
# #     for f in [0,1]:
# #         for l in [0,1]:
# #             PF[f] += F[a][f]*L[a][l]
# # print(PF)


