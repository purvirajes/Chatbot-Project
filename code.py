#LIBRARIES IMPORTED
import random
from textblob import TextBlob   #mention pip install
import re
import time
                                                    #FUNCTIONS CREATED

#funcn1
def exercise(r):
  if r=='Push-ups':
    steps=["1.	Get on the ground to a plank position. Place hands slightly wider than the shoulders, keeping elbows slightly bent",
           "2.	Straighten arms and legs, contracting abs and tightening the core.",
           "3.	Inhale slowly when bending the elbows and lower to the floor until chest almost touches the floor",
           "4.	Exhale while contracting chest muscles and push back up to return to start position", 
           "5.	Repeat"]
    for a in steps:
      print(a)
      time.sleep(2)  #add a second delay after printing each line
  elif r=='Sit-ups':
    steps=["1.	Lie back on a mat, bend knees and place feet flat on the floor",
           "2.	Cross hands over the chest",  
           "3.	Engage the core before starting",
           "4.	Slowly lift head and curl upper body all the way up towards the knees and exhale as you lift",
           "5.	Then return to starting position slowly by lowering down returning to starting point. Inhale as you lower",
           "6.	Repeat" ]
    for a in steps:
      print(a)
      time.sleep(2)
  elif r=='Squats':
    steps=["1.	Stand straight with feet shoulder-width apart, tighten the stomach abdominal",
           "2.	Lower down and bend knees to 90 degree angle and press hips back ",
           "3.	Press heels into floor then return to initial position",
           "4.	Repeat" ]
    for a in steps:
      print(a)
      time.sleep(2)
  elif r=='Lunges':
    steps=["1.	Position standing with feet hip-width apart", 
           "2.	With 1 leg take large step forward", 
           "3.	Lower down by bending both knees to near 90 degree angle", 
           "4.	Push back up to starting position by driving through the front foot heel",
           "5.	Repeat"]
    for a in steps:
      print(a)
      time.sleep(2)
  elif r=='Planks':
    steps=[ "1.	Position into a push-up with elbows being under the shoulder", 
            "2.	Keep forearms parallel to each other, pressing into them and rise up on your toes, engage the abdominals",
            "3.	Look on floor to keep head in straight alignment and hold onto the position for as long as possible"]
    for a in steps:
      print(a)
      time.sleep(2)
 

#funcn2
def bmr(height,weight,age):
  bmr = 88.36 + (13.4 * float(weight)) + (4.8 * float(height) * 100) - (5.7 * age)
  return bmr

#funcn3
def wanna(ex):
  res=[f"Fitbot: Wanna try some  {ex}?",f"Fitbot: How about trying some  {ex} then?", f"Fitbot: Would you like to try some  {ex}?"]
  return random.choice(res)

funcn4 (Function not needed now)
def outOfAns():
    response = [f"Fitbot: I am afraid I didn't get you {name} ",
                "Fitbot: What do you mean?",
                "Fitbot: Could you please put that in simple words for me? ",
                "Fitbot: Pardon?",
                "Fitbot: Um..Sorry what?",
                "Fitbot: What does that mean?"][
        random.randrange(6)]
    return response


