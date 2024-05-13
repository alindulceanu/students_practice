package com.example.backend

import com.example.backend.database.AppDatabase
import com.example.backend.network.createHttpClient
import android.os.Bundle
import android.util.Log
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity
import androidx.compose.material3.Button
import androidx.lifecycle.lifecycleScope
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import androidx.room.Room
import com.example.backend.repository.MovieRepository
import com.example.backend.ui.adapter.MovieAdapter
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext

class MainActivity : AppCompatActivity() {

    private lateinit var movieAdapter: MovieAdapter
    private lateinit var recyclerView: RecyclerView
    private lateinit var database: AppDatabase

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        recyclerView = findViewById(R.id.recyclerView)
        val layoutManager = LinearLayoutManager(this, LinearLayoutManager.HORIZONTAL, false)
        recyclerView.layoutManager = layoutManager

        database = Room.databaseBuilder(
            applicationContext,
            AppDatabase::class.java, "database-name"
        ).build()

        val movieDao = database.movieDao()
        val client = createHttpClient()
        val apiKey = "b37616b149ecfd201b476bcc991f1fe8"
        val repository = MovieRepository(client, apiKey)
        val button = findViewById<Button>(R.id.buton)
        button.setOnClickListener{
            lifecycleScope.launch {
                repository.fetchPopularMovies()
            }
        }

        lifecycleScope.launch {
            try {
                val movies = repository.fetchPopularMovies()
                withContext(Dispatchers.Main) {
                    movieAdapter = MovieAdapter(movies)
                    recyclerView.adapter = movieAdapter
                }
            } catch (e: Exception) {
                Log.e("MainActivity", "Error fetching movies", e)
            }
        }
    }
}