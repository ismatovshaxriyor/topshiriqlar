""" ---------------------- 7 - masala ----------------------- """
# txt = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
# txt_list = txt.split()
# new_txt_list = []

# while True:
#     shart = input("-> ")

#     if shart == "a":
#         for word in txt_list:
#             if "." not in word:
#                 new_word = word.strip(word[0]) + word.strip(word[1:])
#                 new_txt_list.append(new_word)
#         print(new_txt_list)
#         new_txt_list.clear()
#     elif shart == "b":
#         for word in txt_list:
#             if "." not in word:
#                 new_word = word.strip(word[:-1]) + word.strip(word[-1])
#                 new_txt_list.append(new_word)
#         print(new_txt_list)
#         new_txt_list.clear()
#     elif shart == "c":
#         for word in txt_list:
#             if "." not in word:
#                 new_word = word.strip(word[0])
#                 new_txt_list.append(new_word)
#         print(new_txt_list)
#         new_txt_list.clear()
#     else:
#         print("Command not found :(")
#         break


# """ ---------------------- 26 - masala ----------------------- """
# word = input("So'z kiriting: ")
# secret_word = ''
# unsecret_word = ''

# while True:
#     shart = input("1. So'zni shifrlash \n2. So'zni deshifrlash \n3. Chiqish \n-> ")
#     if shart == "1":
#         qism1 = ''
#         qism2 = ''

#         for i in range(len(word)):
#             if i % 2 == 1:
#                 qism1 += word[i]
#             else:
#                 qism2 += word[i]
#         secret_word = qism1 + qism2[::-1]
#         print(f"Shifrlangan so'z: {secret_word}\n")
#     elif shart == '2':
#         if len(secret_word) == 0:
#             print("So'zni deshifrlashdan oldin uni shifrlangan")
#         else:
#             qism1 = list(secret_word[:(len(secret_word)//2)])
#             qism2 = list(secret_word[-len(secret_word)//2:][::-1])

#             for i in range(len(secret_word)):
#                 if i % 2 != 1:
#                     unsecret_word += qism2[0]
#                     del qism2[0]
#                 elif i % 2 != 1 and len(qism1) == 0:
#                     unsecret_word += qism2[0]
#                     del qism2[0]
#                 else:
#                     unsecret_word += qism1[0]
#                     del qism1[0]
#             print(f"Deshifrlangan so'z: {unsecret_word}\n")
#             unsecret_word = ''
#     elif shart == "3":
#         break
#     else:
#         print("Noto'g'ri buyruq kiritildi.\n")