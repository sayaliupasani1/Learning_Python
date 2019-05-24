from question import question_class

question_prompts = [
    "What Color are Apples?\na)Red/Green\nb)Blue\nc)Black\nd)Yellow\n",
    "What Color are Bananas?\na)Orange\nb)Brown\nc)Yellow\nd)Green\n",
    "What Color are strawberries?\na)Yellow\nb)Red\nc)Purple\nd)Blue\n "
]

question_array =  [
    question_class(question_prompts[0], "a"),
    question_class(question_prompts[1], "c"),
    question_class(question_prompts[2], "b")
]

def run_test(question):
    score = 0
    for question in question_array:
        #print (question.prompt)
        answer = input(question.prompt)
        if answer == question.answer:
            score+=1
    print ("You got "+str(score)+"/"+str(len(question_array))+" Correct!")

run_test(question_prompts)
