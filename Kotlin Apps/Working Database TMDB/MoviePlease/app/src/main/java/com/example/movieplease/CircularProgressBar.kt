package com.example.movieplease

import android.content.Context
import android.graphics.Canvas
import android.graphics.Color
import android.graphics.Paint
import android.graphics.RectF
import android.util.AttributeSet
import android.view.View
import androidx.core.content.ContextCompat

class CircularProgressBar @JvmOverloads constructor(
    context: Context, attrs: AttributeSet? = null, defStyle: Int = 0
) : View(context, attrs, defStyle) {

    private var progress: Int = 0
    private val paint = Paint()
    private val backgroundPaint = Paint()
    private val faintRingPaint = Paint()
    private val progressRingPaint = Paint()

    init {
        paint.isAntiAlias = true
        paint.strokeCap = Paint.Cap.ROUND
        paint.style = Paint.Style.FILL

        backgroundPaint.color = Color.BLACK
        backgroundPaint.style = Paint.Style.FILL

        faintRingPaint.isAntiAlias = true
        faintRingPaint.style = Paint.Style.STROKE
        faintRingPaint.strokeWidth = 20f

        progressRingPaint.isAntiAlias = true
        progressRingPaint.style = Paint.Style.STROKE
        progressRingPaint.strokeWidth = 20f
    }

    fun setProgress(progress: Int) {
        this.progress = progress
        invalidate()
    }

    override fun onDraw(canvas: Canvas) {
        super.onDraw(canvas)

        val centerX = width / 2f
        val centerY = height / 2f
        val radius = Math.min(centerX, centerY) - faintRingPaint.strokeWidth

        // Draw solid black background
        canvas.drawCircle(centerX, centerY, radius, backgroundPaint)

        // Set faint ring color
        faintRingPaint.color = getFaintColorForProgress(progress)

        // Draw faint ring
        canvas.drawCircle(centerX, centerY, radius, faintRingPaint)

        // Set progress color
        progressRingPaint.color = getColorForProgress(progress)

        // Draw progress arc
        val rectF = RectF(centerX - radius, centerY - radius, centerX + radius, centerY + radius)
        canvas.drawArc(rectF, -90f, (progress * 3.6).toFloat(), false, progressRingPaint)

        // Draw the text
        paint.color = ContextCompat.getColor(context, android.R.color.white)
        paint.textSize = 40f
        val text = "$progress%"
        val textWidth = paint.measureText(text)
        val x = (width - textWidth) / 2
        val y = (height - (paint.descent() + paint.ascent())) / 2
        canvas.drawText(text, x, y, paint)
    }

    private fun getColorForProgress(progress: Int): Int {
        return when (progress) {
            in 0..29 -> 0xFFFF0000.toInt() // Red
            in 30..59 -> 0xFFFFFF00.toInt() // Yellow
            in 60..89 -> 0xFF00FF00.toInt() // Lime
            in 90..100 -> 0xFF008000.toInt() // Strong Green
            else -> 0xFF00FF00.toInt() // Default to Lime
        }
    }

    private fun getFaintColorForProgress(progress: Int): Int {
        return when (progress) {
            in 0..29 -> 0x55FF0000.toInt() // Faint Red
            in 30..59 -> 0x55FFFF00.toInt() // Faint Yellow
            in 60..89 -> 0x5500FF00.toInt() // Faint Lime
            in 90..100 -> 0x55008000.toInt() // Faint Strong Green
            else -> 0x5500FF00.toInt() // Default to Faint Lime
        }
    }
}
