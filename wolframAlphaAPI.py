#5ULE6P-UP89AYE5TV
import wolframalpha


def pregunta():
    #Next question function
    def nextQ():
        print("Do you want to continue?")
        x = input("YES/NO):")
        print("\n")
        if x == "y" or x == "yes" or x == "YES" or x == "Yes" or x == "Y":
            pregunta()
        else:
            print("Bye!")

    #Assitant function
    Qinput = input("QUESTION: ")
    app_id = "5ULE6P-UP89AYE5TV"
    client = wolframalpha.Client(app_id)
    responce = client.query(Qinput)
    answer = next(responce.results).text
    print(answer, "\n",)
    nextQ()

#wolframalpha function
pregunta()
