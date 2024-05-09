package com.example.movie

import android.os.Bundle
import android.widget.EditText
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.runtime.Composable
import androidx.compose.runtime.produceState
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import androidx.lifecycle.lifecycleScope
import com.example.movie.data.remote.MovieService
import com.example.movie.data.remote.MovieServiceImplementation
import com.example.movie.data.remote.dto.MovieResponse
import io.ktor.websocket.Frame
import kotlinx.coroutines.launch


class MainActivity : AppCompatActivity() {
    private val service = MovieService.create()
    private lateinit var textBox: EditText

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        textBox = findViewById(R.id.Text)

        lifecycleScope.launch {
            try {
                val movieResponse = service.getMovies()
                // Now you have your data in movieResponse, update UI here
                runOnUiThread {
                    // Set the text of textBox or other UI elements here
                    textBox.setText(movieResponse.toString())
                }
            } catch (e: Exception) {
                // Handle possible errors here
                println(e.message.toString())
            }
        }
    }
}
