package com.example.backend.database

import androidx.room.Entity
import androidx.room.PrimaryKey
import androidx.room.Dao
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import androidx.room.Database
import androidx.room.RoomDatabase
import kotlinx.serialization.Serializable


@Serializable
@Entity(tableName = "Movie")
data class Movie(
    @PrimaryKey val id: Int,
    val title: String,
    val overview: String,
    val poster_path: String,
    val vote_average: Double
)

@Dao
interface MovieDao {
    @Query("SELECT * FROM Movie")
    fun getAllMovies(): List<Movie>

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    fun insertAll(vararg movies: Movie): List<Long>
}

@Database(entities = [Movie::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun movieDao(): MovieDao
}
