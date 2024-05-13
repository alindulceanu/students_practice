package com.example.backend.repository

import com.example.backend.database.Movie
import com.example.backend.database.MovieDao
import kotlinx.serialization.json.Json
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import io.ktor.client.*
import io.ktor.client.request.*
import kotlinx.serialization.builtins.ListSerializer
import kotlinx.serialization.json.jsonArray
import kotlinx.serialization.json.jsonObject


class MovieRepository(private val client: HttpClient, private val apiKey: String) {
    private val json = Json { ignoreUnknownKeys = true }

    suspend fun fetchPopularMovies(): List<Movie> = withContext(Dispatchers.IO) {
        val url = "https://api.themoviedb.org/3/movie/popular?api_key=$apiKey"
        println("Requesting URL: $url")
        val response = client.get<List<Movie>>(url)
/*        val jsonObject = json.parseToJsonElement(response).jsonObject
        val moviesJson = jsonObject["results"]?.jsonArray
        if (moviesJson != null) {
            json.decodeFromString(ListSerializer(Movie.serializer()), moviesJson.toString())
        } else {
            emptyList()
        }*/
        println(response)
        return@withContext emptyList()
    }
}

