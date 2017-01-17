import fresh_tomatoes_github
import media_github

toy_story = media_github.Movie("Toy Story", "1995", "G",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media_github.Movie("Avatar", "2009", "PG-13",
                     "The story of an ex-Marine who finds himself thrust into hostilities on an alien planet filled with exotic life forms. As an Avatar, a human mind in an alien body, he finds himself torn between two worlds, in a desperate fight forhis own survival and that of the indigenous people.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

gladiator = media_github.Movie("Gladiator", "2000", "R",
                        "Commodus takes power and strips rank from Maximus, one of the favored generals of his predecessor and father, Emperor Marcus Aurelius, the great stoical philosopher. Maximus is then relegated to fighting to the death in the gladiator arenas.",
                        "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
                        "https://www.youtube.com/watch?v=AxQajgTyLcM")

dark_knight = media_github.Movie("The Dark Knight", "2008", "PG-13",
                          "Batman has been able to keep a tight lid on crime in Gotham City. But when a vile young criminal calling himself the Joker suddenly throws the town into chaos, the caped Crusader begins to tread a fine line between heroism and vigilantism.",
                          "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                          "https://www.youtube.com/watch?v=_PZpmTj1Q8Q")

incredibles = media_github.Movie("The Incredibles", "2004", "PG",
                          "Superheroes are forced to assume mundane lives after all super-powered activities have been banned. Mr. Incredible gets a new chance at adventure when summoned to an island to battle an out-of-control robot.",
                          "https://upload.wikimedia.org/wikipedia/en/e/ec/The_Incredibles.jpg",
                          "https://www.youtube.com/watch?v=1LASc8ewLaw")

aviator = media_github.Movie("The Aviator", "2004", "PG-13",
                      "An aviation pioneer who helps build TWA into a major airline. But in private, Hughes remains tormented, suffering from paralyzing phobias and depression. The higher he rises, the farther has to fall. Here is more random text to get this sumary to another line",
                      "https://upload.wikimedia.org/wikipedia/en/f/f7/The_Aviator_Poster.jpg",
                      "https://www.youtube.com/watch?v=zikFDK4cuQA")

transformers = media_github.Movie("Transformers", "2007", "PG-13",
                      "Two Transformer factions, the Autobots led by Optimus Prime and the Decepticons led by Megatron. Optimus jettisoned the AllSpark, a mystical artifact that brings life to the planet, into space, but Megatron pursued it.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BNDg1NTU2OWEtM2UzYi00ZWRmLWEwMTktZWNjYWQ1NWM1OThjXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                      "https://www.youtube.com/watch?v=UxI_JI6chas")

gotg = media_github.Movie("Guardians of the Galaxy", "2014", "PG-13",
                      '''Brash space adventurer Peter Quill finds himself the quarry of relentless bounty hunters after he steals an orb coveted by Ronan, a powerful villain.''',
                      "https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg",
                      "https://www.youtube.com/watch?v=B16Bo47KS2g")

shawshank_redemption = media_github.Movie("Shawshank Redemption", "1994", "R",
                      "In 1946, a banker is convicted of a double murder, even though he stubbornly proclaims his innocence. He's sentenced to a life term at the Shawshank State Prison in Maine, where another lifer picks him as the new recruit most likely to crack under the pressure.",
                      "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                      "https://www.youtube.com/watch?v=6hB3S9bIaco")


movies = [toy_story, avatar, gladiator, dark_knight, incredibles, aviator, transformers, gotg, shawshank_redemption]
fresh_tomatoes_github.open_movies_page(movies)

