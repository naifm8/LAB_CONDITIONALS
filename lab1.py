movie:str = "Jhon Wick"
movie_rating:int = 3
popularity_score:float = 72.65

if movie_rating >= 4 and popularity_score > 80.00:
    print("Highly recommended")
elif movie_rating >= 3 and popularity_score >70.00:
    print("I recommended it . It is good")
elif movie_rating <= 2 and popularity_score < 50.00:
    print("You should check it out!")
else:
    print("Don't watch it. It is a waste of time")