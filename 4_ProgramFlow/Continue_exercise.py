# # # my answer
# for i in range(21):
#     if i % 3 and i % 5 != 0:
#         print(i)
#
# #
# # # without continue
# # for x in range(21):
# #     if x % 3 != 0 and x % 5 != 0:
# #         print(x)
#
# # # using continue
# # for x in range(21):
# #     if x % 3 == 0 or x % 5 == 0:
# #         continue
# #     print(x)
#
# for x in range(21):
#     if x % (3 and 5) != 0:
#         print(x)

for x in range(21):
    if x % 3 and 5 != 0:
        print(x)
