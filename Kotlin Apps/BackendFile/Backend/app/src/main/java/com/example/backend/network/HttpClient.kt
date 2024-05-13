package com.example.backend.network

import io.ktor.client.*
import io.ktor.client.engine.android.*
import io.ktor.client.features.json.*
import io.ktor.client.features.json.serializer.*
import kotlinx.serialization.json.Json

fun createHttpClient(): HttpClient {
    val json = Json {
        ignoreUnknownKeys = true
    }
    return HttpClient(Android) {
        install(JsonFeature) {
            serializer = KotlinxSerializer(json)
        }
    }
}