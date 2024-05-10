package com.example.movie.viewmodel

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.movie.data.remote.dto.MovieResponse
import com.example.movie.database.dao.MovieDao
import com.example.movie.database.model.MovieEntity
import com.example.movie.viewmodel.events.FilterType
import com.example.movie.viewmodel.events.MovieEvents
import com.example.movie.viewmodel.state.MovieState
import kotlinx.coroutines.ExperimentalCoroutinesApi
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.SharingStarted
import kotlinx.coroutines.flow.combine
import kotlinx.coroutines.flow.flatMapLatest
import kotlinx.coroutines.flow.stateIn
import kotlinx.coroutines.flow.update
import kotlinx.coroutines.launch

class MovieViewModel(
    private val dao: MovieDao
): ViewModel() {

    private val _filterType = MutableStateFlow(FilterType.POPULARITY)

    @OptIn(ExperimentalCoroutinesApi::class)
    private val _movies = _filterType
        .flatMapLatest { filterType ->
            when(filterType){
                FilterType.POPULARITY -> dao.orderMoviesByPopularity()
                FilterType.FAVORITES -> dao.orderFavouriteMovies()
                FilterType.RATING -> dao.orderMoviesByRating()
            }
        }
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(), emptyList<MovieEntity>())

    private val _state = MutableStateFlow(MovieState())

    val state = combine(_state, _filterType, _movies) { state, filterType, movies ->
        state.copy(
            movies = movies,
            filterType = filterType
        )
    }
    .stateIn(viewModelScope, SharingStarted.WhileSubscribed(5000), MovieState())

    fun onEvent(event: MovieEvents){
        when (event){
//            MovieEvents.FillDatabase -> {
//                fillDatabase(event.movies)
//            }

            is MovieEvents.FilterMovies -> {
                _filterType.value = event.filterType
            }
            MovieEvents.HideFilters -> {
                _state.update { it.copy(
                    isFiltering = false
                )}
            }
            MovieEvents.HideMovieInfo -> {
                _state.update {it.copy(
                    isReadingInfo = false
                )}
            }
//            is MovieEvents.RemoveMovie -> {
//                viewModelScope.launch{
//                    dao.deleteMovie(event.movie)
//                }
//            }
            MovieEvents.ShowFilters -> {
                _state.update { it.copy(
                    isFiltering = true
                ) }
            }
            MovieEvents.ShowMovieInfo -> {
                _state.update { it.copy(
                    isReadingInfo = false
                )}
            }
        }
    }

    private fun fillDatabase(movies: MovieResponse){

    }
}