#import os

# Initializing some variables
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
L = 0

# Question List
question =  ["How do you typically react when faced with uncertainty or unknown situations?",
             "When encountering a challenging problem, what emotion do you usually experience?",
             "How do you typically respond to unexpected positive news or events?",
             "In difficult times, which emotion tends to dominate your feelings?",
             "Which emotion best describes your reaction to witnessing an act of kindness?"]
options = "A.Fear\nB.Violence\nC.Sadness\nD.Joy\nE.Disgust\nF.Suprise\nG.Trust"

# start of actual program
print("_____________________________________________________________________")
print("                                                                     ")
print("                           Welcome to the                            ")
print("                           Personality Test                          ")
print("                                                                     ")
print("            Made By: Ronan Donovan (Psychologist)            ")
print("_____________________________________________________________________")
print("                                                                     ")
print("                  When ready to start, press enter:                  ")
response = input("")

# Loop of Questions
while True:
    L = L+1
    L = str(L)
   # os.system(
        #"D:\megathon\3.jpg")
    L = int(L)
    print(" ")
    print(question[L-1])
    print("")
    print(options)
    response = input(
        "Please Type the Corresponding Letter of your Answer\n")
    if response == "a":
        a = a+1
        pass
    if response == "b":
        b = b+1
        pass
    if response == "c":
        c = c+1
        pass
    if response == "d":
        d = d+1
        pass
    if response == "e":
        e = e+1
        pass
    if response == "f":
        f = f+1
        pass
    if response == "g":
        g = g+1
        pass
    if response == "stop":
        break
    if L == 5:
        break
print("Time to see the results, hit enter for a graph")

# Making Graph
while L == 5:
    response = input("")
    import matplotlib.pyplot as plt
    labels = 'Fear', 'Violence', 'Sadness', 'Joy', 'Disgust', 'Suprise', 'Trust'
    sizes = [a, b, c, d, e, f, g]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    plt.title('Type of Response')
    plt.show()
    # Making Conclusions
  #  for i in range(75):
        #print("  ")
    print("To See Final Results, Hit Enter")
    response = input("")
    if a >= 3:
        print("You tend to see the world in a fearful way")
    if b >= 3:
        print(
            "You have tendency to see violence - Consider taking a real schizophrenia test")
    if c >= 3:
        print("You have a tendency towards sadness.")
    if d >= 3:
        print("You are a naturally joyful person :) ")
    if e >= 3:
        print("Your default perception is disgust.")
    if f >= 3:
        print("Things often take you by suprise!")
    if g >= 3:
        print("You tend to trust those around you.")
    print("________________________________________________________________")
    print("                                                                ")
    print("                    Thank You for Taking the                    ")
    print("                        Personality Test                        ")
    print("                                                                ")
    print("________________________________________________________________")
    break
