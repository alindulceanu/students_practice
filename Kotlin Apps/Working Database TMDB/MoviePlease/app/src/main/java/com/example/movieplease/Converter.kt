package com.example.movieplease

import androidx.room.TypeConverter
import com.google.gson.Gson
import com.google.gson.reflect.TypeToken

class Converter {
    @TypeConverter
    fun fromGenreIdsList(genreIds: List<Int>?): String? {
        return if (genreIds == null) null else Gson().toJson(genreIds)
    }

    @TypeConverter
    fun toGenreIdsList(genreIdsString: String?): List<Int>? {
        return if (genreIdsString == null) null else {
            val listType = object : TypeToken<List<Int>>() {}.type
            Gson().fromJson(genreIdsString, listType)
        }
    }
}
