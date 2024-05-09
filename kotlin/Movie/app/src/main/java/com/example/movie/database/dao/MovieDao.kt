package com.example.movie.database.dao

import androidx.room.Dao
import androidx.room.Delete
import androidx.room.Query
import androidx.room.Upsert
import com.example.movie.database.model.MovieEntity
import kotlinx.coroutines.flow.Flow

@Dao
interface MovieDao {

    @Upsert
    suspend fun insertMovie(movie: MovieEntity)

    @Delete
    suspend fun deleteMovie(movie: MovieEntity)

    suspend fun favoriteMovie(movie: MovieEntity) =
        when(movie.favourite){
            true -> movie.favourite = false
            false -> movie.favourite = true
    }

//    @Query("SELECT * FROM MovieEntity ORDER BY genreIds")
//    suspend fun orderMoviesByGenre(): Flow<List<MovieEntity>>

    @Query("SELECT * FROM MovieEntity ORDER BY popularity")
    suspend fun orderMoviesByPopularity(): Flow<List<MovieEntity>>

    @Query("SELECT * FROM MovieEntity ORDER BY favourite")
    suspend fun showFavouriteMovies(): Flow<List<MovieEntity>>

    @Query("SELECT * FROM MovieEntity ORDER BY voteAverage")
    suspend fun orderMoviesByRating(): Flow<List<MovieEntity>>

//    @Query("SELECT * FROM MovieEntity ORDER BY releaseDate")
//    suspend fun orderMoviesByReleaseDate(): Flow<List<MovieEntity>>
}