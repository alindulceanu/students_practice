package com.example.movieplease

import android.content.Context
import androidx.room.Database
import androidx.room.Room
import androidx.room.RoomDatabase
import androidx.room.TypeConverters


@Database(
    entities = [Movie::class],
    version = 1
)
@TypeConverters(Converter::class)

abstract class AppDatabase : RoomDatabase() {

    abstract val dao: MovieDao
}