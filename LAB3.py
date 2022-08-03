def main():
    print("Hello")
jokerDict = {
    "Title": "-Joker",
    "Genre": "Drama"
}

hustleDict = {
     "Title": "-Hustle",
    "Genre": "Sport"
}
jurassicDict = {
     "Title": "-Jurassic Park",
    "Genre": "Thriller"
}

pizzaTopings =[ "Onions" , "Chicken", "Pepperoni"]

moviesList = [jokerDict, hustleDict, jurassicDict]

movieTitleList = [jokerDict.get('Title'), hustleDict.get('Title'), jurassicDict.get('Title')]
genreList = [jokerDict.get('Genre'), hustleDict.get('Genre'), jurassicDict.get('Genre')]
thisdict = {
  "full_name": "Mridul",
  "student_id": 123456789,
  "pizza_toppings": pizzaTopings,
  "movies": moviesList,
  "Interesting_Genre" : genreList,
  "Movie_titles" : movieTitleList
  
}



def step4(a=None, b=None):
    newPizzaTopping = "Grilled Chicken"
    a = pizzaTopings
    a.append(newPizzaTopping)
    b = tuple(a) 
    b = sorted(b, key = lambda x: x[0]) 
        

def step5(a=None):
    print("Hello my name is "  + a["full_name"] + "." + "\nMy Student ID is " + str(a["student_id"]))


def step6(a=None):
    print("My Favourite toppings are:")
    for i in a["pizza_toppings"]:
        print("-{" + i + "}")
  
def step7(a=None):
    print("I Like to watch:")
    for i in a["Interesting_Genre"]:
        print(i)

def step8(a=None):
    print("Some of my favourite movies are:")
    for i in a["Movie_titles"]:
        print(i)     



step4(thisdict, tuple(pizzaTopings))
step5(thisdict)
print("\n\n")
step6(thisdict)
print("\n\n")
step7(thisdict)
print("\n\n")
step8(thisdict)
