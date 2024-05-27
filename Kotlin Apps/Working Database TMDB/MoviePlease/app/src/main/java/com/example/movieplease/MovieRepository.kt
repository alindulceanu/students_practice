package com.example.movieplease

import io.ktor.client.*
import io.ktor.client.request.*
import io.ktor.client.statement.*
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.withContext
import kotlinx.serialization.decodeFromString
import kotlinx.serialization.json.Json

class MovieRepository(private val db: AppDatabase, private val ktorClient: HttpClient) {

    suspend fun fetchMovies(apiKey: String): List<Movie> {
        return withContext(Dispatchers.IO) {
            val response: HttpResponse = ktorClient.get("https://api.themoviedb.org/3/movie/popular?api_key=$apiKey")
            val responseBody: String = response.bodyAsText()
            val movieResponse: MovieResponse = Json.decodeFromString(responseBody)
            val movieEntities = movieResponse.results
            movieEntities.forEach {
                db.dao.insertMovie(it)
            }
            movieEntities
        }
    }

    fun getAllMovies(): Flow<List<Movie>> {
        return db.dao.getAllMovies()
    }
}
