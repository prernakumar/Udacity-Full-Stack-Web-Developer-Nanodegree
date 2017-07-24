import fresh_tomatoes
import media

prestige=media.Movie("Prestige","Two stage magicians engage in competitive one-upmanship in an attempt to create the ultimate stage illusion.",
                     "https://upload.wikimedia.org/wikipedia/en/d/d2/Prestige_poster.jpg",
                     "https://www.youtube.com/watch?v=o4gHCmTQDVI")

momento=media.Movie("Momento","A man juggles searching for his wife's murderer and keeping his short-term memory loss from being an obstacle. ",
                    "https://upload.wikimedia.org/wikipedia/en/c/c7/Memento_poster.jpg",
                    "https://www.youtube.com/watch?v=0vS0E9bBSL0")

dark_knight=media.Movie("Dark Knight","When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice.",
                        "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                        "https://www.youtube.com/watch?v=EXeTwQWrcwY")

inception=media.Movie("Inception","A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.",
                      "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                      "https://www.youtube.com/watch?v=8hP9D6kZseM")

toy_story=media.Movie("Toy Story","A story of a boy and his toys that come to life",
                      "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                      "https://www.youtube.com/watch?v=KYz2wyBy3kc")


avatar=media.Movie("Avatar","A marine on an alien planet",
                   "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                   "https://www.youtube.com/watch?v=5PSNL1qE6VY")



movies=[prestige,momento,dark_knight,inception,toy_story,avatar]
#school_of_rock,ratatouille,midnight_in_paris,hunger_games
fresh_tomatoes.open_movies_page(movies)
