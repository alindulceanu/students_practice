package com.example.movieplease

import android.annotation.SuppressLint
import android.os.Bundle
import androidx.activity.viewModels
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.lifecycleScope
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import androidx.room.Room
import com.google.android.material.tabs.TabLayout
import kotlinx.coroutines.launch

class MainActivity : AppCompatActivity() {

    private val db: AppDatabase by lazy {
        Room.databaseBuilder(
            applicationContext,
            AppDatabase::class.java, "movie-database"
        ).fallbackToDestructiveMigration()
            .build()
    }

    private val repository: MovieRepository by lazy {
        MovieRepository(db, KtorClient.instance)
    }

    private val viewModel: MovieViewModel by viewModels {
        MovieViewModelFactory(repository)
    }

    @SuppressLint("MissingInflatedId")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val recyclerView = findViewById<RecyclerView>(R.id.recycler_view)
        val movieAdapter = MovieAdapter(emptyList()) { movie ->
            // Handle movie click
        }

        recyclerView.apply {
            layoutManager = LinearLayoutManager(this@MainActivity, LinearLayoutManager.HORIZONTAL, false)
            adapter = movieAdapter
        }

        val tabLayout = findViewById<TabLayout>(R.id.tab_layout)
        tabLayout.addTab(tabLayout.newTab().setText("Popularity"))
        tabLayout.addTab(tabLayout.newTab().setText("Release Date"))
        tabLayout.addTab(tabLayout.newTab().setText("Vote Average"))
        tabLayout.addTab(tabLayout.newTab().setText("Vote Count"))

        tabLayout.addOnTabSelectedListener(object : TabLayout.OnTabSelectedListener {
            override fun onTabSelected(tab: TabLayout.Tab) {
                when (tab.position) {
                    0 -> viewModel.onEvent(MovieEvent.FilterMovies(FilterType.POPULARITY))
                    1 -> viewModel.onEvent(MovieEvent.FilterMovies(FilterType.RELEASE_DATE))
                    2 -> viewModel.onEvent(MovieEvent.FilterMovies(FilterType.VOTE_AVERAGE))
                    3 -> viewModel.onEvent(MovieEvent.FilterMovies(FilterType.VOTE_COUNT))
                }
            }

            override fun onTabUnselected(tab: TabLayout.Tab) {}
            override fun onTabReselected(tab: TabLayout.Tab) {}
        })

        // Fetch movies initially
        lifecycleScope.launch {
            viewModel.onEvent(MovieEvent.FilterMovies(FilterType.POPULARITY)) // Start with default filter
        }

        // Observe state from the ViewModel
        lifecycleScope.launch {
            viewModel.state.collect { state ->
                movieAdapter.updateMovies(state.movies)
            }
        }
    }
}
