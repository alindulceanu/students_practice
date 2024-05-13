plugins {
    alias(libs.plugins.androidApplication)
    alias(libs.plugins.jetbrainsKotlinAndroid)
    id("kotlin-kapt")
    kotlin("plugin.serialization") version "1.5.31"

}

android {
    namespace = "com.example.backend"
    compileSdk = 34

    defaultConfig {
        applicationId = "com.example.backend"
        minSdk = 24
        targetSdk = 34
        versionCode = 1
        versionName = "1.0"

        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
        vectorDrawables {
            useSupportLibrary = true
        }
    }

    buildTypes {
        release {
            isMinifyEnabled = false
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
    }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_1_8
        targetCompatibility = JavaVersion.VERSION_1_8
    }
    kotlinOptions {
        jvmTarget = "1.8"
    }
    buildFeatures {
        compose = true
    }
    composeOptions {
        kotlinCompilerExtensionVersion = "1.5.1"
    }
    packaging {
        resources {
            excludes += "/META-INF/{AL2.0,LGPL2.1}"
        }
    }
}

dependencies {

    implementation("com.google.android.material:material:1.4.0")
    implementation("androidx.appcompat:appcompat:1.x.x")
    implementation(libs.androidx.core.ktx)
    implementation(libs.androidx.lifecycle.runtime.ktx)
    implementation(libs.androidx.activity.compose)
    implementation(platform(libs.androidx.compose.bom))
    implementation(libs.androidx.ui)
    implementation(libs.androidx.ui.graphics)
    implementation(libs.androidx.ui.tooling.preview)
    implementation(libs.androidx.material3)
    // Ktor for network operations
    implementation("io.ktor:ktor-client-android:1.6.7")
    implementation("io.ktor:ktor-client-serialization:1.6.7")
    implementation("io.ktor:ktor-client-core:<version>")
    implementation("io.ktor:ktor-client-json:<version>")
    implementation("io.ktor:ktor-client-android:<version>")
    implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:1.3.2")
    implementation("org.jetbrains.kotlin:kotlin-stdlib-jdk7:1.5.31")
    implementation("org.jetbrains.kotlin:kotlin-stdlib-jdk8")
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-android:1.5.0")


// Room components
    implementation("androidx.room:room-runtime:2.3.0")
    implementation(libs.androidx.appcompat)
    implementation(libs.androidx.viewpager2)
    kapt("androidx.room:room-compiler:2.3.0")
    implementation("androidx.room:room-ktx:2.3.0")
    implementation("com.github.bumptech.glide:glide:4.12.0")
    kapt("com.github.bumptech.glide:compiler:4.12.0")

// RecyclerView
    implementation("androidx.recyclerview:recyclerview:1.2.1")

// Kotlin Serialization
    implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:1.3.0")
    testImplementation(libs.junit)
    androidTestImplementation(libs.androidx.junit)
    androidTestImplementation(libs.androidx.espresso.core)
    androidTestImplementation(platform(libs.androidx.compose.bom))
    androidTestImplementation(libs.androidx.ui.test.junit4)
    debugImplementation(libs.androidx.ui.tooling)
    debugImplementation(libs.androidx.ui.test.manifest)
}