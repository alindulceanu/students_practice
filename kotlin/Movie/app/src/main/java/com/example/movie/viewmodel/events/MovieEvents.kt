package com.example.movie.viewmodel.events

import com.example.movie.data.remote.dto.MovieResponse

sealed interface MovieEvents {
    object ShowFilters: MovieEvents
    object HideFilters: MovieEvents
    object ShowMovieInfo: MovieEvents
    object HideMovieInfo: MovieEvents
    data class FilterMovies(val filterType: FilterType): MovieEvents
//    data class FillDatabase(val movies: MovieResponse) : MovieEvents
//    data class RemoveMovie(val movie: MovieEntity): MovieEvents
}