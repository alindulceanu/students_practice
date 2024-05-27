package com.example.movieplease

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.Query
import androidx.room.Update
import androidx.room.Upsert
import kotlinx.coroutines.flow.Flow

@Dao
interface MovieDao {
    @Upsert
    suspend fun insertMovie(movie: Movie)

    @Update
    suspend fun updateMovie(movie: Movie)

    @Query("SELECT * FROM Movie")
    fun getAllMovies(): Flow<List<Movie>>

    @Query("SELECT * FROM Movie WHERE favourite = 1")
    fun getFavouriteMovies(): Flow<List<Movie>>
}
