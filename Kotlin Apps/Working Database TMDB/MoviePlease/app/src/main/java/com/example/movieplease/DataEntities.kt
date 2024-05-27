package com.example.movieplease

import android.os.Parcelable
import androidx.room.Entity
import androidx.room.Index
import androidx.room.PrimaryKey
import androidx.room.TypeConverters
import kotlinx.parcelize.Parcelize
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Entity(
    indices = [Index(value = ["idDatabase"], unique = true)]
)
@Parcelize
@Serializable
@TypeConverters(Converter::class)
data class Movie(
    @PrimaryKey(autoGenerate = true)
    @Transient
    val idDatabase: Int = 0,

    @Transient
    var favourite: Boolean = false,

    val adult: Boolean,
    @SerialName("backdrop_path") val backdropPath: String?,

    @SerialName("genre_ids")
    val genreIds: List<Int>,

    val id: Int,
    @SerialName("original_language") val originalLanguage: String,
    @SerialName("original_title") val originalTitle: String,
    val overview: String,
    val popularity: Double,
    @SerialName("poster_path") val posterPath: String?,
    @SerialName("release_date") val releaseDate: String,
    val title: String,
    val video: Boolean,
    @SerialName("vote_average") val voteAverage: Double,
    @SerialName("vote_count") val voteCount: Int
) : Parcelable {
    val fullPosterPath: String
        get() = "https://image.tmdb.org/t/p/w500$posterPath"
}

@Serializable
data class MovieResponse(
    val page: Int,
    val results: List<Movie>,
    val total_pages: Int,
    val total_results: Int
)
