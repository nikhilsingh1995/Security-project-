#Security project
alphabet='abcdefghijklmnopqrstuvwxyz'
key=4
newmsg=''
oldmsg=''
message=input('Enter the message :')

for character in message:
    position=alphabet.find(character)
    newposition=(position+key)%26
    newchar=alphabet[newposition]
   # print("Encrypted new character is",newchar)
    newmsg+=newchar
print("Encrypted final message is",newmsg)

for character in newmsg:
    position=alphabet.find(character)
    oldposition=(position-key)%26
    oldchar=alphabet[oldposition]
    #print("Decrypted new character is",oldchar)
    oldmsg+=oldchar
print("Decrypted final message is",oldmsg)
