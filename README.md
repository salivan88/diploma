# System of personalized video production recommendations

This project is a bachelor's diploma work, the purpose of which is to develop a system of personalized movies recommendations using machine learning methods. The project has a web device on Django, which allows users to receive personal recommendations based on movies.


## Functionality

- Guest mode with *fast* recommendations (popular movies).
- registration and authorization of users.
- Ability to put on movies.
- Generation of personalized recommendations using **used-based colaborative filtering**.
- Integration with **TMDB API** for dynamic receipt of movies information.
- Admin-panel for managing users and data.

## Used technologies

- **Python**, **Django** (backend)
- **SQLite** (database)
- **HTML/CSS/JavaScript** (fronend)
- **TMDB API** - to obtain metadata movies
- **Pandas**, **NumPy** - for data processing
- **Git/Github** - version control system
- **MovieLens dataset** - as a source of marked data


## TMDB API
To receive movies data, you need a [TMDB API key](https://developer.themoviedb.org/docs/getting-started). After registration, add it to the `.env` or direction to the code, depending on the implementation.

## Database

[MovieLens](https://grouplens.org/datasets/movielens/latest/) daset is used. It includes:

1. Ratings.csv - Film estimates by users
2. Links.csv - movieId comparison with ID on TMDB

A small set of data from the Movielens service was used for this project. It has films evaluation data from 600 different users. In order not to have problems displaying recommendations, another archive file was used, namely Links.csv. He had a relevance to Movieid from ID movies in popular database

## Full thesis

The full text of the bachelor's work can be found in the file [`Diploma-Report-halchyshak.pdf`] (Docs/Diploma-Report-halchyshak.pdf).

# Author
+ Yaroslav Halchyshak
+ Computer Science
+ LNU of I. Franko
+ 2024
