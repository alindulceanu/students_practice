package com.example.movieplease

import androidx.lifecycle.*
import kotlinx.coroutines.flow.*
import kotlinx.coroutines.launch

class MovieViewModel(private val repository: MovieRepository) : ViewModel() {

    private val _state = MutableStateFlow(MovieState())
    val state: StateFlow<MovieState> = _state.asStateFlow()

    val movies: LiveData<List<Movie>> = repository.getAllMovies().asLiveData()

    fun onEvent(event: MovieEvent) {
        when (event) {
            is MovieEvent.ShowMovieInfo -> {
                _state.value = _state.value.copy(selectedMovie = event.movie, showMovieInfo = true)
            }
            is MovieEvent.HideMovieInfo -> {
                _state.value = _state.value.copy(showMovieInfo = false)
            }
            is MovieEvent.FilterMovies -> {
                viewModelScope.launch {
                    val filteredMovies = when (event.filterType) {
                        FilterType.POPULARITY -> repository.getAllMovies().map { it.sortedByDescending { movie -> movie.popularity } }
                        FilterType.RELEASE_DATE -> repository.getAllMovies().map { it.sortedByDescending { movie -> movie.releaseDate } }
                        FilterType.VOTE_AVERAGE -> repository.getAllMovies().map { it.sortedByDescending { movie -> movie.voteAverage } }
                        FilterType.VOTE_COUNT -> repository.getAllMovies().map { it.sortedByDescending { movie -> movie.voteCount } }
                    }
                    filteredMovies.collect { movies ->
                        _state.value = _state.value.copy(movies = movies)
                    }
                }
            }

            MovieEvent.FilterByFavourites -> TODO()
            is MovieEvent.SaveToFavourites -> TODO()
        }
    }
}

data class MovieState(
    val selectedMovie: Movie? = null,
    val showMovieInfo: Boolean = false,
    val movies: List<Movie> = emptyList()
)

class MovieViewModelFactory(private val repository: MovieRepository) : ViewModelProvider.Factory {
    override fun <T : ViewModel> create(modelClass: Class<T>): T {
        if (modelClass.isAssignableFrom(MovieViewModel::class.java)) {
            @Suppress("UNCHECKED_CAST")
            return MovieViewModel(repository) as T
        }
        throw IllegalArgumentException("Unknown ViewModel class")
    }
}
