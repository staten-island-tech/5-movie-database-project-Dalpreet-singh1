import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)
#for dict in data:
 #   print(dict["title"])
#def search_by_year(year):
    
   # for dict in data:
    #    if dict["year"] > int(year):
     #       print(dict["title"])
    

#search_by_year(input("year:"))
#def search_by_year_range(year_start,year_end):
    
 #   for dict in data:
  #      if dict["year"] > int(year_start) and dict["year"] < int(year_end):
   #         print(dict["title"])
    

#def search_year_one(year):
#   for dict in data:
#       if dict["year"] == int(year):
#           print(dict["title"])
#search_year_one(input("year:"))

#def search_movie(title):
#   for dict in data:
#       if title.title() in dict["title"]:
#           print(dict["title"])
#search_movie(input("title:"))
def search_genre(genre):
    for dict in data:
        for genre_dict in dict["genres"]:
            if genre.capitalize() == genre_dict:
                print(dict["title"])
                break
search_genre(input("genre:"))