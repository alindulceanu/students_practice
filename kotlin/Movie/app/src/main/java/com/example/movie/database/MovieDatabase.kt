package com.example.movie.database

import androidx.room.Database
import androidx.room.RoomDatabase
import com.example.movie.database.dao.MovieDao
import com.example.movie.database.model.MovieEntity

@Database(
    entities = [MovieEntity::class],
    version = 1
)
abstract class MovieDatabase: RoomDatabase() {
    abstract val dao: MovieDao
}