Questions_Geography = ["Whats the capital of Morocco?: ","How many countries are there in the world?: ","Whats the biggest country in the world","How many continents are there in the world?: "]
Answers_Geography = [{"Rabat","Casablanca","Tangier","Marrakesh"},{"200","198","203","195"},{"USA","China","India","Russia"},{"6","8","7","5"}]
actual_aswers_geography = ["casablanca","195","russia","7"]
Questions_Science = ["Who's the relativity guy?: ","Who invented the light bulb?: ", "What direction do electrons travel in?: ","Whats the equation of special relativity?: "]
Answers_Science = [{"Albert Einstein", "Stepehn Hawking","Jean Paul","your mother"},{"Thomas Edison","George Floyd","Barack Obama","Stepehn curry"},{"inverse of current","wih current","right","left"},{"e=mc2 or something idk","bro did you expect me to finish this","liek cmon man","the speed of light"}]
actual_aswers_science = ["albert einstein","thomas edison","inverse of current","e=mc2 or something idk"]
order = ["A: ", "B: ", "C: ", "D: "]
while True:
    answer_number = 0
    ategory = input("Choose your category (science/geography): ").lower()
    if ategory == "geography":
        for question,set_answer,actual_answer in zip(Questions_Geography,Answers_Geography,actual_aswers_geography):
            print(question)
            for letter,answer in zip(order,set_answer):
                print(letter+answer)
            user_answer = input("Whats the answer boi: ").lower()
            if user_answer == actual_answer:
                print("Correct!")
                answer_number += 1
                continue
            else:
                print("Wrong! you're gonna have to restart now, doodoo head!")
                break
    elif ategory == "science":
    
        for question,set_answer,actual_answer in zip(Questions_Science,Answers_Science,actual_aswers_science):
            print(question)
            for letter,answer in zip(order,set_answer):
                print(letter+answer)
            user_answer = input("Whats the answer boi: ").lower()
            if user_answer == actual_answer:
                print("Correct!")
                continue
            else:
                print("Wrong! you're gonna have to restart now, doodoo head!")
                break
    else:
        print("there is no such category baka")
    if ategory == "geography" or ategory == "science" and answer_number == 4:
        input1 = input("Congrats you finished the quiz! want to do the other category? (yes/no): ")
        if input1 == "yes":
            continue
        else:
            print("you have finnished this quiz thanks so much for playing!!!!!!")
            break
    break