#funcn5
# Define a function to handle user input
def handle_input(input_text):
    # Clean the input text by removing non-alphanumeric characters and converting to lowercase
    cleaned_text = re.sub(r'[^\w\s]', '', input_text).lower()
    
    # Use TextBlob to perform sentiment analysis on the input text
    sentiment = TextBlob(cleaned_text).sentiment.polarity
    
    if 'motiv' in cleaned_text or 'inspi' in cleaned_text or 'encourage' in cleaned_text:    #order matters if/elif motiv/ex
        print("Fitbot:",random.choice(motivational_quotes))
        response=input(f"{name}: ")
        if 'one'  or 'once'  or 'again'  or 'more' in response:
            return random.choice(motivational_quotes)
        
    
    elif "ex" in cleaned_text or "workout" in cleaned_text: #'ex' in is much better than 'exercises' in~ to accept typos and lingos
        if sentiment > 0:
            print("Fitbot: That's great! What kind of exercise do you enjoy doing?")
            time.sleep(2)
            while True:
               r=random.choice(exercises)
               print(wanna(r))
               response=input(f"{name}: ")
               
    
               if 'no' in i.lower() or "don't" in i.lower() or "dont" in i.lower(): 
                     continue
               else:
                      exercise(r)
                      break

                  

        else:
          print("Fitbot: I know exercise can be tough, but it's worth it in the end. What kind of exercise do you usually do?")
          time.sleep(2)
          while True:
               r=random.choice(exercises)
               print(wanna(r))
               response=input(f"{name}: ")
               #for i in response.split():
    
               if 'no' in response or "don't" in response or "dont" in response: 
                     continue
               else:
                      exercise(r)
                      break
        response= "Anything more that I can help you with or is it a goodbye?"

     elif "diet" in cleaned_text or "nutrition" in cleaned_text:
        if sentiment > 0:
            response = "Good for you! What kind of healthy foods do you like to eat?"
        else:
            response = "I know eating healthy can be challenging, but it's important for your fitness goals. What kind of healthy foods do you usually eat?"
    
    elif "personalised" in cleaned_text or "plan" in cleaned_text or "ye" in cleaned_text:
        print("Fitbot: Do you want me to provide you with some personalised plans? ")
        response= input(f"{name}: ")
        for j in response.split():
    if 'ye' in j.lower() or "great" in j.lower() or "please" in j.lower() or 'ofc' in j.lower() or 'of c' in j.lower(): 
                     print("Fitbot: Let's begin with some questions then")
                     print("Fitbot: How old are you", name,"?")
                     age = int(input(f"{name}: "))
                     print("Fitbot: What's your gender?")
                     gender = input(f"{name}: ")
                     print("Fitbot: What's your weight in kilograms?")
                     weight = input(f"{name}: ")
                     print("Fitbot: What's your height in meters?")
                     height = input(f"{name}: ")
                     goal= input("Fitbot: Do you want to lose or gain weight? ")
                     for i in height.split():
    
                          if 'no' in i.lower() or 'dont' in i.lower() or "don't" in i.lower()  : 
                            if gender.lower=="male":
                                height=1.75

                            else:
                                height=1.62
                     for j in weight.split():
    
                         if 'no' in j.lower()or 'dont' in j.lower() or "don't" in j.lower() : 
                            if gender.lower=="male":
                                weight=85.4
      
                            else:
                                weight=72.1
                     if 'lose' in goal.lower():
                             calories = bmr(height,weight,age) * 0.8
                     elif 'gain' in goal.lower():
                             calories = bmr(height,weight,age) * 1.2
                     else:
                             calories = bmr(height,weight,age)

                     if calories < 1200:
                            level = "Beginner"
                     elif calories < 2000:
                            level = "Intermediate"
                     else:
                            level = "Advanced"
                            
                     if level == "Beginner":
                            print(f"Hi {name}, here's your personalized workout plan for {goal}:\n"
                                  f"1. 10 minutes of stretching\n"
                                  f"2. 20 minutes of cardio (e.g., walking or jogging)\n"
                                  f"3. 3 sets of 10 reps of push-ups\n"
                                  f"4. 3 sets of 10 reps of squats\n"
                                  f"5. 3 sets of 10 reps of lunges\n"
                                  f"6. 10 minutes of cool-down exercises")
                     elif level == "Intermediate":
                            print(f"Hi {name}, here's your personalized workout plan for {goal}:\n"
                                  f"1. 10 minutes of stretching\n"
                                  f"2. 30 minutes of cardio (e.g., running or cycling)\n"
                                  f"3. 3 sets of 12 reps of push-ups\n"
                                  f"4. 3 sets of 12 reps of squats\n"
                                  f"5. 3 sets of 12 reps of lunges\n"
                                  f"6. 3 sets of 12 reps of bicep curls\n"
                                  f"7. 3 sets of 12 reps of tricep extensions\n"
                                  f"8. 10 minutes of cool-down exercises")
                     else:
                            
                            print(f"Hi {name}, here's your personalized workout plan for {goal}:\n"
                                  f"1. 10 minutes of stretching\n"
                                  f"2. 40 minutes of cardio (e.g., running or cycling)\n"
                                  f"3. 3 sets of 15 reps of push-ups\n"
                                  f"4. 3 sets of 15 reps of squats\n"
                                  f"5. 3 sets of 15 reps of lunges\n"
                                  f"6. 3 sets of 15 reps of bicep curls\n"
                                  f"7. 3 sets of 15 reps of tricep extensions\n"
                                  f"8. 10 minutes of cool-down exercises")
                     break

        response= "Anything more that I can help you with or is it a goodbye ?"          

    else:
          prompt= input_text
                                                            #funcn not needed now: print(outOfAns())
          reply = openai.Completion.create(engine="text-davinci-002",prompt=prompt,max_tokens=1000)
          response = reply.choices[0].text.strip()  
          #print(response)                                             
          time.sleep(1)
        
    
    
    return response    
