package com.example.movie.data.remote

import com.example.movie.data.remote.dto.MovieGenres
import com.example.movie.data.remote.dto.MovieResponse
import com.example.movie.database.MovieDatabase
import io.ktor.client.HttpClient
import io.ktor.client.engine.cio.CIO
import io.ktor.client.plugins.contentnegotiation.ContentNegotiation
import io.ktor.client.plugins.logging.LogLevel
import io.ktor.client.plugins.logging.Logging
import io.ktor.serialization.kotlinx.json.json
import kotlinx.serialization.json.Json
import kotlinx.serialization.serializer

interface MovieService {
    suspend fun getMovies() : MovieResponse
    suspend fun getGenres(): MovieGenres

    companion object {
        fun create(): MovieService {
            return MovieServiceImplementation(
                client = HttpClient(CIO){
                    install(Logging){
                        level = LogLevel.ALL
                    }
                    install(ContentNegotiation) {
                        json(Json {
                            ignoreUnknownKeys = true
                        })
                    }
                }
            )
        }
    }
}