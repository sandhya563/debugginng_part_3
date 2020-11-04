# def find_in_list(query, mainlis):
#     for i in range(len(mainlist)):
#         if mainlist[i] == query:
#             return i

# chars =         ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# shifted_chars = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']
# def encrypt_message(plain_msg):
#     encrypt_message = " "
#     for character in plain_message:
#         if character in chars:
#             char_index = find_in_list(character, chars)
#             new_char = shifted_chars[char_index]
#             encrypt_message = encrypt_message + new_char
#         else:
#             encrypt_message = encrypt_message + character
#     return encrypt_message
# def decrypt_message(encrypt_message):
#     decrypt_message = " "
#     for character in encrypt_msg:
#         if character in shifted_chars:
#             char_index = find_in_list(character, shifted_chars)
#             new_char = chars[char_index]
#             decrypt_message = decrypt_message + new_char
#         else:
#             decrypt_message = decrypt_message + character
#     return decrypt_message

# ############################################### Code starts from here ##################################################

# flag = True
# while True:
#     choice = input("What do you want to do? 1. Encrypt a message 2. Decrypt a message  Enter `e` or `d` respectively:-")
#     if choice == 'e':
#         plain_message = input("Enter message to encrypt??")
#         print(encrypt_message(plain_message))
#     elif choice =='d':
#         encrypt_msg = input("Enter message to decrypt?")
#         print(decrypt_message(encrypt_msg))
#     play_again = input("Do you want to try agian or Do you want to exit? (y/n)")
#     if play_again == 'y':
#         continue
#     else:
#         break
