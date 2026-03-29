# SQL More Queries

This project covers advanced SQL concepts including user management, constraints, joins, and subqueries.

## Learning Objectives

- How to create MySQL users and manage privileges
- What PRIMARY KEY and FOREIGN KEY constraints are
- How to use NOT NULL and UNIQUE constraints
- How to retrieve data from multiple tables using JOIN and subqueries
- What UNION is and how to use it

## Requirements

- All files executed on Ubuntu 20.04 LTS using MySQL 8.0
- All SQL keywords in uppercase
- All files end with a new line
- All queries preceded by a comment describing the task

## Tasks

| File | Description |
|------|-------------|
| `0-privileges.sql` | List privileges of user_0d_1 and user_0d_2 |
| `1-create_user.sql` | Create user_0d_1 with all privileges |
| `2-create_read_user.sql` | Create database and user with SELECT only |
| `3-force_name.sql` | Table with NOT NULL name column |
| `4-never_empty.sql` | Table with id defaulting to 1 |
| `5-unique_id.sql` | Table with UNIQUE id column |
| `6-states.sql` | Create states table with PRIMARY KEY |
| `7-cities.sql` | Create cities table with FOREIGN KEY |
| `8-cities_of_california_subquery.sql` | Cities of California using subquery |
| `9-cities_by_state_join.sql` | All cities with state name using JOIN |
| `10-genre_id_by_show.sql` | Shows with at least one genre |
| `11-genre_id_all_shows.sql` | All shows with genre id or NULL |
| `12-no_genre.sql` | Shows without a genre |
| `13-count_shows_by_genre.sql` | Genre count sorted by number of shows |
| `14-my_genres.sql` | Genres of Dexter |
| `15-comedy_only.sql` | All Comedy shows |
| `16-shows_by_genre.sql` | All shows with genres or NULL |
