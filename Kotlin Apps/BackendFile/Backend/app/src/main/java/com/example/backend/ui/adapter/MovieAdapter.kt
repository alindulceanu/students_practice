package com.example.backend.ui.adapter

import com.example.backend.database.Movie
import com.example.backend.database.MovieDao
import android.view.View
import android.view.ViewGroup
import android.view.LayoutInflater
import androidx.recyclerview.widget.RecyclerView
import com.bumptech.glide.Glide
import android.widget.TextView
import android.widget.ImageView
import com.example.backend.R


class MovieAdapter(private val movies: List<Movie>) : RecyclerView.Adapter<MovieAdapter.MovieViewHolder>() {
    class MovieViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        fun bind(movie: Movie) {
            itemView.findViewById<TextView>(R.id.movie_title).text = movie.title
            Glide.with(itemView.context).load("https://image.tmdb.org/t/p/w500${movie.poster_path}").into(itemView.findViewById<ImageView>(R.id.movie_image))
        }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): MovieViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.movie_item, parent, false)
        return MovieViewHolder(view)
    }

    override fun onBindViewHolder(holder: MovieViewHolder, position: Int) {
        holder.bind(movies[position])
    }

    override fun getItemCount(): Int = movies.size
}
