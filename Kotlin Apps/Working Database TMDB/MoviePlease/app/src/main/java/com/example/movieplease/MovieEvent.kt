package com.example.movieplease

sealed class MovieEvent {
    data class ShowMovieInfo(val movie: Movie) : MovieEvent()
    data object HideMovieInfo : MovieEvent()
    data object FilterByFavourites : MovieEvent()
    data class SaveToFavourites(val movie: Movie) : MovieEvent()
    data class FilterMovies(val filterType: FilterType) : MovieEvent()
}
