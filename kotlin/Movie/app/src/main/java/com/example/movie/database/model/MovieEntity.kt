package com.example.movie.database.model

import androidx.room.Entity
import androidx.room.PrimaryKey
import kotlinx.serialization.SerialName

@Entity
data class MovieEntity(
    @PrimaryKey(autoGenerate = true)
    val id : Int,
    var favourite : Boolean = false,
    val adult : Boolean,
    val backdropPath : String,
    val genreIds : List<Int>,
    val originalLanguage : String,
    val originalTitle : String,
    val overview : String,
    val popularity : Double,
    val posterPath : String,
    val releaseDate : String,
    val title : String,
    val video : Boolean,
    val voteAverage : Double,
    val voteCount : Int
)

