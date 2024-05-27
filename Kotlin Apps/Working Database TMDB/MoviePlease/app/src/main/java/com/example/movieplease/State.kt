package com.example.movieplease

import com.example.movieplease.Movie
import com.example.movieplease.SortType

data class State(
    val movies: List<Movie> = emptyList(),
    val isLoading: Boolean = false,
    val error: String? = null
)

