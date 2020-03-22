# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r")
email_two = open("email_two.txt", "r")
email_three = open("email_three.txt", "r")
email_four = open("email_four.txt", "r")
teste = open('teste.txt','r')


def closing_file(email,lista):
    path = email.name
    email.close()
    texto = " ".join(lista)
    file_w = open(path,'w')
    file_w.write(texto+'/n')
    file_w.close()



def censor(email,badWord):

    email_txt = email.read().strip().lower()
    list_email = email_txt.split()
    list_aux = []

    if type(badWord) is list:
        list_badWord = badWord
    else:
        list_badWord = badWord.split()

    for i in list_email:
        if i in list_badWord:
             list_aux.append("ééé")
        else:
             list_aux.append(i)
        
    closing_file(email,list_aux)
