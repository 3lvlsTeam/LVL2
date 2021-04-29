import random ,re

special_words = ['!', '@', '#', '$', '%', '^', '&','*', ':', '"', '?', '/', '(', ')', '+', '_']

class passwordgenerator():
        
    def password_maker(favourite_number,some_words):

        def emptyns_remover(x):
            return x !=''
        rand_list = some_words.split(" ")
        sent_list= list(filter(emptyns_remover,rand_list))
        password=''
        for letter in sent_list:
            password = password+letter[0]

        def the_mixer(pw,num):
            cont=0
            new_pass=''
            for i in pw:
                for n in num:
                    rand = random.randint(0,9)
                    if rand > 5 and cont < len(num):
                        new_pass=new_pass+num[cont]
                        cont=cont+1
                    break
                new_pass=new_pass+i    
            return new_pass

        pw_with_num = the_mixer(password,favourite_number)
        return the_mixer(pw_with_num,special_words)

    def conventer_to_list(word):
        def emptyns_remover(x):
            return x !=''
        rand_list = word.split(" ")
        return len(list(filter(emptyns_remover,rand_list)))