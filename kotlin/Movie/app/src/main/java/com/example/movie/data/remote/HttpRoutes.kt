package com.example.movie.data.remote

object HttpRoutes {
    private const val BASE_URL = "https://api.themoviedb.org/3"

    const val POPULAR_URL = "${BASE_URL}/movie/popular?language=en-US&page=1"
    const val GENRE_LIST = "${BASE_URL}/genre/movie/list?language=en'"
}