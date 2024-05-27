package com.example.movieplease

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.bumptech.glide.Glide
import com.example.movieplease.databinding.ActivityMovieDetailBinding

class MovieDetailActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMovieDetailBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMovieDetailBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val movie = intent.getParcelableExtra<Movie>("MOVIE")

        movie?.let {
            title = it.title

            Glide.with(this)
                .load("https://image.tmdb.org/t/p/w500" + it.posterPath)
                .into(binding.movieDetailPoster)

            binding.movieDetailTitle.text = it.title
            binding.movieDetailRating.text = "Rating: ${it.voteAverage}/10"
            binding.movieDetailDescription.text = it.overview
        }
    }
}
