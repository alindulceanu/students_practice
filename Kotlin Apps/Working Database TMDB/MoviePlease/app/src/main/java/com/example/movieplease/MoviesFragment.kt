package com.example.movieplease

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.lifecycle.lifecycleScope
import androidx.lifecycle.ViewModelProvider
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import kotlinx.coroutines.flow.collect
import kotlinx.coroutines.launch

class MoviesFragment : Fragment() {

    private lateinit var viewModel: MovieViewModel
    private lateinit var movieAdapter: MovieAdapter
    private var filterType: FilterType = FilterType.POPULARITY

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val view = inflater.inflate(R.layout.fragment_movies, container, false)

        val recyclerView = view.findViewById<RecyclerView>(R.id.recycler_view)
        recyclerView.layoutManager = LinearLayoutManager(context)

        viewModel = ViewModelProvider(requireActivity())[MovieViewModel::class.java]

        lifecycleScope.launch {
            viewModel.state.collect { state ->
                movieAdapter = MovieAdapter(state.movies) { movie ->
                    viewModel.onEvent(MovieEvent.ShowMovieInfo(movie))
                }
                recyclerView.adapter = movieAdapter
            }
        }

        // Trigger the filter event when the fragment is created
        viewModel.onEvent(MovieEvent.FilterMovies(filterType))

        return view
    }

    companion object {
        @JvmStatic
        fun newInstance(filterType: FilterType) = MoviesFragment().apply {
            this.filterType = filterType
        }
    }
}
